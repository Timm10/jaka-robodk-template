from robodk import robolink, robomath
from config_helper import load_config

config = load_config()
DEBUG = config.get("debug_mode", False)

def move_to_pick(robot):
    if DEBUG:
        logger.debug("DEBUG: move_to_pick() übersprungen.")
        return
    robot.MoveJ(pick_target)

robot_name = config["robot_name"]
pick_target = config["pick_target"]
place_target = config["place_target"]

RDK = robolink.Robolink('host.docker.internal', 20500)

def move_to_pick():
    target = RDK.Item(pick_target, robolink.ITEM_TYPE_TARGET)
    robot = RDK.Item(robot_name, robolink.ITEM_TYPE_ROBOT)
    robot.MoveJ(target)

def move_to_place():
    target = RDK.Item(place_target, robolink.ITEM_TYPE_TARGET)
    robot = RDK.Item(robot_name, robolink.ITEM_TYPE_ROBOT)
    robot.MoveJ(target)

def open_gripper():
    print("[ACTION] Gripper öffnen (simuliert)")

def close_gripper():
    print("[ACTION] Gripper schließen (simuliert)")
