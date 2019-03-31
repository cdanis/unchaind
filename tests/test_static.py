import unittest

from unchaind import static as unchaind_static


class StaticTest(unittest.TestCase):
    def test__static_connections__count(self) -> None:
        self.assertEqual(len(unchaind_static.connections), 3917)

    def test__static_systems__count(self) -> None:
        self.assertEqual(len(unchaind_static.systems), 8285)

    def test__static_systems__sec_status_value(self) -> None:
        self.assertAlmostEqual(unchaind_static.systems[30_002_187]["secStatus"], 1.0)

    def test__static_systems__class_value(self) -> None:
        self.assertAlmostEqual(unchaind_static.systems[31_002_479]["class"], 5) # J100820

    def test__static_ships__count(self) -> None:
        self.assertEqual(len(unchaind_static.ships), 497)

    def test__static_ships__can_convert_to_name(self) -> None:
        self.assertEqual(unchaind_static.ships[582]["name"], "Bantam")

    def test__static_ships__can_convert_to_class(self) -> None:
        self.assertEqual(unchaind_static.ships[582]["class"], "Frigate")
