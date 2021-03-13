"""PDF file parser class."""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse .PDF file and create a list of QuoteModel class."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .PDF file and create a list of QuoteModel classes.

        Arguments:
            path {str} -- location of a file to parse
        Returns:
            list -- collection of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        # Create temporary file
        tmp = f'./tmp/{random.randint(0,10**6)}.txt'
        # Call pdftotext.exe to read content and write to txt file
        subprocess.run([pdftotext, '-layout', path, tmp])

        file_ref = open(tmp, 'r')
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
        # Delete temporary txt file
        os.remove(tmp)

        return quotes
