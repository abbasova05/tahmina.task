from flask import Flask, request, render_template, jsonify
import csv
from datetime import datetime

app = Flask(__name__)
CSV_FILE = "notes.csv"

def read_notes():
    try:
        with open(CSV_FILE, newline='', encoding="utf-8") as f:
            return list(csv.reader(f))
    except FileNotFoundError:
        return []

def write_notes(notes):
    with open(CSV_FILE, "w", newline='', encoding="utf-8") as f:
        csv.writer(f).writerows(notes)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/notes", methods=["GET", "POST"])
def notes_page():
    mesaj = ""
    notes = read_notes()

    if request.method == "POST":
        ad = request.form.get("ad", "").strip()
        qeyd = request.form.get("qeyd", "").strip()

        if ad and qeyd:
            vaxt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            notes.append([ad, qeyd, vaxt])
            write_notes(notes)
            mesaj = "Qeyd uğurla əlavə edildi!"
        else:
            mesaj = "Ad və qeyd boş ola bilməz!"

    return render_template("notess.html", mesaj=mesaj, qeydlər=reversed(notes))

@app.route("/api/notes", methods=["GET"])
def api_get_notes():
    notes = read_notes()
    return jsonify(notes)

@app.route("/api/notes", methods=["POST"])
def api_add_note():
    data = request.get_json()
    if not data or "ad" not in data or "qeyd" not in data:
        return jsonify({"error": "Ad və qeyd tələb olunur"}), 400

    vaxt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes = read_notes()
    notes.append([data["ad"], data["qeyd"], vaxt])
    write_notes(notes)

    return jsonify({"message": "Qeyd əlavə edildi"}), 201

@app.route("/api/notes/<int:note_id>", methods=["PUT"])
def api_update_note(note_id):
    notes = read_notes()
    if note_id < 0 or note_id >= len(notes):
        return jsonify({"error": "Qeyd tapılmadı"}), 404

    data = request.get_json()
    ad = data.get("ad", notes[note_id][0])
    qeyd = data.get("qeyd", notes[note_id][1])
    vaxt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes[note_id] = [ad, qeyd, vaxt]
    write_notes(notes)

    return jsonify({"message": "Qeyd yeniləndi"})

@app.route("/api/notes/<int:note_id>", methods=["DELETE"])
def api_delete_note(note_id):
    notes = read_notes()
    if note_id < 0 or note_id >= len(notes):
        return jsonify({"error": "Qeyd tapılmadı"}), 404

    del notes[note_id]
    write_notes(notes)

    return jsonify({"message": "Qeyd silindi"})

if __name__ == "__main__":
    app.run(port=1453, debug=True)
