import os

from typing import Dict, List, Union


def load_systems() -> Dict[int, Dict[str, Union[str,float,int]]]:
    systems: Dict[int, Dict[str, Union[str,float,int]]] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "system.txt")
    ) as f:
        for line in f:
            typeID, systemName, systemSecStatus, systemClass = line.strip().split("|")

            if systemClass == '':
                systemClass = '-1'

            systems[int(typeID)] = {
                "name": systemName,
                "secStatus": float(systemSecStatus),
                "class": int(systemClass)
            }

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


def load_ships() -> Dict[int, Dict[str, str]]:
    ships: Dict[int, Dict[str, str]] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "ships.txt")
    ) as f:
        for line in f:
            typeID, shipName, shipClass = line.strip().split("|")

            ships[int(typeID)] = {
                "name": shipName,
                "class": shipClass,
            }

    return ships


systems: Dict[int, str] = load_systems()
connections: Dict[int, List[int]] = load_connections()
ships: Dict[int, Dict[str, str]] = load_ships()
