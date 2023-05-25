from datetime import date
from database import session 
from tables import Holidy

holidy = session.query(Holidy).filter_by(holi_date=date(2023, 1, 1)).first()
holidy.holi_text = "元旦"

session.add(holidy)
session.commit()