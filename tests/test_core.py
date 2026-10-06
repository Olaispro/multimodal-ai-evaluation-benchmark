import unittest
from src.benchmark import summarize
class TestBenchmark(unittest.TestCase):
 def test_macro_score(self):
  r=summarize([{"task_id":"a","modality":"image","outcome":1},{"task_id":"b","modality":"audio","outcome":0}]); self.assertEqual(r["macro_success_rate"],.5); self.assertEqual(r["invalid_rows"],[])
