"""Root package info."""

import logging
import sys

# explicitly don't set root logger's propagation and leave this to subpackages to manage
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)

_console = logging.StreamHandler()
_console.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s: %(message)s")
_console.setFormatter(formatter)
_logger.addHandler(_console)

from engine.__about__ import *  # noqa: E402, F403
# from engine.__version__ import version as __version__  # noqa: E402
# from engine.fabric.fabric import Fabric  # noqa: E402
from engine.fabric.utilities.seed import seed_everything  # noqa: E402

