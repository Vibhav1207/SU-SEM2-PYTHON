class OutOfAmmoError(Exception):
    pass

class Sniper:
    def __init__(self, ammo):
        self.ammo = ammo

    def attack(self):
        if self.ammo == 0:
            raise OutOfAmmoError()
        print("Sniper attack")

try:
    s = Sniper(0)
    s.attack()
except OutOfAmmoError:
    print("Reloading...")
