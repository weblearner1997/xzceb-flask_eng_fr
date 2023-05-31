import unittest
from machinetranslation.translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_French(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french(None))

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english(None))


if __name__ == '__main__':
    unittest.main()