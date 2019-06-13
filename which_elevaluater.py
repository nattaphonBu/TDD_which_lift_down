import unittest

class which_elevaluater(unittest.TestCase):

    def test_flor_1_Press_up_lift_1(self):
        expected = 1
        actual = which_evaluater_down(1, 'up')
        self.assertEqual(actual, expected)

def which_evaluater_down(flor, direction):
    pass

unittest.main()
