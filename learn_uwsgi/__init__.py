# The first beta version
__version__ = '0.1.0'

from .default import DefaultResource
from .dev import create_dev_routes
from .prod import create_prod_routes