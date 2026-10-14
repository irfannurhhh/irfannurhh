import json, os, time, smtplib
from email.message import EmailMessage
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


def kirim_email(n, e, m):
    """Kirim pesan ke email Anda. Return True kalau terkirim, False kalau SMTP belum diatur.

    Kredensial dibaca dari environment variable (JANGAN ditulis di kode):
      SMTP_USER = alamat Gmail Anda
      SMTP_PASS = App Password 16 karakter (tanpa spasi)
    """
    user = os.environ.get("SMTP_USER", "").strip()
    pw = os.environ.get("SMTP_PASS", "").replace(" ", "").strip()
    if not (user and pw):
        print("SMTP_USER / SMTP_PASS belum terbaca di server")
        return False
    msg = EmailMessage()
    msg["Subject"] = f"Pesan portfolio dari {n}"
    msg["From"] = user
    msg["To"] = user
    msg["Reply-To"] = e
    msg.set_content(f"Nama: {n}\nEmail: {e}\n\n{m}")
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as s:
        s.login(user, pw)
        s.send_message(msg)
    return True


@app.route("/")
def index():
    return render_template("index.html", photos=album_photos(), **D.__dict__)


@app.post("/contact")
def contact():
    n, e, m = (request.form.get(k, "").strip() for k in ("nama", "email", "pesan"))
    if not (n and "@" in e and m):
        return jsonify(ok=False, msg="Mohon lengkapi nama, email valid, dan pesan."), 400

    saved = sent = False
    try:  # simpan ke file (hanya berhasil di laptop; di Vercel dilewati)
        with open(os.path.join(BASE, "messages.jsonl"), "a", encoding="utf-8") as f:
            f.write(json.dumps({"waktu": time.strftime("%Y-%m-%d %H:%M:%S"), "nama": n, "email": e, "pesan": m}, ensure_ascii=False) + "\n")
        saved = True
    except Exception as err:
        print("Gagal simpan file:", err)
    try:
        sent = kirim_email(n, e, m)
    except Exception as err:
        print("Email gagal dikirim:", err)

    if saved or sent:
        return jsonify(ok=True, msg="Terima kasih! Pesan Anda sudah terkirim.")
    return jsonify(ok=False, msg="Maaf, pesan belum bisa dikirim. Silakan hubungi lewat email."), 500


if __name__ == "__main__":
    app.run(debug=True)
