from sensor_loop import wait_for_object
from robot_control import move_to_pick, move_to_place, open_gripper, close_gripper

import time

def main():
    start_time = time.time()
    max_duration = 60  # Sekunden

    while time.time() - start_time < max_duration:
        wait_for_object()
        move_to_pick()
        close_gripper()
        move_to_place()
        open_gripper()

if __name__ == "__main__":
    main()
