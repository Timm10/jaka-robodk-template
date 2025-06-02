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
   - Aktiviere in RoboDK unter *Tools > Options > API*: ✔️ „Start RoboDK API when the program starts“

2. **Starte VS Code Dev Container**
   ```bash
   python program_runner.py
   ```

3. Die Konsole zeigt den Ablauf: Sensor erkennt Objekt → Pick → Place → Wiederholen (10x)

---

python program_runner.py

---

## 🔧 Konfigurationsmanagement & Validierung

Dieses Projekt nutzt `config.yaml` zur Steuerung von Betriebsparametern.  
Damit daraus robuste, überprüfte Werte entstehen, wird `config_helper.py` verwendet:

### Vorteile:
- Setzt Standardwerte automatisch
- Prüft auf Pflichtfelder
- Kann später mit `pydantic` oder `cerberus` validiert werden

### Beispielstruktur (`config.yaml`):

```yaml
robot_name: JAKA Zu7
pick_target: PickTarget
place_target: PlaceTarget
use_random_input: true
sensor_intervals: [2, 3, 1.5, 4, 2.5]






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

## 📦 GitHub-Veröffentlichung

Um dieses Projekt als GitHub-Repository zu veröffentlichen:

1. Initialisiere Git im lokalen Projektordner (nur beim ersten Mal):
   ```bash
   git init
   git add .
   git commit -m "Initial commit for JAKA Zu 7 + RoboDK"
   ```

2. Konfiguriere deine GitHub-Identität (falls nötig):
   ```bash
   git config --global user.name "Dein Name"
   git config --global user.email "deine@email.de"
   ```

3. Erstelle ein neues Repository auf [https://github.com/new](https://github.com/new)
   - Kein README anlegen (ist lokal schon enthalten)
   - Repository-Link kopieren

4. Verbinde dein lokales Repo mit GitHub:
   ```bash
   git remote add origin https://github.com/deinname/jaka-robodk-template.git
   git branch -M main
   git push -u origin main
   ```

Optional kannst du das Repo in GitHub unter **Settings** als „Template Repository“ markieren.

---

📍 Fragen, Anpassungen oder Feedback? Einfach melden – wir bauen dein Robotics-Toolkit gemeinsam aus.

neuer Code 01.06.25:

python program_runner.py

---

## 🔧 Konfigurationsmanagement & Validierung

Dieses Projekt nutzt `config.yaml` zur Steuerung von Betriebsparametern.  
Damit daraus robuste, überprüfte Werte entstehen, wird `config_helper.py` verwendet:

### Vorteile:
- Setzt Standardwerte automatisch
- Prüft auf Pflichtfelder
- Kann später mit `pydantic` oder `cerberus` validiert werden

### Beispielstruktur (`config.yaml`):

```yaml
robot_name: JAKA Zu7
pick_target: PickTarget
place_target: PlaceTarget
use_random_input: true
sensor_intervals: [2, 3, 1.5, 4, 2.5]

---

## 🧪 Simulation digitaler Ein-/Ausgänge (I/O)

Die Datei `io_simulation.py` enthält eine simulierte Lichtschranke mit zufälligem Triggersignal.

### Beispielverwendung:

```python
from io_simulation import VirtualLightBarrier

ls1 = VirtualLightBarrier(name="Lichtschranke 1")
if ls1.wait_until_triggered():
    print("Objekt erkannt, weiter mit Pick.")



