import unittest
from utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi_valid(self):
        """Test BMI calculation with valid inputs."""
        height = 1.75  
        weight = 70  
        expected_bmi = 22.86
        result = calculate_bmi(height, weight)
        self.assertAlmostEqual(result, expected_bmi, places=2)

    def test_calculate_bmi_zero_height(self):
        """Test BMI calculation with zero height (should raise an error)."""
        height = 0  
        weight = 70  
        with self.assertRaises(ValueError):
            calculate_bmi(height, weight)

    def test_calculate_bmi_negative_weight(self):
        """Test BMI calculation with negative weight (should raise an error)."""
        height = 1.75  
        weight = -70  
        with self.assertRaises(ValueError):
            calculate_bmi(height, weight)

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmr_valid_male(self):
        """Test BMR calculation for males with valid inputs."""
        height = 175
        weight = 70
        age = 25
        gender = 'male'
        expected_bmr = 1724.05
        result = calculate_bmr(height, weight, age, gender)
        self.assertAlmostEqual(result, expected_bmr, places=2)

    def test_calculate_bmr_valid_female(self):
        """Test BMR calculation for females with valid inputs."""
        height = 160
        weight = 60
        age = 30
        gender = 'female'
        expected_bmr = 1368.19
        result = calculate_bmr(height, weight, age, gender)
        self.assertAlmostEqual(result, expected_bmr, places=2)

    def test_calculate_bmr_negative_values(self):
        """Test BMR calculation with negative height, weight, or age (should raise an error)."""
        height = -175  
        weight = 70  
        age = 25  
        gender = 'male'
        with self.assertRaises(ValueError):
            calculate_bmr(height, weight, age, gender)

if __name__ == '__main__':
    unittest.main()
