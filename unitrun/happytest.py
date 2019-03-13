import unittest
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


class Mytest(unittest.TestCase):
    def setUp(self):
        logging.info("start to test now")

    def test_a_run(self):
        self.assertEqual(1, 1)  # 测试用例
        logging.info("test case A ")

    def test_b_run(self):
        self.assertEqual(2, 2)  # 测试用例
        logging.info("test case B ")

    def test_c_run(self):
        self.assertEqual(5, 5)
        logging.info("test case c ")

    def tearDown(self):
       # print("I have completed")
        logging.info("Tear Down completed")


if __name__ == "__main__":
    unittest.main()




