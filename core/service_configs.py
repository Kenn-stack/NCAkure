import os

from django.conf import settings
from .schema import ServiceConfig, TicketConfig
from django.templatetags.static import static

nc_akure = ServiceConfig(
    id= 'nc-akure',
    name= 'NC Akure',
    ticket_config= TicketConfig(
        registration_template = os.path.join(settings.BASE_DIR, 'static', 'nc_akure', 'ticket.png'),
        registration_color = (0, 0, 0),
        font_family = os.path.join(settings.BASE_DIR, 'static', 'nc_akure', 'Raleway', 'static', 'Raleway-Bold.ttf'),
        name_offset = (142, 429),
        lc_offset = (110, 510),
        max_font_size = 20,
        max_text_size = 200
    )
)

service_configs: dict[str, ServiceConfig] = {
  nc_akure.id: nc_akure,}
