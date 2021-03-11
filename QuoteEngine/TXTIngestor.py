"""TXT file parser class."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Class to parse .TXT file and create a list of QuoteModel class."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .TXX file and create a list of QuoteModel classes.

        Arguments:
            path {str} -- location of a file to parse
        Returns:
            list -- collection of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        file_ref = open(path, 'r')
        quotes = []

        # Iterate through each line in txt file
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                # Split in two and strip "" marks
                parse = [aa.strip().strip('"') for aa in line.split('-')]
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        file_ref.close()

        return quotes
