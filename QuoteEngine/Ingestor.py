"""Main Ingestor class to contain all other ingestors."""
from typing import List

from .IngestorInterface import IngestorInterface
from .DOCXIngestor import DOCXIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TXTIngestor import TXTIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """Main class to encapsulate all ingestors."""

    importers = [DOCXIngestor, CSVIngestor, PDFIngestor, TXTIngestor]
 
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select appropriate ingestor based on file extension."""
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)