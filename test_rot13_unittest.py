import unittest
from parameterized import parameterized # pip install parameterized

import rot13_pkg

class Rot13Test(unittest.TestCase):
    @parameterized.expand([
        ("test", "grfg"), # lowercase
        ("grfg", "test"), # reverse applies
        ("Test", "Grfg"), # mixed-case1
        ("KELVIN@254","XRYIVA@254"), # mixed-case2
        ("Gb trg gb gur bgure fvqr!", "To get to the other side!"),
        ("^&*#2023/","^&*#2023/"), # non-latin/english alphabets remains the same
        ("","") # empty string returns empty
    ])
    def test_rot13(self, string_input, string_output):
        self.assertEqual(rot13_pkg.rot13_fn(string_input), string_output)

if __name__ == "__main__":
    unittest.main()

