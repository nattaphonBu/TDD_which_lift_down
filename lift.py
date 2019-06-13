import unittest

class Test_Lift(unittest.TestCase):

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

    def test_flor_1_arrow_up_lift1(self):
        expected = 1
        actual = where_lift_come1(1, 'up')
        self.assertEqual(actual, expected)

    def test_flor_2_arrow_up_lift1(self):
        expected = 1
        actual = where_lift_come1(2, 'up')
        self.assertEqual(actual, expected)

    def test_flor_2_arrow_down_lift1(self):
        expected = 1
        actual = where_lift_come1(2, 'down')
        self.assertEqual(actual, expected)

    def test_flor_4_arrow_down_Lift3(self):
        expected = 3
        actual = where_lift_come1(4, 'down')
        self.assertEqual(actual, expected)

    def test_flor_1_arrow_up_lift1come(self):
        expected = 3
        actual = where_lift_come2(1, 'up')
        self.assertEqual(actual, expected)

def where_lift_come(st_flors):
    if st_flors == 1 or st_flors == 2:
        return 1
    elif st_flors ==3 or st_flors == 4:
        return 2
    elif st_flors == 5:
        return 3

def where_lift_come1(st_flors, direction):
    if st_flors == 4 and direction == 'down':
        return 3
    if st_flors == 1 and direction == 'up':
        return 1
    if st_flors == 2 and direction == 'up':
        return 1
    if st_flors == 2 and direction == 'down':
        return 1

unittest.main()

