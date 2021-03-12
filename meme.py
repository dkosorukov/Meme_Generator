"""Interface module for meme egnerator."""

import os
import random
import argparse

from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None) -> str:
    """.Generate a meme given an path and a quote.
    
    Arguments:
        path {str} -- path to image file
        body {str} -- caption text
        author {str} -- caption author
    Returns:
        path {str} -- path to generated meme image file
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description='Generate a Meme')
    parser.add_argument('--path',
                        type=str,
                        help='path to image file')
    parser.add_argument('--body',
                        type=str,
                        help='caption text to add to image')
    parser.add_argument('--author',
                        type=str,
                        help='caption autor')

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
