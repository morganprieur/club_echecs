
from abc import ABC, abstractmethod 


class AbstractModel(ABC): 

    def to_dict(self, exclude=None):
        exclude = exclude or []
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_")
            and key not in exclude
            and not callable(getattr(self, key))
            and isinstance(getattr(self, key), (str, int, float))
        } 


