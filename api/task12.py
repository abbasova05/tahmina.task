from flask import Flask, request
import csv
app = Flask(__name__)

html_sablon = '''
<!DOCTYPE html>
<html>
<head>
    <title>Flask form numunesi</title>
</head>
<body>    
<h1 style="text-align: center;"Emeliyyat secin</h1>>

<form method="POST">
    <label>Ad:</label>
    <input type="text" name="ad">
    <input type="hidden" name="emeliyyat" value="gonder">
    <input type="submit" value="Gonder">
    </form>
    <br>

<form method="POST">
    <label>Yeni ad:</label>
    <input type="text" name="ad">
    <input type="hidden" name="emeliyyat" value="yenile">
    <input type="submit" value="Yenile">
    </form>
    <br>

<form method="POST">
    <input type="hidden" name="emeliyyat" value="sil">
    <input type="submit" value="Sil">
    </form>
    <br>  
'''

@app.route("/", methods=["GET", "POST"])
def ana_sehife():
    netice = ""
    if request.method == "POST":
        emeliyyat = request.form.get("emeliyyat")
        ad = request.form.get("ad", ""). strip()

        if emeliyyat == "gonder":
            netice = f"Salam, {ad}!"
            save_to_csv(ad, emeliyyat)
        elif emeliyyat == "yenile":
        
            netice = f"Ad yeniləndi: Salam {ad}!"
            save_to_csv(ad, emeliyyat)
        elif emeliyyat == "sil":
            return "Meliumat silindi. "
        else:
            return "namelum emelliyyat"
    return "" + html_sablon + f"<p>{netice}</p>"
def save_to_csv(ad, emeliyyat):

    with open('emeliyyatlar.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ad, emeliyyat])
app.run(port=1453, debug=True, host="0.0.0.0")


