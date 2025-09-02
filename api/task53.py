from flask import Flask, request, jsonify

app = Flask(__name__)

melumat = [
    {'id': 1, 'tapsiriq': 'Zehra az daniss'},
    {'id': 2, 'tapsiriq': 'Yoruldumm'},
    {'id': 3, 'tapsiriq': 'bixdimmmm'}
]

@app.route('/tapsiriq', methods=['GET'])
def baslanqic_melumat():
    return jsonify(melumat)

@app.route('/tapsiriq', methods=['POST'])
def elave_melumat():
    yeni_melumat = request.json.get('melumat')
    if not yeni_melumat:
        return {"error": "Melumat metnini gonderin"}, 400
    yeni_id = melumat[-1]['id'] + 1 if melumat else 1
    melumat = {'id': yeni_id, 'melumat': yeni_melumat}
    melumat.append(melumat)
    return jsonify(melumat), 201

if __name__ == '__main__':
    app.run(debug=True)
