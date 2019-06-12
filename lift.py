import unittest

class Test_Lift(unittest.TestCase):
    global lift
    lift = [(1, 2), (2, 3), (3, 5)]


    def test_press_2_then_should_be_Lift1(self):
        expected = 1
        actual = where_lift_come(2)
        self.assertEqual(actual, expected)


def where_lift_come(self):
    pass


unittest.main()
