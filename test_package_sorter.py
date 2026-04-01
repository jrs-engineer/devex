"""Unit tests for package_sorter.sort."""

import unittest

from package_sorter import sort


class SortTests(unittest.TestCase):
    def test_standard_package(self) -> None:
        self.assertEqual(sort(10, 20, 30, 5), "STANDARD")

    def test_heavy_only_package_is_special(self) -> None:
        self.assertEqual(sort(10, 20, 30, 20), "SPECIAL")

    def test_bulky_by_volume_only_is_special(self) -> None:
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_bulky_by_dimension_only_is_special(self) -> None:
        self.assertEqual(sort(150, 10, 10, 10), "SPECIAL")

    def test_both_heavy_and_bulky_are_rejected(self) -> None:
        self.assertEqual(sort(150, 100, 100, 20), "REJECTED")

    def test_exact_volume_threshold_counts_as_bulky(self) -> None:
        self.assertEqual(sort(100, 100, 100, 1), "SPECIAL")

    def test_exact_dimension_threshold_counts_as_bulky(self) -> None:
        self.assertEqual(sort(149.9, 150, 1, 1), "SPECIAL")

    def test_exact_mass_threshold_counts_as_heavy(self) -> None:
        self.assertEqual(sort(1, 1, 1, 20), "SPECIAL")

    def test_zero_values_are_allowed(self) -> None:
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")

    def test_negative_values_raise_value_error(self) -> None:
        with self.assertRaises(ValueError):
            sort(-1, 10, 10, 10)


if __name__ == "__main__":
    unittest.main()
