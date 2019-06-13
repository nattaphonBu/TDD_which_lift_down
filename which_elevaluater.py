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

    def test_flor_3_Press_up_lift_2(self):
        expected = 'eveluater2'
        actual = which_evaluater_down(3, 'up')
        self.assertEqual(actual, expected)

    def test_flor_4_Press_up_lift_3(self):
        expected = 'eveluater2'
        actual = which_evaluater_down(4, 'up')
        self.assertEqual(actual, expected)

    def test_flor_4_Press_down_lift3(self):
        expected = 'eveluater3'
        actual = which_evaluater_down(4, 'down')
    def test_flor_5_Press_down_lift_3(self):
        expected = 'eveluater3'
        actual = which_evaluater_down(5,'down')
        self.assertEqual(actual, expected)


def which_evaluater_down(flor, direction):
        if flor == 1 and direction == 'up' or flor == 2 and direction == 'up':
            return 'eveluater1'
        if flor == 3 and direction == 'up':
            return 'eveluater2'
        if flor == 4 and direction == 'up':
            return  'eveluater2'
        if flor == 4 and direction == 'down':
            return 'eveluater3'
        if flor == 5 and direction == 'down':
            return 'eveluater3'


unittest.main()
