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


# taking a string name variable from the url
# @app.get('/get-item/<string:name>')
# def get_item(name):
#     for item in items:
#         if name == item['name']:
#             return item
#     return {"message": "Item not found"}

@app.get('/get-item')
def get_item():
    query = request.args.get('name')
    for item in items:
        if query == item['name']:
            return item
    return {"message": "Item not found"}, 404


@app.get('/get-items')
def get_items():
    return {"items": items}


@app.post('/add-items')
def add_items():
    request_data = request.get_json()
    items.append(request_data)
    return {"message": "Items added successfully"}, 201


@app.put('/update-item')
def update_items():
    request_data = request.get_json()
    for item in items:
        if item['name'] == request_data['name']:
            item['price'] = request_data['price']
            return {"message": "Items updated successfully"}
    return {"message": "Item not available"}, 404


@app.delete('/delete-item')
def delete_item():
    query = request.args.get('name')
    for item in items:
        if query == item['name']:
            items.remove(item)
            return {"message": "Item deleted successfully"}, 200
    return {"message": "Item not found"}, 404

