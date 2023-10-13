import unittest
from karl.karl import Karl

class KarlTest(unittest.TestCase):
    
    def setUp(self):
        self.karl = Karl(rpc='localhost:8545', output=None)

    def test_init(self):
        self.assertEqual(self.karl.rpc, 'localhost:8545')
        self.assertEqual(self.karl.output, None)
        self.assertEqual(self.karl.sandbox, True)
        self.assertEqual(self.karl.timeout, 600)
        self.assertEqual(self.karl.tx_count, 3)
        self.assertIsNotNone(self.karl.modules)
        self.assertEqual(self.karl.onchain_storage, True)
        self.assertEqual(self.karl.loop_bound, 3)

    def test_run_mythril(self):
        with self.assertRaises(Exception):
            self.karl._run_mythril()

    def test_run_sandbox(self):
        with self.assertRaises(Exception):
            self.karl._run_sandbox()

if __name__ == '__main__':
    unittest.main()