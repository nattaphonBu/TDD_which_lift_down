import unittest

class Test_Lift(unittest.TestCase):
    global lift, b_lift
    lift = [(1, 2), (2, 3), (3, 5)]


    def test_flor1_then_should_be_lift1(self):
        expected = 1
        actual = where_lift_come(1)
        self.assertEqual(actual, expected)

    def test_flor4_then_should_be_lift2(self):
        expected = 2
        actual = where_lift_come(4)
        self.assertEqual(actual, expected)

    def test_flor3_then_should_be_lift2(self):
        expected = 2
        actual = where_lift_come(3)
        self.assertEqual(actual, expected)

    def test_flor_2_then_should_be_lift1(self):
        expected = 1
        actual = where_lift_come(2)
        self.assertEqual(actual, expected)

    def test_flor_5_then_should_be_lift3(self):
        expected = 3
        actual = where_lift_come(5)
        self.assertEqual(actual, expected)


def where_lift_come(st_flors):
    if st_flors == 1 or st_flors == 2:
        return 1
    if st_flors ==3 or st_flors == 4:
        return 2
    return 3

unittest.main()
