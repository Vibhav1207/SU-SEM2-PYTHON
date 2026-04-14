class PaperJamError(Exception):
    pass

class LaserPrinter:
    def print_document(self, pages):
        if pages > 500:
            raise PaperJamError()
        print("Printing...")

try:
    lp = LaserPrinter()
    lp.print_document(600)
except PaperJamError:
    print("Paper jam!")
