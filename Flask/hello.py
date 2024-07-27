from flask import Flask, jsonify, request

app = Flask(__name__)

empDB = [
    {
        'id': "201",
        'name': 'Mohamad',
        'title': 'Flutter dev'
    }, {
        'id': "202",
        'name': 'Ali',
        'title': 'java dev'
    }, {
        'id': "203",
        'name': 'Ahmad',
        'title': 'python dev'
    },
]


@app.route('/')
def hello():
    return "Hello from serve"


@app.route('/empDb/employees')
def getAllEmployees():
    return jsonify({"emps": empDB})


@app.route('/empDb/employees', methods=['POST'])
def addNewEmployee():
    data = {'id': request.form['id'],
           'name': request.form['name'],
           'title': request.form['title']}
    empDB.append(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=1233)
