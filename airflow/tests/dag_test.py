import unittest
from airflow.models import DagBag

class TestDagIntegrity(unittest.TestCase):


    def setUp(self):
        self.dagbag = DagBag(dag_folder="/src/dags", include_examples=False)

    def test_number_of_dags(self):
        self.assertIn('generate', self.dagbag.dags)
        self.assertIn('predict', self.dagbag.dags)
        self.assertIn('train', self.dagbag.dags)

    def test_number_of_tasks(self):
        self.assertEqual(len(self.dagbag.dags["generate"].tasks), 1)
        self.assertEqual(len(self.dagbag.dags["predict"].tasks), 4)
        self.assertEqual(len(self.dagbag.dags["train"].tasks), 5)


if __name__ == "__main__":
    unittest.main()