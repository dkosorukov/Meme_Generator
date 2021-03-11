from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """ Abstract class parsing a file and creating
    a list of QuoteModel class instances
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """ Check if a file extension is in allowed list
        
        Concrete subclasses must override this method

        :param path: location of a file to parse
        :return: whether a file type can be parsed
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Create a list of QuoteModel classes

        Concrete subclasses must override this method with
        parsing specific to a file extension

        : param path: location of a file to parse
        : return: list of QuoteModel classes
        """
        pass
