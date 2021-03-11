from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """ Class parsing .TXT file and creating
    a list of QuoteModel class instances
    """
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse .TXX file and create a list of QuoteModel classes

       : param path: location of a file to parse
       : return: list of QuoteModel classes
       """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        file_ref = open(path, 'r')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-').strip()
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        file_ref.close()

        return quotes
