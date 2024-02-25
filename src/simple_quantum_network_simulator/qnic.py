from collections import deque
import simpy

from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.packet import Packet

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from simple_quantum_network_simulator.link import Link


class QNic:
    """A quantum network interface card (QNIC) that can be attached to a QNode.
    QNICs are connected to each other via Link.

    QNIC can connect to one QNIC on the other side of the Link.
    This class may have multiple addresses.
    QNICs can send and receive classical packets and manage network related Qubits."""

    env: simpy.Environment
    index: int
    addresses: list[QNodeAddress]
    queue_recv: deque[Packet]
    link: "Link"

    def __init__(
        self,
        env: simpy.Environment,
        index: int,
        addresses: QNodeAddress | list[QNodeAddress] = [],
    ) -> None:
        self.env = simpy.Environment()
        self.index = index
        self.addresses = addresses if isinstance(addresses, list) else [addresses]
        self.queue_recv = deque()

    def put_from_link(self, packet: Packet) -> None:
        self.queue_recv.append(packet)

    def send(self, packet: Packet) -> None:
        """send classical packet to the other QNIC through the Link."""
        assert (
            self.link is not None
        ), "QNic is not connected to any Link. The link must be set duraing the netwrok building phase"

        # set the previous hop to determine the direction of the packet in the link
        packet.prev_hop = self.addresses[0]
        self.link.send(packet)

    def __repr__(self) -> str:
        return f"QNic({self.addresses[0].short_repr}:{self.index})"
