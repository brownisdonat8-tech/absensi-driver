from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DriverLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tanggal = db.Column(db.String(20), nullable=False)
    jam_out = db.Column(db.String(10), nullable=True)
    jam_in = db.Column(db.String(10), nullable=True)
    status = db.Column(db.String(20), default="Hadir")

    def __repr__(self):
        return f"<DriverLog {self.nama} - {self.tanggal}>"
