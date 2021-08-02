from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [{
        "name": "Niva",
        "phone_number": 2345566
    },
    {
        "name": "Rusuna",
        "phone_number": 2345566
    },
    {
        "name": "Deepika",
        "phone_number": 2345566
    }
]


@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "It works"})


@app.route('/contacts', methods=['GET'])
def contact():
    return jsonify({"Address book": contacts})


@app.route('/contacts/<string:name>', methods=['GET'])
def contactone(name):
    con = [cont for cont in contacts if cont['name'] == name]
    return jsonify({"contact": con[0]})


@app.route('/contacts', methods=['POST'])
def add_contact():
    contact = {"name": request.json['name'], "phone_number": request.json['phone_number']}
    contacts.append(contact)
    return jsonify({"contacts": contacts})


if __name__ == '__main__':
    app.run(debug=True, port=8000)