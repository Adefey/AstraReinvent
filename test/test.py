import sys
import unittest

sys.path.append("src")
from astra import Astra


class TestAstra(unittest.TestCase):
    def test_k_0(self):
        model = Astra(fuel=["N2H8C2"], oxidizer=["N2O4"])
        k_0 = model.k_0()
        k_0_true = 3.06
        self.assertTrue(k_0 - k_0_true < 0.01)


if __name__ == "__main__":
    unittest.main()
