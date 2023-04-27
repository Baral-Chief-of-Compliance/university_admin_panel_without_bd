from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)


@app.route("/students", methods=['POST'])
def students_update():
    if request.method == "POST":
        students = request.json["students"]

        with open("../frontend/admin_panel/src/data/students.json", 'w') as file:
            json.dump(students, file)

        return jsonify("file is changed")


@app.route("/disciplines", methods=['POST'])
def disciplines_update():
    if request.method == 'POST':
        disciplines = request.json["disciplines"]

        with open("../frontend/admin_panel/src/data/disciplines.json", 'w') as file:
            json.dump(disciplines, file)

        return jsonify("file is changed")


@app.route("/teachers", methods=['POST'])
def teachers_update():
    if request.method == 'POST':
        teachers = request.json["teachers"]

        with open("../frontend/admin_panel/src/data/teachers.json", 'w') as file:
            json.dump(teachers, file)

        return jsonify("file is changed")


if __name__ == '__main__':
    app.run(debug=True)
