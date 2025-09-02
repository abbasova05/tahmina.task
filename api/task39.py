from flask import Flask, request, jsonify
import csv
from datetime import datetime
import os

app = Flask(__name__)
CSV_FILE = "notes.csv"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ad", "mesaj", "tarix"])

def read_notes():
    notes = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["tarix_obj"] = datetime.strptime(row["tarix"], DATETIME_FORMAT)
            notes.append(row)
    return notes

@app.route("/notes", methods=["GET", "POST"])
def notes():
    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        mesaj = request.form.get("mesaj", "").strip()

        if not ad or not mesaj:
            return jsonify({"error": "Ad və mesaj boş ola bilməz"}), 400

        now = datetime.now().strftime(DATETIME_FORMAT)
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([ad, mesaj, now])

        return jsonify({"success": True, "tarix": now})

    notes = read_notes()
    notes.sort(key=lambda x: x["tarix_obj"], reverse=True)

    for n in notes:
        n.pop("tarix_obj")
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)
