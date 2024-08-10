class QuaggyManager:
    def __init__(self):
        self.food = "apple"

    def get_food(self):
        return self.food

def check_quaggy():
    qm = QuaggyManager()
    food = qm.get_food()
    return f"Quaggy is eating {food}."