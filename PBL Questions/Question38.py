class MotorJammedError(Exception):
    pass

class RollerBlind:
    def adjust_blinds(self):
        raise MotorJammedError()

try:
    rb = RollerBlind()
    rb.adjust_blinds()
except MotorJammedError:
    print("Power cut")
