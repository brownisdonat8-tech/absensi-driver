from flask import Flask, render_template, request, jsonify
from models import db, DriverLog
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///driver.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/simpan", methods=["POST"])
def simpan_data():
    data = request.json
    log_baru = DriverLog(
        nama=data["nama"],
        tanggal=data["tanggal"],
        jam_out=data.get("jam_out", ""),
        jam_in=data.get("jam_in", "")
    )
    db.session.add(log_baru)
    db.session.commit()
    return jsonify({"status": "sukses", "pesan": "Data berhasil disimpan"})

@app.route("/api/data", methods=["GET"])
def lihat_data():
    logs = DriverLog.query.order_by(DriverLog.id.desc()).all()
    hasil = []
    for log in logs:
        hasil.append({
            "id": log.id,
            "nama": log.nama,
            "tanggal": log.tanggal,
            "jam_out": log.jam_out,
            "jam_in": log.jam_in
        })
    return jsonify(hasil)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
