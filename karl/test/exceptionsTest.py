import unittest
from karl.karl.exceptions import KarlBaseException, RPCError

class TestExceptions(unittest.TestCase):
    
    def test_KarlBaseException(self):
        with self.assertRaises(KarlBaseException):
            raise KarlBaseException

    def test_RPCError(self):
        with self.assertRaises(RPCError):
            raise RPCError

if __name__ == '__main__':
    unittest.main()