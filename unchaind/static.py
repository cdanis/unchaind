import os

from typing import Dict, List


def load_systems() -> Dict[int, str]:
    systems: Dict[int, str] = {}

    with open(
        os.path.join(os.path.dirname(__file__), "data", "system.txt")
    ) as f:
        for line in f:
            a, b = line.strip().split("|")

            systems[int(a)] = b

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


systems: Dict[int, str] = load_systems()
connections: Dict[int, List[int]] = load_connections()
