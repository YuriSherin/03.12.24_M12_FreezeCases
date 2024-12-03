"""Задача "Заморозка кейсов":"""
import unittest
import tests

my_test_suite = unittest.TestSuite()    # создаем объект класса

# подключаем тесты
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest))
my_test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest))

# получаем подробную строку справки за каждый результат
runner = unittest.TextTestRunner(verbosity=2)

# запускаем тесты
runner.run(my_test_suite)