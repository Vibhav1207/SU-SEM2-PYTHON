class FuelLineLeakError(Exception):
    pass

class MainEngine:
    def ignite(self):
        raise FuelLineLeakError()

try:
    me = MainEngine()
    me.ignite()
except FuelLineLeakError:
    print("Engine shutdown!")
