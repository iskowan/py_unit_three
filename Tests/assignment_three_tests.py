import unittest
import assignment_three

import sys
from io import StringIO

saved_stdout = sys.stdout
try:
    out = StringIO()
    sys.stdout = out
    addition.add_two(2, 4)
    output = out.getvalue().strip()
    assert output == "The sum of 2 and 4 is 6"
finally:
    sys.stdout = saved_stdout


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
