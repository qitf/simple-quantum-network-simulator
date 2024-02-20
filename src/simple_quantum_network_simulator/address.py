class QNodeAddress:

    host_part: int
    network_part: int

    def __init__(self, host_part: int, network_part: int = 0) -> None:
        self.host_part = host_part
        self.network_part = network_part

    def __repr__(self) -> str:
        return f"QAddr({self.network_part}.{self.host_part})"
