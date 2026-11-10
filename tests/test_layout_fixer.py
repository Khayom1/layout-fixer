import unittest

from layout_fixer import convert, detect_direction, RU_TO_EN, TJ_TO_EN, EN_TO_TJ

class LayoutFixerTests(unittest.TestCase):
    def test_russian_round_trip(self):
        sample = "Привет мир! Ёж"
        self.assertEqual(convert(convert(sample, "1"), "2"), sample)

    def test_tajik_round_trip(self):
        sample = "Салом ҷаҳон! ҒӮҲҶҚӢ"
        self.assertEqual(convert(convert(sample, "3"), "4"), sample)

    def test_unmapped_characters_are_preserved(self):
        self.assertEqual(convert("123 🙂", "1"), "123 🙂")

    def test_invalid_direction_raises(self):
        with self.assertRaises(ValueError):
            convert("hello", "9")

    def test_auto_detects_tajik(self):
        self.assertEqual(detect_direction("салом ҷаҳон"), "3")

    def test_auto_detects_russian(self):
        self.assertEqual(detect_direction("привет мир"), "1")

    def test_auto_does_not_guess_latin_target(self):
        self.assertIsNone(detect_direction("hello world"))

    def test_tajik_mapping_is_reversible(self):
        self.assertEqual(convert("ғӣқӯҳҷ", "3"), "~g~i~q~u~h~j")
        self.assertEqual(convert("~g~i~q~u~h~j", "4"), "ғӣқӯҳҷ")

if __name__ == "__main__":
    unittest.main()
