# JAKA Zu 7 + RoboDK + Python API Starter (Dev Template)

Dieses Projekt bildet den Startpunkt für eine simulationstaugliche JAKA-Robotersteuerung mit:

- 🦾 **RoboDK** (JAKA Zu 7 mit Pick & Place Targets)
- 🐍 **Python-Steuerung** über RoboDK-API
- 🧠 **Spätere Integration mit voraus.pioneer / voraus.core**
- 🧪 Virtuelle Sensorik (z. B. periodischer Trigger)
- 📦 Dev Container Setup für VS Code

---

## 📁 Projektstruktur

```plaintext
jaka-devkit/
├── .devcontainer/             # VS Code Container Setup
├── roboDK_project/           # .rdk-Datei mit JAKA Zu 7 Modell & Targets
├── robot_control.py          # RoboDK Bewegungslogik via API
├── sensor_loop.py            # Periodischer Sensortrigger
├── program_runner.py         # Ablaufsteuerung (10 Wiederholungen)
├── config.yaml               # Konfigurierbare Parameter (Targetnamen, Intervall)
├── README.md                 # Anleitung & Hintergrund
```

---

## 🚀 Schnellstart

1. **Starte RoboDK (lokal)**
   - Lade das `.rdk`-Projekt aus `roboDK_project/`
   - Stelle sicher: Robotername = `JAKA`, Targets = `PickTarget`, `PlaceTarget`

2. **Starte VS Code Dev Container**
   ```bash
   python program_runner.py
   ```

3. Die Konsole zeigt den Ablauf: Sensor erkennt Objekt → Pick → Place → Wiederholen (10x)

---

## ⚙️ `config.yaml` – Beispiel

```yaml
robot_name: JAKA
pick_target: PickTarget
place_target: PlaceTarget
sensor_interval: 3
```

Später: Anpassbar für andere JAKA-Typen, Tools, Bewegungsarten.

---

## 🔄 Integration in voraus.core/pioneer (geplant)

- API-Struktur und Modultrennung berücksichtigen spätere Containerisierung
- `config.yaml` als Vorläufer für `program.yaml`
- Sensorik/Steuerung erweiterbar über REST, OPC UA oder direkte Container

---

## 🧩 Nächste Ausbaustufen

- ✔️ Realistischer TCP / Toolmodelle
- ✔️ Mehrere Roboter (Typen tauschen)
- 🧠 KI-Anbindung / Copilot-Generierte Sequenzen
- 🧪 Node-RED Visualisierung (später optional)
- 📡 REST-API zur Fernsteuerung / Sensoranbindung

---

📍 Fragen, Anpassungen oder Feedback? Einfach melden – wir bauen dein Robotics-Toolkit gemeinsam aus.
