from collections import deque
from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.link import Link
from simple_quantum_network_simulator.packet import Packet
from simple_quantum_network_simulator.qnic import QNic
import simpy


def test_packet_transfer():
    env = simpy.Environment()
    addr1 = QNodeAddress(1, 2)
    addr2 = QNodeAddress(2, 1)
    qnic1 = QNic(env, 1, addr1)
    qnic2 = QNic(env, 2, addr2)
    link = Link(env, qnic1, qnic2, classical_distance=1.0)
    assert len(qnic1.queue_recv) == 0, "qnic1 should have an empty queue"
    assert len(qnic2.queue_recv) == 0, "qnic2 should have an empty queue"

    # send packet through the link, and simulate until 0.1 sec.
    # this simulation should not transfer the packet to the other qnic
    pkt = Packet("Hello, world!", prev_hop=addr1)
    link.send(pkt)
    env.run(until=0.1)
    assert len(qnic1.queue_recv) == 0, "qnic1 should still have an empty queue"
    assert len(qnic2.queue_recv) == 0, "qnic2 should still have an empty queue"

    # simulate until 1.1 sec. This should transfer the packet to the other qnic
    env.run(until=1.1)
    assert len(qnic1.queue_recv) == 0, "qnic1 should still have an empty queue"
    assert qnic2.queue_recv == deque([pkt]), "qnic2 should have the packet"
