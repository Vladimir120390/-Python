import unittest

# Определяем декоратор для пропуска тестов
def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper

# Класс Runner
class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


# Класс Tournament
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


# Тесты для Runner
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Установите True, чтобы заморозить тесты

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


# Тесты для Tournament
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Установите True, чтобы заморозить тесты

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


# Создание тестового набора
def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RunnerTest))
    suite.addTest(unittest.makeSuite(TournamentTest))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = create_test_suite()
    runner.run(test_suite)
