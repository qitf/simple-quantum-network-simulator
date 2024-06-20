from simpy import Environment
from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.qnic import QNic
from .qrepeater import BaseQuantumRepeater


class BaseQuantumRouter(BaseQuantumRepeater):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)


class QuantumRouter(BaseQuantumRouter):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)
