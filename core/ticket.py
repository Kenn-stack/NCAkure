import re
from io import BytesIO

#from fastapi.exceptions import HTTPException
from PIL import Image, ImageDraw, ImageFont
from ninja.errors import HttpError

from .service_configs import service_configs


def make_ticket(img_file, color, attendee_name, lc, name_offset, lc_offset, font_family, max_font_size, max_text_size, allow_multi_line=True) -> Image:  # noqa: FBT002
    #opens the image file and converts image to RGB mode
    img = Image.open(img_file, 'r').convert('RGB')
    imgdraw = ImageDraw.Draw(img)
    font_size = max_font_size

    def get_text_size(text, font):
        # multiline_text method to get text dimensions
        return imgdraw.multiline_textbbox((0, 0), text, font=font)[2]

    font = ImageFont.truetype(font_family, font_size)
    width = get_text_size(attendee_name, font)
    
    # checks if the name fits in the maximum font size
    while width > max_text_size:
        # replace spaces with newlines
        if font_size == max_font_size and allow_multi_line:
            attendee_name = attendee_name.replace(' ', '\n')
        else:
            font = ImageFont.truetype(font_family, font_size)

        width = get_text_size(attendee_name, font)
        font_size -= 1

    # Use multiline_text for drawing
    imgdraw.multiline_text(name_offset, attendee_name, color, font=font)
    imgdraw.multiline_text(lc_offset, lc, color, font=font)
    buffer = BytesIO()
    img.save(buffer, format='PDF', resolution=300.0)
    buffer.seek(0)
    return buffer


def generate_delegate_ticket(attendee_name: str, lc: str, service: str = 'nc-akure'):
    """generates a delegate ticket for a service and participant names."""

    service_config = service_configs.get(service)

    if service_config is None or service_config.ticket_config is None:
        raise HttpError(404, "Requested service is unavailable")

    attendee_name = ' '.join(word.capitalize() for word in attendee_name.split())
    lc = lc.capitalize()
    
    ticket_config = service_config.ticket_config

    img = make_ticket(
        ticket_config.registration_template,
        ticket_config.registration_color,
        attendee_name,
        lc,
        ticket_config.name_offset,
        ticket_config.lc_offset,
        ticket_config.font_family,
        ticket_config.max_font_size,
        ticket_config.max_text_size,
        ticket_config.allow_multi_line
    )

    # return the in-memory image buffer and a formatted filename for the ticket
    
    return img
#generate_delegate_ticket('nc-akure', 'Ekenedilichukwu', 'agwu', 'enugu')