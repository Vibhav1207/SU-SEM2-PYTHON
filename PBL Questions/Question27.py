class PayloadTooHeavyError(Exception):
    pass

class Quadcopter:
    def takeoff(self, weight):
        if weight > 2:
            raise PayloadTooHeavyError()
        print("Flying")

try:
    q = Quadcopter()
    q.takeoff(5)
except PayloadTooHeavyError:
    print("Too heavy")
