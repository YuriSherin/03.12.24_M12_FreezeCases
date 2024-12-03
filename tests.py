import unittest
import runners

is_frozen = False

class RunnerTest(unittest.TestCase):
    """Дочерний класс, наследуемый от класса unittest.TestCase"""

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        """Метод тестирует метод объекта 'run'"""
        runner_run = runners.Runner('Runner_2')  # создаем экземпляр класса
        for i in range(10):  # в цикле от 0 до 9
            runner_run.run()  # вызываем метод 'run' объекта
        self.assertEqual(runner_run.distance, 100)  # сравниваем значение атрибута объекта
        # с контрольным значением

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        """Метод тестирует атрибуты двух объектов класса на неравенство"""
        test_runner_1 = runners.Runner('Runner_1')  # создаем первый объект класса
        test_runner_2 = runners.Runner('Runner_2')  # создаем второй объект класса
        for i in range(10):  # в цикле от 0 до 9
            test_runner_1.run()  # вызываем метод 'run' для первого объекта
            test_runner_2.walk()  # вызываем метод 'walk' для второго объекта
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)  # сравниваем значение атрибута объектов
                                                                            # с контрольным значением на неравенство


is_frozen = True

class TournamentTest(unittest.TestCase):
    """Дочерний тестовый класс, наследуемый от unittest.TestCase"""

    @classmethod
    def setUpClass(cls):
        """Метод класса вызывается один раз перед началом всех тестов.
        Данный метод создает атрибут класса словарь, в который будут сохраняться результаты всех тестов"""
        cls.all_results = {}  # словарь в который будут сохраняться результаты всех тестов.

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        vs = {'Усэйн': 10, 'Андрей': 9, 'Ник': 3}
        self.runners = {n: runners.Runner(name=n, speed=v) for n, v in vs.items()}

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(f'{k}: {v}')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tour = runners.Tournament(90, self.runners['Усэйн'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tour = runners.Tournament(90, self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[2], self.runners['Ник'])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tour = runners.Tournament(90, self.runners['Усэйн'], self.runners['Андрей'], self.runners['Ник'])
        all_results = tour.start()
        self.assertTrue(all_results[3], self.runners['Ник'])
