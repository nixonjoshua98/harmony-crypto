from web3.contract import Contract, ContractFunctions


class W3Contract:
    """ Wrapped contract object with helper functiions """

    def __init__(self, contract: Contract):
        self.contract = contract

    @property
    def functions(self) -> ContractFunctions: return self.contract.functions

    def total_supply(self):
        supply = self.contract.functions.totalSupply().call()

        return round(supply * 10 ** -18, 3)
