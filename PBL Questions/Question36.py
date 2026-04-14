class VaccinationOverdueError(Exception):
    pass

class Dog:
    def schedule_appointment(self, years):
        if years > 2:
            raise VaccinationOverdueError()

try:
    d = Dog()
    d.schedule_appointment(3)
except VaccinationOverdueError:
    print("High priority")
