class PathBlockedError(Exception):
    pass

class Enemy:
    def move(self, blocked):
        if blocked:
            raise PathBlockedError()

try:
    e = Enemy()
    e.move(True)
except PathBlockedError:
    print("Wait one turn")
