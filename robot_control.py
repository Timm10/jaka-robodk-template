from robodk import robolink, robomath
import time

RDK = robolink.Robolink('host.docker.internal', 20500)

def move_to_pick():
    target = RDK.Item("PickTarget", robolink.ITEM_TYPE_TARGET)
    robot = RDK.Item("JAKA Zu7", robolink.ITEM_TYPE_ROBOT)
    robot.MoveJ(target)

def move_to_place():
    target = RDK.Item("PlaceTarget", robolink.ITEM_TYPE_TARGET)
    robot = RDK.Item("JAKA", robolink.ITEM_TYPE_ROBOT)
    robot.MoveJ(target)

def open_gripper():
    print("[ACTION] Gripper öffnen (simuliert)")

def close_gripper():
    print("[ACTION] Gripper schließen (simuliert)")
