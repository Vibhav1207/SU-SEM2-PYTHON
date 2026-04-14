class DoorOpenError(Exception):
    pass

class WashingMachine:
    def __init__(self, door_open):
        self.door_open = door_open

    def start_cycle(self):
        if self.door_open:
            raise DoorOpenError("Door is open!")
        print("Washing Machine running")

try:
    wm = WashingMachine(True)
    wm.start_cycle()
except DoorOpenError as e:
    print(e)
