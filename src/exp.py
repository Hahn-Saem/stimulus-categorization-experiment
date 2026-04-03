import random
import datetime

class Exp:
    def __init__(self):
        self.create_random_seed()
        self.create_participant_id()
        # self.run_experiment()

    def create_random_seed(self):
        self.rng = random.Random(self.random_seed)
    
    def create_participant_id(self):
        formatted_datetime = self.experiment_start_time.strftime("%Y%m%d%H%M%S%f")
        random_number = self.rng.randint(100000, 999999)
        self.participant_id = f"{formatted_datetime}_{random_number}"

    