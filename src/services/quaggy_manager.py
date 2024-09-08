import random
import datetime
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

    def get_schedule(self, target_time: datetime.datetime):

        random_value = random.random()
        logger.debug(f"value: {random_value}")

        if random_value < 0.25:
            return "sleep"
        elif random_value < 0.5:
            return "eat"
        elif random_value < 0.75:
            return "play"
        else:
            return "free"

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


def get_quaggy_schedule(quaggy_id: int, target_time: datetime.datetime):

    now_time = datetime.datetime.now()

    watcher = QuaggyWatcher(quaggy_id)
    behavior = watcher.get_schedule(target_time)

    if behavior == "free":
        behavior = "free" if target_time < now_time else "undesided"

    return behavior
