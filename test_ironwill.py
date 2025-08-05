# test_ironwill.py
"""
Tests for IronWill module.
"""

import unittest
from ironwill import IronWill

class TestIronWill(unittest.TestCase):
    """Test cases for IronWill class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IronWill()
        self.assertIsInstance(instance, IronWill)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IronWill()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
