"""Module to fetch user submitted quote and URL image."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine
from QuoteEngine import QuoteModel


app = Flask(__name__)

# Instantiate class
meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Parse all quote files into caption text and author
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    # Collect all images
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs

# Load quotes and images
quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Select random image and quote
    img = random.choice(imgs)
    quote = random.choice(quotes)
    # Create a meme and return path to created image
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    # Create quote
    quote = QuoteModel(body, author)

    # Save image in temp file
    image_content = requests.get(img_url, stream=True).content
    temp_path = './tmp/temp_img.jpg'
    open(temp_path, 'wb').write(image_content)

    # Create meme
    path = meme.make_meme(temp_path, quote.body, quote.author)

    # Remove the temporary saved image
    os.remove(temp_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
