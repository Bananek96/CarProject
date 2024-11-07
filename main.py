import json
from flask import Flask, jsonify, request
from car import Car
import threading
import time

app = Flask(__name__)

car = Car()
lock = threading.Lock()

def run_model(delta_t:float):
    while(True):
        with lock:
            car.run_model(delta_t)
        time.sleep(delta_t)

t_ref = threading.Thread(target=run_model, args=[0.1])
t_ref.deamon = True
t_ref.start()

@app.route('/forward', methods=['POST'])
def set_forward():
    speed = request.json['speed']
    with lock:
        car.move_forward(speed)
    return jsonify({'speed': speed}), 201

@app.route('/stop', methods=['POST'])
def set_stop():
    speed = request.json['speed']
    with lock:
        car.stop()
    return jsonify({'speed': speed}), 201

@app.route('/backward', methods=['POST'])
def set_backward():
    speed = request.json['speed']
    with lock:
        car.move_backwards(speed)
    return jsonify({'speed': speed}), 201

@app.route('/turn', methods=['POST'])
def set_left():
    angle = request.json['angle']
    angle = angle % 360
    with lock:
        car.turn(angle)
    return jsonify({'angle': angle}), 201

@app.route("/")
def hello_world ():
    with lock:
        text = car.__str__()
    return text, 200

if __name__ == "__main__":
    # app.run(debug=False, host='0.0.0.0')
    app.run(debug=True)
    app.run()