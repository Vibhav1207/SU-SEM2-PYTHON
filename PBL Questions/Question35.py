class ItemStuckError(Exception):
    pass

class SnackMachine:
    def dispense_item(self):
        raise ItemStuckError()

try:
    sm = SnackMachine()
    sm.dispense_item()
except ItemStuckError:
    print("Refund issued")
