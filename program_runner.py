from config_helper import load_config
from sensor_loop import wait_for_light_barrier
from robot_control import move_to_pick, move_to_place, open_gripper, close_gripper
from logger_helper import logger

import time

config = load_config()
NUM_CYCLES = config.get("num_cycles", 10)

def main():
    for i in range(NUM_CYCLES):
        from logger_helper import logger
        logger.info(f"== Zyklus {i+1} ==")
        wait_for_light_barrier(i)
        move_to_pick()
        close_gripper()
        move_to_place()
        open_gripper()

if __name__ == "__main__":
    main()
