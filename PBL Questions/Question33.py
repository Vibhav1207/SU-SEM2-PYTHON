class FilterCloggedError(Exception):
    pass

class AC:
    def regulate_temp(self, temp):
        if temp > 24:
            raise FilterCloggedError()

try:
    ac = AC()
    ac.regulate_temp(30)
except FilterCloggedError:
    print("Maintenance required")
