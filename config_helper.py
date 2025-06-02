import yaml

DEFAULTS = {
    "robot_name": "JAKA Zu7",
    "pick_target": "PickTarget",
    "place_target": "PlaceTarget",
    "use_random_input": True,
    "sensor_intervals": [2, 3, 1.5],
    "num_cycles": 10,
    "use_virtual_io": False,
    "debug_mode": True,
    "log_to_file": True
}

REQUIRED_FIELDS = ["robot_name", "pick_target", "place_target"]

def load_config(path="config.yaml"):
    try:
        with open(path, "r") as f:
            config = yaml.safe_load(f) or {}
    except FileNotFoundError:
        raise RuntimeError(f"⚠️ Konfigurationsdatei '{path}' nicht gefunden.")

    # Pflichtfelder prüfen
    for key in REQUIRED_FIELDS:
        if key not in config:
            raise ValueError(f"❌ Fehlende Konfiguration: '{key}'")

    # Defaults ergänzen
    for key, default in DEFAULTS.items():
        config.setdefault(key, default)

    return config
