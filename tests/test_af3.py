import unittest
import os
from scripts.evaluate_af3_complex import fetch_alphafold_pae_matrix, analyze_domain_pae

class TestAF3Evaluation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Use local JSON fixture to avoid hitting the AlphaFold API during unit tests
        cls.fixture_path = os.path.join(
            os.path.dirname(__file__), "fixtures", "AF-P04637-F1-pae.json"
        )
        cls.pae_matrix = fetch_alphafold_pae_matrix(local_fixture=cls.fixture_path)

    def test_pae_matrix_dimensions(self):
        self.assertEqual(self.pae_matrix.shape, (393, 393))

    def test_analyze_domain_pae_numerical_accuracy(self):
        metrics = analyze_domain_pae(self.pae_matrix)
        
        # Exact numerical structural PAE evaluations (Angstroms)
        self.assertEqual(metrics["seq_len"], 393)
        self.assertAlmostEqual(metrics["min_pae"], 0.0, places=2)
        self.assertAlmostEqual(metrics["overall_mean_pae"], 20.59, places=2)
        
        # Structured DNA-Binding Domain (DBD) should have low PAE error
        self.assertAlmostEqual(metrics["dbd_core_pae"], 3.69, places=2)
        
        # Intrinsically Disordered Transactivation Domain (TAD) should have high PAE error
        self.assertAlmostEqual(metrics["tad_disordered_pae"], 22.43, places=2)

if __name__ == '__main__':
    unittest.main()
