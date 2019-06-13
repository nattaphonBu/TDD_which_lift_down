import unittest

class which_elevaluater(unittest.TestCase):

    def test_flor_1_Press_up_lift_1(self):
        expected = 'eveluater1'
        actual = which_evaluater_down(1, 'up')
        self.assertEqual(actual, expected)

    def test_flor_2_Press_up_lift_1(self):
        expected = 'eveluater1'
        actual = which_evaluater_down(2, 'up')
        self.assertEqual(actual, expected)

def which_evaluater_down(flor, direction):
        if flor == 1 and direction == 'up' or flor == 2 and direction == 'up':
            return 'eveluater1'

unittest.main()
