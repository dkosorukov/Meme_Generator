class QuoteModel():
    def __init__(self, meme_body, meme_author):
        self.meme_body = meme_body
        self.meme_author = meme_author
    
    def __repr__(self):
        return f'{self.meme_body} - {self.meme_author}'