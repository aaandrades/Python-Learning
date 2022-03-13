import unittest
import functions


class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = "python"
        result = functions.capitalizeNames(text)
        self.assertEqual(result, "Python")

    def test_multiple_words(self):
        text = "monty python"
        result = functions.capitalizeNames(text)
        self.assertEqual(result, "Monty Python")


if __name__ == "__main__":
    # To run the test, just call the python file
    unittest.main()
