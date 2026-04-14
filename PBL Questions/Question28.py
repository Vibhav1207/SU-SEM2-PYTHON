class DailyLimitExceededError(Exception):
    pass

class BasicWallet:
    def transfer(self, amt):
        if amt > 10000:
            raise DailyLimitExceededError()
        print("Transfer done")

try:
    bw = BasicWallet()
    bw.transfer(20000)
except DailyLimitExceededError:
    print("Limit exceeded")
