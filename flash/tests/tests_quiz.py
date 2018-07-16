import unittest
from flash.quiz import Answered
from flash.load import Question

class TestGetWeights(unittest.TestCase):
    def test_weights_empty(self):
        questions = [
            Question("who", "correct"),
            Question("what", "correct"),
        ]

        answered = Answered()
        weights = answered.get_weights(questions)
        assert weights == [1, 1]