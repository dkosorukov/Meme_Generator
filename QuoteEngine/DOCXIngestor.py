from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """ Class parsing .DOCX file and creating
    a list of QuoteModel class instances
    """
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """ Parse .DOCX file and create a list of QuoteModel classes

        : param path: location of a file to parse
        : return: list of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-').strip()
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
