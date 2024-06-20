from struct import pack
from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.packet import Packet
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

    def send(self, message: str, to: QNodeAddress) -> Packet:
        data = {
            'message': message,
            'to': to
        }
        return Packet(data=data, prev_hop=self.address)

    def receive(self, packet: Packet) -> None:
        if 'to' in packet.data.keys():  # dataの型が任意だから.keys()でいいのか？
            if packet.data['to'] == self.address:
                message = packet.data['message']
                print(f'from: {packet.prev_hop}, message: {message}')
            else:
                print(f'Invalid address: {packet.data["to"]}')
        else:
            message = packet.data['message']
            print(f'from: {packet.prev_hop}, message: {message}')



    def __repr__(self) -> str:
        return f"QNode({self.address.short_repr})"


if __name__ == "__main__":
    env = simpy.Environment()
    qnode1 = QNode(env, QNodeAddress(1))
    message = qnode1.send("Hello, world!", QNodeAddress(2))
    """
    receiveの方にpacketがいるが、sendの時点でpacketができて
    指定したアドレスのqnodeに向かってnetworkが運んでいくイメージ
    ただ、それを今書くのはすごく長くなりそうな気がするので
    """

    qnode2 = QNode(env, QNodeAddress(2))
    qnode2.receive(message)
