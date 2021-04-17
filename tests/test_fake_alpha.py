import unittest
import time


class TestFakeAlpha(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_success(self):
        time.sleep(1)
        self.assertEqual(1, 0)

    def test_subset_success(self):
        for i in range(0, 3):
            time.sleep(1)
            with self.subTest(i=i):
                self.assertEqual(1, 1)

    def test_subset_success_and_skip_1(self):
        for i in range(0, 6):
            time.sleep(1)
            if i == 2:
                self.skipTest("Personal Reason")
            with self.subTest(i=i):
                self.assertEqual(1, 1)

    def test_subset_success_and_skip_2(self):
        for i in range(0, 4):
            time.sleep(1)
            with self.subTest(i=i):
                if i == 2:
                    self.skipTest("For Personal Reason")
                self.assertEqual(1, 1)

    def test_subset_error_1(self):
        for i in range(0, 4):
            time.sleep(1)
            if i == 2:
                raise Exception("Exception Provoquée")
            with self.subTest(i=i):
                self.assertEqual(1, 1)

    def test_subset_error_2(self):
        for i in range(0, 4):
            time.sleep(1)
            with self.subTest(i=i):
                if i == 2:
                    raise Exception("Exception Provoquée")
                self.assertEqual(1, 1)

    def test_subset_failure(self):
        for i in range(0, 4):
            time.sleep(1)
            with self.subTest(i=i):
                if i == 2:
                    self.assertEqual(1, 0)
                else:
                    self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
