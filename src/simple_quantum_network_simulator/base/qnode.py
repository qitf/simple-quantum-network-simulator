from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.qnic import QNic
import simpy


class QNode:

    address: QNodeAddress
    qnics: list[QNic]
    env: simpy.Environment

    def __init__(
        self, env: simpy.Environment, address: QNodeAddress, qnics: list[QNic] = []
    ) -> None:
        self.env = env
        self.address = address

    def send(self, message: str) -> None:
        pass

    def __repr__(self) -> str:
        return f"QNode({self.address.short_repr})"


if __name__ == "__main__":
    env = simpy.Environment()
    qnode1 = QNode(env, QNodeAddress(1))
    qnode1.send("Hello, world!")

    qnode2 = QNode(env, QNodeAddress(2))
    packet = qnode2.receive()
