from abc import ABC, abstractmethod


class Domain(ABC):
    @abstractmethod
    def is_valid(self):
        pass
