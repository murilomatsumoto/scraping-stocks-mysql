from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Ticker():
    cotacao:Optional[str] = ""
    data_cotacao:Optional[datetime] = ""
    p_l:Optional[str] = ""
    roe:Optional[str] = ""
    
    