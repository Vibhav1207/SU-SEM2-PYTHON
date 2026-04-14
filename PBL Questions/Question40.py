class WaterPressureLowError(Exception):
    pass

class RotarySprinkler:
    def water_crops(self, pressure):
        if pressure < 20:
            raise WaterPressureLowError()

try:
    r = RotarySprinkler()
    r.water_crops(10)
except WaterPressureLowError:
    print("System shutdown")
