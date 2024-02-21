import argparse
import random
import time
import requests
import math


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--d", dest="d", type=float, help="Размер дрона")
    drone_d = parser.parse_args().d
    drone_x = 0
    drone_y = 0
    last_timestamp = time.time()
    while True:
        velocity_x = random.random() * 10 - 5
        velocity_y = random.random() * 10 - 5

        if abs(drone_x) > 10:
            drone_x = math.copysign(10, drone_x)
        if abs(drone_y) > 10:
            drone_y = math.copysign(10, drone_y)

        while -10 <= drone_x <= 10 and -10 <= drone_y <= 10:
            elapsed = time.time() - last_timestamp
            drone_x = drone_x + velocity_x * elapsed
            drone_y = drone_y + velocity_y * elapsed
            last_timestamp = time.time()
            requests.get("http://127.0.0.1:9000/set_drone_coordinates", params={
                "x": drone_x,
                "y": drone_y,
                "d": drone_d
            })
            time.sleep(0.05)


