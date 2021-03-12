"""Class to manipulate image and draw caption onto image."""
from PIL import Image, ImageDraw, ImageFont
import random


class MemeEngine():
    """Class to manipulate image and draw caption onto image."""

    def __init__(self, img_out_path='./tmp'):
        """Create instance of class.

        Arguments:
            img_out_path {str} -- output folder for processed images
        """
        self.img_out_path = img_out_path

    def make_meme(self, img_path, text=None, author=None, width=500) -> str:
        """Make a meme by adding caption on a resized image.

        Arguments:
            img_path {str} -- the file location of the input image
            text {str} -- image caption text to put on the image
            author {str} -- author name
            width {int} -- resize image to max width
        Returns:
            str -- location of the produced meme image file
        """
        width_limit = width
        file_ext = img_path.split('.')[-1]

        # Load image
        img = Image.open(img_path)
        # Resize image so the width is at most 500px and the height\
        # is scaled proportionally
        width, height = img.size
        if width > width_limit:
            scale_ratio = width_limit / width
            width = int(width * scale_ratio)
            height = int(height * scale_ratio)
            size = (width, height)
            img = img.resize(size, Image.NEAREST)

        # Add caption text to the image
        if text is not None:
            draw = ImageDraw.Draw(img)
            fnt_size = int(height / 12)
            fnt = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                     size=fnt_size)

            # "No text" frame around the image of at least 10px
            frame_margin = max(10, int(fnt_size / 4))
            # Keep horizontal position fixed at the no text frame
            caption_x = frame_margin
            # Texbox size for unfolded text
            x1, y1, x2, y2 = draw.multiline_textbbox(
                                                     (0, 0),
                                                     f'"{text}"\n-{author}',
                                                     font=fnt
                                                     )
            # Number of lines to split text into
            n_lines = int((x2 - x1) / width) + ((x2 - x1) % width > 0)
            # Split text into multiple lines
            if n_lines > 1:
                string_length = len(text)
                txt_lines = ['']
                ii = 0
                for word in text.split():
                    if len(txt_lines[ii] + ' ' + word) < string_length/n_lines:
                        txt_lines[ii] += word + ' '
                    else:
                        txt_lines.append(word + ' ')
                        ii += 1
                n_lines = len(txt_lines)
                text = "\n".join(txt_lines)
                # Update now a multi line text box size
                _, y1, _, y2 = draw.multiline_textbbox(
                                                       (0, 0),
                                                       f'"{text}"\n-{author}',
                                                       font=fnt
                                                       )

            # Random vertical position of the text box
            caption_y = random.randint(frame_margin,
                                       height - frame_margin - (y2 - y1))
            draw.text((caption_x, caption_y),
                      f'"{text}"\n-{author}',
                      font=fnt,
                      fill='white')

        out_path = f'{self.img_out_path}/{random.randint(0,10**6)}.{file_ext}'
        img.save(out_path)
        return out_path

    def __repr__(self):
        """Machine readable string representating this class."""
        return f'{self.img_out_path}'

if __name__ == '__main__':
    postcard = MemeEngine()
    print(postcard)
    postcard.make_meme('./_data/photos/dog/xander_1.jpg',
                       'Hello', 'Sobaka', 500)
