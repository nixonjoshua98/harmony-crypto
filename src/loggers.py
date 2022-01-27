import logging.config

from src import utils as _utils

logging.config.dictConfig(_utils.load_json("logging.json"))

logger = logging.getLogger("CLNY.Logger")
