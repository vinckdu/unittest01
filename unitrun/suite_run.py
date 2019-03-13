import unittest
case_path = r'.'


def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(get_allcase())






