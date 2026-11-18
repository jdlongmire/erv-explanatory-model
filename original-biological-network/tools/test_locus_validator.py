"""Synthetic fixtures only; no biological findings asserted."""
import tempfile
import unittest
from pathlib import Path
from locus_validator import assess

L = "ACGTACGTACGT"
R = "TGCATGCATGCA"

class TestLocus(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def check(self, between, status="positive", insertion="GGCC"):
        (self.root / "test.fa").write_text(">synthetic\n" + L + between + R + "\n")
        case = dict(id="synthetic", species="synthetic", status=status,
                    fasta="test.fa", left_flank=L, right_flank=R, insertion=insertion)
        return assess(case, self.root)["status"]

    def test_positive(self):
        self.assertEqual(self.check("GGCC"), "sequence_consistent_positive")

    def test_empty_site(self):
        self.assertEqual(self.check("", status="empty_site"), "sequence_consistent_empty_site")

    def test_mismatch_unresolved(self):
        self.assertEqual(self.check("GGCA"), "unresolved")

    def test_nonempty_not_empty(self):
        self.assertEqual(self.check("GGCC", status="empty_site"), "unresolved")

    def test_duplicate_flanks_unresolved(self):
        (self.root / "test.fa").write_text(">synthetic\n" + L + "GGCC" + R + L + "GGCC" + R + "\n")
        case = dict(id="synthetic", species="synthetic", status="positive",
                    fasta="test.fa", left_flank=L, right_flank=R, insertion="GGCC")
        self.assertEqual(assess(case, self.root)["status"], "unresolved")

    def test_missing_fasta_unresolved(self):
        case = dict(id="synthetic", species="synthetic", status="positive",
                    fasta="missing.fa", left_flank=L, right_flank=R, insertion="GGCC")
        self.assertEqual(assess(case, self.root)["status"], "unresolved")

if __name__ == "__main__":
    unittest.main()
