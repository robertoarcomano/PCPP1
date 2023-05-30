"""
1 CRUD = Create(POST), Read(GET), Update(PUT), Delete(DELETE)
2 Content-type: application/json; charset=utf-8
3 http://localhost:3000/cars/2 get the right ID
4 HTTP version 1.1
    4.1 it waits for the client's connection;
    4.2 it reads the client's request;
    4.3 it sends its response;
    4.4 it keeps the connection alive, waiting for the client's next request;
    4.5 if the client is inactive for some time, the server silently closes the connection;
        this means that the client is obliged to set up a new connection again
        if it wants to send another request.
"""
import requests
import json

key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]

def show_head():
    for (n, w) in zip(key_names, key_widths):
        print(n.ljust(w), end='| ')
    print()


def show_empty():
    for w in key_widths:
        print(' '.ljust(w), end='| ')
    print()


def show_car(car):
    for (n, w) in zip(key_names, key_widths):
        print(str(car[n]).ljust(w), end='| ')
    print()


def show(json):
    show_head()
    if type(json) is list:
        for car in json:
            show_car(car)
    elif type(json) is dict:
        if json:
            show_car(json)
        else:
            show_empty()


def get_and_show(headers=None):
    reply = requests.get("http://localhost:3000/cars?_sort=id&_order=asc", headers=headers)
    if reply.status_code != requests.codes.ok:
        raise Exception
    show(reply.json())
    print()


def delete_car(car_id):
    requests.delete('http://localhost:3000/cars/'+str(car_id))


def add_car(my_new_car):
    headers = {'Content-Type': 'application/json'}
    requests.post('http://localhost:3000/cars', headers=headers, data=json.dumps(my_new_car))


def edit_car(id, my_car):
    headers = {'Content-Type': 'application/json'}
    requests.put('http://localhost:3000/cars/'+id, headers=headers, data=json.dumps(my_car))


try:
    get_and_show()
    print("delete_car(7)")
    delete_car(7)
    get_and_show()
    new_car = {"id": 7,
               "brand": "Porsche",
               "model": "911",
               "production_year": 1963,
               "convertible": False}
    print("add_car(7)")
    add_car(new_car)
    get_and_show(headers={'Connection': 'Close'})
    new_car = {"id": 7,
               "brand": "Porsche",
               "model": "911",
               "production_year": 2000,
               "convertible": False}
    print("edit_car(7)")
    edit_car("7", new_car)
    get_and_show(headers={'Connection': 'Close'})

except requests.RequestException:
    print("Communication error")
except Exception as e:
        print("Server error:", e)
