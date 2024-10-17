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
    """
    {speed: 100}
    """
    speed = request.json['speed']
    with lock:
        car.move_forward(speed)
    return jsonify({'speed': speed}), 201

@app.route('/stop')
def set_stop():
    with lock:
        car.stop()
    return "OK", 201

@app.route('/backward')
def set_backward():
    with lock:
        car.move_backwards(1)
    return "OK", 201
@app.route("/")
def hello_world():
    with lock:
        text = car.__str__()
    return text, 200

if __name__ == "__main__":
    # app.run(debug=False, host='0.0.0.0')
    app.run(debug=True)
    app.run()