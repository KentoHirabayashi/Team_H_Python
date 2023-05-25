from datetime import date
from database import session 
from tables import Holidy

holidy = Holidy(
    holi_date = date(2024, 1, 1),
    holi_text = "お正月"
)

session.add(holidy)
session.commit()