import random
import time

class VirtualLightBarrier:
    def __init__(self, name="LS1", trigger_chance=0.6):
        self.name = name
        self.trigger_chance = trigger_chance
        self.state = False

    def check_signal(self):
        self.state = random.random() < self.trigger_chance
        print(f"[I/O] {self.name} {'AKTIVIERT' if self.state else 'inaktiv'}")
        return self.state

    def wait_until_triggered(self, timeout=5.0, check_interval=0.5):
        print(f"[I/O] Warte auf {self.name} (Timeout: {timeout}s)")
        start = time.time()
        while time.time() - start < timeout:
            if self.check_signal():
                print(f"[I/O] {self.name} hat Objekt erkannt.")
                return True
            time.sleep(check_interval)
        print(f"[I/O] {self.name} hat KEIN Objekt erkannt.")
        return False
