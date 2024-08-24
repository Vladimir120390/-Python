import unittest


def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
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



class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Usain", 10)
        runner.run()
        self.assertEqual(runner.distance, 20)

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Usain", 10)
        runner.walk()
        self.assertEqual(runner.distance, 10)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Usain", 10)
        runner2 = Runner("Andrey", 9)
        self.assertTrue(runner1 != runner2)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        runner1 = Runner("Usain", 10)
        runner2 = Runner("Nick", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(results[1].name, "Usain")

    @skip_if_frozen
    def test_second_tournament(self):
        runner1 = Runner("Andrey", 9)
        runner2 = Runner("Nick", 3)
        tournament = Tournament(90, runner1, runner2)
        results = tournament.start()
        self.assertEqual(results[1].name, "Andrey")

    @skip_if_frozen
    def test_third_tournament(self):
        runner1 = Runner("Usain", 10)
        runner2 = Runner("Andrey", 9)
        runner3 = Runner("Nick", 3)
        tournament = Tournament(90, runner1, runner2, runner3)
        results = tournament.start()
        self.assertEqual(results[1].name, "Andrey")


if __name__ == '__main__':
    unittest.main()
