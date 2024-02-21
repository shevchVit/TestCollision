import argparse
import random
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder="./templates", static_folder="./frontend")
blocks = []
drone_x = 0
drone_y = 0
drone_d = 0
collisions = []


def generate_blocks(n):
    for i in range(n):
        x = round(random.random() * 20 - 10, 2)
        y = round(random.random() * 20 - 10, 2)
        blocks.append((x, y))
        print(f"Препятствие {i} в точке ({x},{y})")


def check_square_collision(obj1, obj2):

    ox_c = (obj2[0][0] <= obj1[0][0] <= obj2[1][0] or
            obj2[0][0] <= obj1[1][0] <= obj2[1][0] or
            obj1[0][0] <= obj2[0][0] <= obj1[1][0] or
            obj1[0][0] <= obj2[1][0] <= obj1[1][0])

    oy_c = (obj2[0][1] >= obj1[0][1] >= obj2[1][1] or
            obj2[0][1] >= obj1[1][1] >= obj2[1][1] or
            obj1[0][1] >= obj2[0][1] >= obj1[1][1] or
            obj1[0][1] >= obj2[1][1] >= obj1[1][1])

    return ox_c and oy_c


def get_square_collider(center_coords, length):
    x = center_coords[0]
    y = center_coords[1]

    p = length / 2

    return [(x - p, y + p), (x + p, y - p)]


@app.route("/set_drone_coordinates", methods=['GET'])
def set_drone_coordinates():
    global drone_x
    global drone_y
    global drone_d
    global collisions

    drone_x = float(request.args.get("x"))
    drone_y = float(request.args.get("y"))
    drone_d = float(request.args.get("d"))

    drone_collider = get_square_collider((drone_x, drone_y), drone_d)

    collisions_ = []

    for i in range(len(blocks)):
        block_collider = get_square_collider(blocks[i], 1)
        if check_square_collision(drone_collider, block_collider):
            collisions_.append(i)
            print(f"Дрон столкнулся с блоком {i}")
    collisions = collisions_
    return "200"


@app.route("/get_position", methods=['GET'])
def get_position():
    return jsonify({"x": drone_x, "y": drone_y, "d": drone_d, "collisions": collisions})


@app.route("/get_blocks", methods=['GET'])
def get_blocks():
    return jsonify(blocks)


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", dest="n", type=int, help="Количество препятствий")
    generate_blocks(parser.parse_args().n)
    app.run(host="127.0.0.1", port=9000, debug=False)



