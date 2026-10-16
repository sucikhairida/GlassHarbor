# test_glassharbor.py
"""
Tests for GlassHarbor module.
"""

import unittest
from glassharbor import GlassHarbor

class TestGlassHarbor(unittest.TestCase):
    """Test cases for GlassHarbor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlassHarbor()
        self.assertIsInstance(instance, GlassHarbor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlassHarbor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
