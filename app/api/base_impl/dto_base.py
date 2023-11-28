"""dto_base.py

This package contains base implementation and interfaces for DTO Handler.

"""
from abc import ABC, abstractmethod

from typing import List


class IDTOHandler(ABC):
    """Interface for DTO handler. All DTO implementations have to have
    all the listed methods.

    """

    @classmethod
    @abstractmethod
    def create_item(cls, **kwargs):
        pass

    @classmethod
    @abstractmethod
    def get_item_by_id(cls, item_id) -> List[dict]:
        pass

    @classmethod
    @abstractmethod
    def get_items(cls) -> List[dict]:
        pass

    @classmethod
    @abstractmethod
    def update_item(cls, item_id) -> List[dict]:
        pass

    @classmethod
    @abstractmethod
    def delete_item(cls, item_id):
        pass


class DTOHandlerBase(IDTOHandler):
    """TBD"""
    pass
