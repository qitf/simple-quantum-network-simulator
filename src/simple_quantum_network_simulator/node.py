from simple_quantum_network_simulator.address import QNodeAddress


class QNode:

    address: QNodeAddress

    def __init__(self, address: QNodeAddress) -> None:
        self.address = address

    def send(self, message: str) -> None:
        pass

    def __repr__(self) -> str:
        return f"QNode({self.address})"


if __name__ == "__main__":
    address = QNodeAddress(1)
    qnode = QNode(address)
    print(qnode)
    qnode.send("Hello, world!")
