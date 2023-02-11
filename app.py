from flask import Flask, request

app = Flask(__name__)

items = [
    {
        "name": "Green Apple",
        "price": 200
    },
    {

        "name": "Momos",
        "price": 50
    },
]


@app.get('/get-items')
def get_items():
    return {"items": items}


@app.post('/add-items')
def add_items():
    request_data = request.get_json()
    items.append(request_data)
    return {"message": "Items added successfully"}, 201
