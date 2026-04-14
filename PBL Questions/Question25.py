class DoNotDisturbError(Exception):
    pass

class CleaningService:
    def deliver(self, dnd):
        if dnd:
            raise DoNotDisturbError()
        print("Cleaning done")

try:
    cs = CleaningService()
    cs.deliver(True)
except DoNotDisturbError:
    print("Reschedule")
