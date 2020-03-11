from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/create', methods=['POST', 'GET'])
def create():
    print(request)
    people = []
    # if request.method == 'GET':
    #     name = request.args.get('name')
    #     id = request.args.get('id')
    #     phone = request.args.get('phone')
    #
    #     with open("People", "w") as file:
    #
    #         people.append(
    #             {
    #                 "id": id,
    #                 "name": name,
    #                 "phone": phone
    #             }
    #         )
    #         file.write(people)
    if request.method == 'POST':
        with open("People", "w") as file:
            data = request.data

            data = json.loads(data)
            print(data)
            for user in data:
                people.append(
                    {
                        "id": user['id'],
                        "name": user['name'],
                        "phone": user['phone']
                    }
                )
            file.write(json.dumps(people))
    return f"Succesful add", 201
#Сделал что бы можно было несколько сразу добавлять

@app.route('/user')
def get():
    with open("People", "r") as file:
        data = json.loads(file.read())
    return jsonify(data), 200


@app.route('/delete')
def delete():
    return "Hello World!", 204


app.run()
