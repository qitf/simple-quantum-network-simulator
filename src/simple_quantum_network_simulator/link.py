from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simple_quantum_network_simulator.qnic import QNic

import simpy
from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.packet import Packet


class Link:
    """A link between two QNodes.
    This class has both quantum and classical features."""

    env: simpy.Environment
    addr_left: list[QNodeAddress]
    addr_right: list[QNodeAddress]
    qnic_left: "QNic"
    qnic_right: "QNic"
    classical_distance: float

    def __init__(
        self,
        env: simpy.Environment,
        qnic_left: "QNic",
        qnic_right: "QNic",
        classical_distance: float,
    ) -> None:

        self.env = env
        self.qnic_left = qnic_left
        self.qnic_right = qnic_right
        self.addr_left = qnic_left.addresses
        self.addr_right = qnic_right.addresses
        self.classical_distance = classical_distance

    def send(self, packet: Packet) -> None:

        # If the packet is from the left, send it to the right
        dest_qnic = (
            self.qnic_right if self.is_packet_from_left(packet) else self.qnic_left
        )

        def __transfer(env: simpy.Environment, dest_qnic: "QNic", packet: Packet):
            # delay the classical transfer
            yield env.timeout(self.classical_distance)
            dest_qnic.put_from_link(packet)

        self.env.process(__transfer(self.env, dest_qnic, packet))

    def is_packet_from_left(self, packet: Packet) -> bool:
        assert packet.prev_hop is not None
        return packet.prev_hop in self.addr_left

    def __repr__(self) -> str:
        return (
            f"Link({self.addr_left[0].short_repr} <-> {self.addr_right[0].short_repr})"
        )
