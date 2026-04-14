class ConnectionTimeoutError(Exception):
    pass

class SQLDB:
    def connect(self, time):
        if time > 5000:
            raise ConnectionTimeoutError()
        print("Connected")

try:
    db = SQLDB()
    db.connect(6000)
except ConnectionTimeoutError:
    print("Retry backup")
