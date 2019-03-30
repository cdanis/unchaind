import os

from typing import Dict, List


def load_systems() -> Dict[int, str]:
    systems: Dict[int, str] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "system.txt")
    ) as f:
        for line in f:
            typeID, name, _, _ = line.strip().split("|")
            systems[int(typeID)] = name

    return systems


def load_truesec() -> Dict[int, float]:
    truesec: Dict[int, float] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "system.txt")
    ) as f:
        for line in f:
            typeID, _, secStatus, _ = line.strip().split("|")
            truesec[int(typeID)] = float(secStatus)

    return truesec


def load_system_classes() -> Dict[int, int]:
    systemClasses: Dict[int, int] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "system.txt")
    ) as f:
        for line in f:
            typeID, _, _, systemClass = line.strip().split("|")
            if systemClass != '':
                systemClasses[int(typeID)] = int(systemClass)
            else:
                systemClasses[int(typeID)] = -1

    return systemClasses


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


def load_ships() -> Dict[int, Dict[str, str]]:
    ships: Dict[int, Dict[str, str]] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "ships.txt")
    ) as f:
        for line in f:
            typeID, shipName, shipClass = line.strip().split("|")
            ships[int(typeID)] = {"name": shipName, "class": shipClass}

    return ships


systems: Dict[int, str] = load_systems()
truesec: Dict[int, float] = load_truesec()
systemClasses: Dict[int, int] = load_system_classes()
connections: Dict[int, List[int]] = load_connections()
ships: Dict[int, Dict[str, str]] = load_ships()
