from simple_quantum_network_simulator.address import QNodeAddress


def test_addr_eq():
    addr1 = QNodeAddress(1, 2)
    addr2 = QNodeAddress(1, 2)
    assert addr1 == addr2


def test_addr_ne_host_parts():
    addr1 = QNodeAddress(1, 2)
    addr2 = QNodeAddress(1, 3)
    assert addr1 != addr2


def test_addr_ne_network_parts():
    addr1 = QNodeAddress(2, 1)
    addr2 = QNodeAddress(3, 1)
    assert addr1 != addr2


def test_addr_short_repr():
    addr = QNodeAddress(1, 2)
    assert addr.short_repr == "2.1"
