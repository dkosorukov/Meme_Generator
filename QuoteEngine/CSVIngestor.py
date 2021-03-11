from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """ Class parsing .CSV file and creating
    a list of QuoteModel class instances
    """
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse .CSV file and create a list of QuoteModel classes

        : param path: location of a file to parse
        : return: list of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        quotes = []
        df = pandas.read_csv(path, header=0)

        for _, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
