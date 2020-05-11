import unittest

from project.tests.setup import TestSetup

class TestCase1(TestSetup):
    def test_template(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main(verbosity=2)