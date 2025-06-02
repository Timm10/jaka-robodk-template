from logger_helper import logger
import time
import random
from config_helper import load_config

config = load_config()
USE_RANDOM = config["use_random_input"]
sensor_intervals = config["sensor_intervals"]

def wait_for_light_barrier(cycle_index):
    if USE_RANDOM:
        t = random.uniform(1.0, 4.0)
    else:
        t = sensor_intervals[cycle_index % len(sensor_intervals)]

    print(f"[SENSOR] Wartezeit: {t:.2f}s")
    time.sleep(t)
    print("[SENSOR] Objekt erkannt!")
