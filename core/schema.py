from pydantic import BaseModel

class TicketConfig(BaseModel):
    registration_template: str
    registration_color: tuple[int, int, int]
    font_family: str
    name_offset: tuple[int, int]
    lc_offset: tuple[int, int]
    max_font_size: int
    max_text_size: int
    multi_line: bool = False
    allow_multi_line: bool = True

class ServiceConfig(BaseModel):
    id: str
    name: str
    ticket_config: TicketConfig = None
