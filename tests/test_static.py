
import unittest

from unchaind import static as unchaind_static


class StaticTest(unittest.TestCase):
    def test__static_connections__count(self) -> None:
        self.assertEqual(len(unchaind_static.connections), 3917)

    def test__static_systems__count(self) -> None:
        self.assertEqual(len(unchaind_static.systems), 8285)

    def test__static_truesec__count(self) -> None:
        self.assertEqual(len(unchaind_static.truesec), 8285)

    def test__static_truesec__value(self) -> None:
        self.assertAlmostEqual(unchaind_static.truesec[30_002_187], 1.0)

    def test__static_ships__count(self) -> None:
        self.assertEqual(len(unchaind_static.ships), 497)

    def test__static_ships__can_convert_to_name(self) -> None:
        self.assertEqual(unchaind_static.ships[582]["name"], "Bantam")

    def test__static_ships__can_convert_to_class(self) -> None:
        self.assertEqual(unchaind_static.ships[582]["class"], "Frigate")
