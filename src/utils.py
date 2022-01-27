import pyjson5
import os

from src.models import ContractDataFile


def load_json(fp: str):
    with open(fp) as fh:
        return pyjson5.load(fh)


def load_contract_file(fname: str) -> ContractDataFile:
    fp = os.path.join(os.getcwd(), "contracts", fname)

    return ContractDataFile.parse_obj(load_json(fp))
