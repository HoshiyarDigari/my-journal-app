from flask import Blueprint, render_template, send_file, request
from PIL import Image, ImageDraw, ImageFont



hindi_bp=Blueprint('hindi', __name__)

@hindi_bp.route('/')
# display the hindi fonts for tracing practice
def hindi():
    vowels = ["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", "अं", "अः"]
    consonants = ["क", "ख", "ग", "घ", "ङ","च", "छ", "ज", "झ", "ञ","ट", "ठ", "ड", "ढ", "ण","त", "थ", "द", "ध", "न","प", "फ", "ब", "भ", "म","य", "र", "ल", "व","श", "ष","स", "ह","क्ष", "त्र", "ज्ञ"]

    return render_template('hindi.html', vowels=vowels, consonants=consonants)


@hindi_bp.route('/tracing/', methods=['POST'])
# 

def tracing(letter):
    payload = request.data
    # Create a blank image
    img = Image.new('RGBA', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    # Load Hindi font
    font = ImageFont.truetype('static/hindi.ttf', size=200)

    # Draw the letter
    draw.text((30, 20), letter, font=font, fill='black')

    # Create a mask to identify letter boundaries
    mask = Image.new("L", img.size, 0)  # Grayscale mask
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.text((30, 20), letter, font=font, fill=255)

    # # Add dots dynamically within the letter
    # dot_spacing = 15
    # for x in range(0, img.size[0], dot_spacing):
    #     for y in range(0, img.size[1], dot_spacing):
    #         if mask.getpixel((x, y)) > 0:  # Check if pixel is inside the letter
    #             draw.ellipse((x - 3, y - 3, x + 3, y + 3), fill="red")

    # Save the image
    img.save(f'static/images/letters/{letter}.png')
    return send_file(f'static/images/letters/{letter}.png', mimetype='image/png', as_attachment=False)


