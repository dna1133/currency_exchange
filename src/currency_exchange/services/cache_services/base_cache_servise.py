from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseCacheService(ABC):
    @abstractmethod
    def cached(expire: int = 60): ...
