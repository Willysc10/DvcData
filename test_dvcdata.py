# test_dvcdata.py
"""
Tests for DvcData module.
"""

import unittest
from dvcdata import DvcData

class TestDvcData(unittest.TestCase):
    """Test cases for DvcData class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DvcData()
        self.assertIsInstance(instance, DvcData)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DvcData()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
