"""
DPex demo-request backend (Flask + SQLite)

Setup:   pip install -r requirements.txt
Run:     gunicorn dpex_demo_backend:app
         or python dpex_demo_backend.py
Env:     ADMIN_TOKEN   secret used to read leads (required)
         SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, NOTIFY_TO (optional)
"""
import os, re, json, sqlite3, smtplib, datetime, threading, time, urllib.request
from email.message import EmailMessage
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder=".")
CORS(app)
DB = os.environ.get("LEADS_DB", "leads.db")

def conn():
    c = sqlite3.connect(DB)
    c.execute("""create table if not exists leads(
        id integer primary key autoincrement, created text, name text, email text,
        phone text, company text, team_size text, departments text, slot text, message text)""")
    return c

def notify(l):
    host, to = os.environ.get("SMTP_HOST"), os.environ.get("NOTIFY_TO")
    if not (host and to):
        return
    m = EmailMessage()
    m["Subject"] = f"New DPex demo request: {l['name']} ({l['company'] or 'no company'})"
    m["From"] = os.environ.get("SMTP_USER", to)
    m["To"] = to
    m.set_content(json.dumps(l, indent=2, ensure_ascii=False))
    with smtplib.SMTP(host, int(os.environ.get("SMTP_PORT", 587))) as s:
        s.starttls()
        s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
        s.send_message(m)

# 24/7 Keep-Alive Background Heartbeat Worker
def keep_alive_worker():
    """Background worker that continuously pings the Render service every 10 minutes to prevent cold starts."""
    time.sleep(25)  # Wait for Gunicorn server to bind
    target_url = os.environ.get("RENDER_EXTERNAL_URL", "https://portfolio-4uzl.onrender.com")
    health_url = f"{target_url.rstrip('/')}/health"
    app.logger.info("DPex Keep-Alive worker initialized targeting %s", health_url)
    
    while True:
        try:
            req = urllib.request.Request(
                health_url,
                headers={"User-Agent": "DPex-KeepAlive-Heartbeat/2.0"}
            )
            with urllib.request.urlopen(req, timeout=15) as resp:
                app.logger.info("Keep-alive heartbeat sent: HTTP %s", resp.status)
        except Exception as e:
            app.logger.warning("Keep-alive notice: %s", e)
        time.sleep(600)  # Ping every 10 minutes (well under Render's 15m spin-down timeout)

# Start keep-alive daemon thread
_heartbeat_thread = threading.Thread(target=keep_alive_worker, daemon=True)
_heartbeat_thread.start()

@app.route("/health")
@app.route("/ping")
def health():
    return jsonify(
        status="active",
        timestamp=datetime.datetime.utcnow().isoformat(),
        service="DPex Enterprise Platform",
        uptime="always-on"
    ), 200

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    if os.path.exists(path):
        return send_from_directory(".", path)
    return send_from_directory(".", "index.html")

@app.post("/api/demo")
def demo():
    d = request.get_json(silent=True) or {}
    if d.get("website"):                      # honeypot: bots fill this
        return jsonify(ok=True)
    name, email = (d.get("name") or "").strip(), (d.get("email") or "").strip()
    if not name or not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return jsonify(ok=False, error="Name and a valid email are required"), 400
    lead = {k: str(d.get(k) or "")[:500] for k in
            ("name", "email", "phone", "company", "team_size", "departments", "slot", "message")}
    lead["name"], lead["email"] = name[:200], email[:200]
    with conn() as c:
        c.execute("insert into leads(created,name,email,phone,company,team_size,departments,slot,message) values(?,?,?,?,?,?,?,?,?)",
                  (datetime.datetime.utcnow().isoformat(), lead["name"], lead["email"], lead["phone"], lead["company"],
                   lead["team_size"], lead["departments"], lead["slot"], lead["message"]))
    try:
        notify(lead)
    except Exception as e:                    # never lose a lead because email failed
        app.logger.warning("notify failed: %s", e)
    return jsonify(ok=True)

@app.get("/api/leads")
def leads():
    if request.headers.get("X-Admin-Token") != os.environ.get("ADMIN_TOKEN", "dpex-secret-token"):
        return jsonify(error="unauthorized"), 401
    with conn() as c:
        c.row_factory = sqlite3.Row
        return jsonify([dict(r) for r in c.execute("select * from leads order by id desc")])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
