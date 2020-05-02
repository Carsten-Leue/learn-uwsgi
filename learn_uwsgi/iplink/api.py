import abc
from typing import Optional, Sequence
from ..models import DeviceAttributes, Type


class IpLink(abc.ABC):

    @abc.abstractmethod
    def show(self, name: Optional[str] = None, group: Optional[str] = None, up: Optional[bool] = None, master: Optional[str] = None, vrf: Optional[str] = None, type: Optional[Type] = None) -> Sequence[DeviceAttributes]:
        pass
