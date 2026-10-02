import json, os, time
from flask import Flask, render_template, request, jsonify
import data as D

app = Flask(__name__)
BASE = os.path.dirname(os.path.abspath(__file__))
EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


def album_photos():
    """Scan static/img/album/<slug>/ — cukup taruh foto di folder kategori."""
    out = []
    for c in D.ALBUMS:
        d = os.path.join(BASE, "static", "img", "album", c["slug"])
        if os.path.isdir(d):
            for f in sorted(os.listdir(d)):
                if os.path.splitext(f)[1].lower() in EXT:
                    out.append({"src": f"img/album/{c['slug']}/{f}", "cat": c["slug"]})
    return out


@app.route("/")
def index():
    return render_template("index.html", photos=album_photos(), **D.__dict__)


@app.post("/contact")
def contact():
    n, e, m = (request.form.get(k, "").strip() for k in ("nama", "email", "pesan"))
    if not (n and "@" in e and m):
        return jsonify(ok=False, msg="Mohon lengkapi nama, email valid, dan pesan."), 400
    with open(os.path.join(BASE, "messages.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps({"waktu": time.strftime("%Y-%m-%d %H:%M:%S"), "nama": n, "email": e, "pesan": m}, ensure_ascii=False) + "\n")
    return jsonify(ok=True, msg="Terima kasih! Pesan Anda sudah terkirim.")


if __name__ == "__main__":
    app.run(debug=True)
