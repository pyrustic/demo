import unittest
import time


class TestFakeBeta1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("dcd")
    def test_skip_1(self):
        time.sleep(2)
        self.assertEqual(1, 1)

    @unittest.skip("Skip because I can")
    def test_skip_2(self):
        time.sleep(2)
        self.assertEqual(1, 0)

    @unittest.skip("Skip because I can")
    def test_skip_3(self):
        time.sleep(2)
        raise Exception("Exception Trafiquée")
        self.assertEqual(1, 1)

    @unittest.expectedFailure
    def test_expected_failure(self):
        time.sleep(2)
        self.assertEqual(1, 0)

    @unittest.expectedFailure
    def test_unexpected_success(self):
        time.sleep(2)
        self.assertEqual(1, 1)




class TestFakeBeta2(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_error(self):
        time.sleep(1)
        raise Exception("Exception Trafiquée")
        self.assertEqual(1, 1)

    def test_failure(self):
        time.sleep(1)
        self.assertEqual(1, 0)


if __name__ == '__main__':
    unittest.main()
