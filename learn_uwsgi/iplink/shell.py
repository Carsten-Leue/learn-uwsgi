from logging import Logger
from typing import Optional, Sequence
from ..models import DeviceAttributes, Type
from .api import IpLink


def createIpLinkShell(logger: Logger) -> IpLink:

    class IpLinkShell(IpLink):

        def show(self, name: Optional[str] = None, group: Optional[str] = None, up: Optional[bool] = None, master: Optional[str] = None, vrf: Optional[str] = None, type: Optional[Type] = None) -> Sequence[DeviceAttributes]:
            logger.error('Not implemented yet')
            return []

    return IpLinkShell()
