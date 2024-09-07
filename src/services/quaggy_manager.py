import random

from loguru import logger


class QuaggyWatcher:
    def __init__(self, quaggy_id: int):
        self.quaggy_id = quaggy_id
        self.food = "apple"

    def check_status(self):
        random_value = random.random()
        logger.debug(f"value: {random_value}")

        if random_value < 0.25:
            return "sleeping"
        elif random_value < 0.5:
            return "eating"
        elif random_value < 0.75:
            return "playing"
        else:
            return "walking"

    def feed(self, food):
        if food == "fish":
            self.food = food

        return

    def get_food(self):
        return self.food


def check_quaggy_status(quaggy_id):
    watcher = QuaggyWatcher(quaggy_id)
    behavior = watcher.check_status()
    return f"Quaggy(ID: {quaggy_id}) is {behavior} now."
