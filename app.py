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


def debug_env():
    """SEMENTARA: tampilkan NAMA variabel terkait (tanpa isinya) untuk mendiagnosis env kosong."""
    kunci = sorted(k for k in os.environ if any(t in k.upper() for t in ("SMTP", "STMP", "MAIL", "PASS", "USER")))
    kunci = [k for k in kunci if k not in ("USER", "LOGNAME")]
    sha = os.environ.get("VERCEL_GIT_COMMIT_SHA", "")[:7] or "?"
    return f"env={os.environ.get('VERCEL_ENV', '?')};commit={sha};nama_terlihat={','.join(kunci) or 'tidak_ada'}"


def kirim_email(n, e, m):
    """Kirim pesan ke email Anda. Return (berhasil, kode_alasan).

    Kredensial dibaca dari environment variable (JANGAN ditulis di kode):
      SMTP_USER = alamat Gmail Anda
      SMTP_PASS = App Password 16 karakter (tanpa spasi)
    """
    user = os.environ.get("SMTP_USER", "").strip()
    pw = os.environ.get("SMTP_PASS", "").replace(" ", "").strip()
    kosong = [k for k, v in (("SMTP_USER", user), ("SMTP_PASS", pw)) if not v]
    if kosong:
        print("Variabel belum terbaca di server:", ", ".join(kosong))
        return False, "env_kosong:" + "+".join(kosong) + " | " + debug_env()
    msg = EmailMessage()
    msg["Subject"] = f"Pesan portfolio dari {n}"
    msg["From"] = user
    msg["To"] = user
    msg["Reply-To"] = e
    msg.set_content(f"Nama: {n}\nEmail: {e}\n\n{m}")
    try:
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as s:
                s.login(user, pw)
                s.send_message(msg)
        except smtplib.SMTPAuthenticationError:
            raise
        except OSError as err:  # port 465 tidak bisa dijangkau -> coba 587
            print("SMTP 465 gagal, mencoba 587:", repr(err))
            with smtplib.SMTP("smtp.gmail.com", 587, timeout=15) as s:
                s.starttls()
                s.login(user, pw)
                s.send_message(msg)
    except smtplib.SMTPAuthenticationError as err:
        print("Gmail menolak login:", err)
        return False, "login_ditolak"
    except Exception as err:
        print("Email gagal dikirim:", repr(err))
        return False, "smtp_error:" + type(err).__name__
    return True, ""


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
    alasan = ""
    try:
        sent, alasan = kirim_email(n, e, m)
    except Exception as err:
        print("Kesalahan tak terduga saat kirim email:", repr(err))
        alasan = "error:" + type(err).__name__

    if saved or sent:
        return jsonify(ok=True, msg="Terima kasih! Pesan Anda sudah terkirim.")
    return jsonify(ok=False, msg=f"Maaf, pesan belum bisa dikirim. Silakan hubungi lewat email. (kode: {alasan or 'tidak_diketahui'})"), 500


if __name__ == "__main__":
    app.run(debug=True)
