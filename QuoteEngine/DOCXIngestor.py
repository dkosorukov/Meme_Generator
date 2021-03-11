"""DOCX file parser class."""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Class to parse .DOCX file and create a list of QuoteModel class."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .DOCX file and create a list of QuoteModel classes.

        : param path: location of a file to parse
        : return: list of QuoteModel classes
        """
        if not cls.can_ingest(path):
            raise Exception("Cannot ingest file extension exception")

        quotes = []
        doc = docx.Document(path)

        # Iterate through each line
        for para in doc.paragraphs:
            if para.text != "":
                # Split in two and strip "" marks
                parse = [aa.strip().strip('"') for aa in para.text.split('-')]
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
