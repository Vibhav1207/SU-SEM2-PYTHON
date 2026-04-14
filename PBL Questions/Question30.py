class IntruderAlertError(Exception):
    pass

class PinLock:
    def __init__(self):
        self.attempts = 0

    def unlock(self, pin):
        if pin != "1234":
            self.attempts += 1
            if self.attempts >= 3:
                raise IntruderAlertError()
        else:
            print("Unlocked")

try:
    pl = PinLock()
    pl.unlock("0000")
    pl.unlock("1111")
    pl.unlock("2222")
except IntruderAlertError:
    print("Alarm!")
