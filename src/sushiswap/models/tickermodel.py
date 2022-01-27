

class TickerModel:
    def __init__(self, name: str, address: str, chain_id: int):
        self.name: str = name
        self.address: str = address
        self.chain_id: int = chain_id

    def __str__(self):
        return self.name
