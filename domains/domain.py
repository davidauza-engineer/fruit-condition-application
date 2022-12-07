from abc import ABC, abstractmethod


# This class represents an interface of the methods that a domain should implement.
class Domain(ABC):
    @abstractmethod
    def is_valid(self):
        pass
