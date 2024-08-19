class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2  # Увеличиваем дистанцию в два раза от скорости

    def walk(self):
        self.distance += self.speed  # Увеличиваем дистанцию на скорость

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2  # Увеличиваем дистанцию в два раза от скорости

    def walk(self):
        self.distance += self.speed  # Увеличиваем дистанцию на скорость

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f"{cls.all_results[key]}")

    def test_tournament_usain_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_tournament_andrey_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(results[max(results.keys())] == self.runner3)

    def test_tournament_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results[max(results.keys())] = {place: str(participant) for place, participant in results.items()}
        self.assertTrue(results[max(results.keys())] == self.runner3)

if __name__ == '__main__':
    unittest.main()
