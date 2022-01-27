from web3 import Web3, providers
from web3.contract import Contract

from . import contracts

from src.models import ContractDataFile
from src.classes import W3Contract


class Harmony:
    MAIN_NET_RPC = "https://rpc.s0.t.hmny.io"

    def __init__(self, *, rpc: str = MAIN_NET_RPC):
        self._w3 = Web3(providers.HTTPProvider(rpc))

    def get_wrapped_contract(self, data: ContractDataFile) -> W3Contract:
        """
        Fetch a harmony contract using a (hex) address and abi
        :param data: Data file model
        :return:
            Return the Contract object as a wrapped W3Contract
        """
        return W3Contract(self.get_contract(data))

    def get_contract(self, data: ContractDataFile) -> Contract:
        """
        Fetch a harmony contract using a data file model
        :param data: Data file model
        :return:
            Return the Contract object
        """
        return self._create_contract(data.address, data.abi)

    def _create_contract(self, hex_addr: str, abi: list = None) -> Contract:
        """
        Create a new contract object using the provided address and ABI
        :param hex_addr: Contract hex address
        :param abi (optional): ABI for the contract, used to call functions from the contract
        :return:
            Return the contract object
        """
        if abi:
            return self._w3.eth.contract(address=hex_addr, abi=abi)  # type: ignore
        else:
            return self._w3.eth.contract(address=hex_addr)  # type: ignore
