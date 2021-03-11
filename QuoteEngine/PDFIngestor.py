from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """ Class parsing .PDF file and creating
    a list of QuoteModel class instances
    """
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse .PDF file and create a list of QuoteModel classes

       : param path: location of a file to parse
       : return: list of QuoteModel classes
       """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        pdftotext = r'C:\Program Files\Git\mingw64\bin\pdftotext.exe'
        tmp = f'./tmp/{random.randint(0,10**6)}.txt'
        call = subprocess.run([pdftotext, '-layout', path, tmp])

        file_ref = open(tmp, 'r')
        quotes = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-').strip()
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        file_ref.close()
        os.remove(tmp)
        return quotes
