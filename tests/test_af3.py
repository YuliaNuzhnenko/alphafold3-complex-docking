import unittest
import numpy as np
from scripts.evaluate_af3_complex import analyze_domain_pae

class TestAF3Evaluation(unittest.TestCase):
    def test_analyze_domain_pae(self):
        fake_pae = np.zeros((393, 393))
        fake_pae[92:292, 92:292] = 2.4
        metrics = analyze_domain_pae(fake_pae)
        self.assertEqual(metrics["seq_len"], 393)
        self.assertAlmostEqual(metrics["dbd_core_pae"], 2.4)

if __name__ == '__main__':
    unittest.main()
