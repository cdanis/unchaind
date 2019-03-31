import os

from typing import Dict, List

import dataclasses


@dataclasses.dataclass
class System:
    name: str
    security_status: float
    klass: int


@dataclasses.dataclass
class Ship:
    name: str
    klass: str


def load_systems() -> Dict[int, System]:
    systems: Dict[int, System] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "system.txt")
    ) as f:
        for line in f:
            type_id, system_name, system_security_status, system_class = line.strip().split(
                "|"
            )

            if not system_class:
                system_class = "-1"

            systems[int(type_id)] = System(
                system_name, float(system_security_status), int(system_class)
            )

    return systems


def load_connections() -> Dict[int, List[int]]:
    seen: List[frozenset] = []
    connections: Dict[int, List[int]] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "connection.txt")
    ) as f:
        for line in f:
            a, b = line.strip().split("|")

            if frozenset((a, b)) in seen:
                continue

            connections[int(a)] = connections.get(int(a), []) + [int(b)]

            seen.append(frozenset((a, b)))

    return connections


def load_ships() -> Dict[int, Ship]:
    ships: Dict[int, Ship] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "ships.txt")
    ) as f:
        for line in f:
            type_id, ship_name, ship_class = line.strip().split("|")

            ships[int(type_id)] = Ship(ship_name, ship_class)

    return ships


systems = load_systems()
connections = load_connections()
ships = load_ships()
