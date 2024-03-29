import unittest

# define evaluater [(1, 2), (2, 3), (3, 5)]
class which_elevaluater(unittest.TestCase):
    def test_flor_1_Press_up_lift_1(self):
        expected = 'evaluater1'
        actual = which_evaluater_down(1, 'up')
        self.assertEqual(actual, expected)

    def test_flor_2_Press_up_lift_1(self):
        expected = 'evaluater1'
        actual = which_evaluater_down(2, 'up')
        self.assertEqual(actual, expected)

    def test_flor_2_Press_down_lift_1(self):
        expected = 'evaluater1'
        actual = which_evaluater_down(2, 'down')
        self.assertEqual(actual, expected)

    def test_flor_3_Press_up_lift_2(self):
        expected = 'evaluater2'
        actual = which_evaluater_down(3, 'up')
        self.assertEqual(actual, expected)

    def test_flor_3_Press_down_lift_2(self):
        expected = 'evaluater2'
        actual = which_evaluater_down(3, 'down')
        self.assertEqual(actual, expected)

    def test_flor_4_Press_up_lift_3(self):
        expected = 'evaluater2'
        actual = which_evaluater_down(4, 'up')
        self.assertEqual(actual, expected)

    def test_flor_4_Press_down_lift3(self):
        expected = 'evaluater3'
        actual = which_evaluater_down(4, 'down')
        self.assertEqual(actual, expected)

    def test_flor_5_Press_down_lift_3(self):
        expected = 'evaluater3'
        actual = which_evaluater_down(5,'down')
        self.assertEqual(actual, expected)


def which_evaluater_down(flor, direction):
        if flor == 1 and direction == 'up' or flor == 2 and direction == 'up' or flor == 2 and direction == 'down':
            return 'evaluater1'
        if flor == 3 and direction == 'up' or flor == 3 and direction == 'down' or flor == 4 and direction == 'up':
            return 'evaluater2'
        if flor == 4 and direction == 'down' or flor == 5 and direction == 'down':
            return 'evaluater3'


unittest.main()
