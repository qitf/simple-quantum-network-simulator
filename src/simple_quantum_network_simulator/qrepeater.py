from simpy import Environment
from simple_quantum_network_simulator.address import QNodeAddress
from simple_quantum_network_simulator.qnic import QNic
from .base.qnode import QNode


class BaseQuantumRepeater(QNode):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)


class QuantumRepeaterGen1(BaseQuantumRepeater):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)


class QuantumRepeaterGen2(BaseQuantumRepeater):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)


class QuantumRepeaterGen3(BaseQuantumRepeater):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)

class RpeaterGraphStateSource(BaseQuantumRepeater):
    def __init__(self, env: Environment, address: QNodeAddress, qnics: list[QNic] = ...) -> None:
        super().__init__(env, address, qnics)
