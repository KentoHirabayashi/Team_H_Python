from datetime import date
from database import session 
from tables import Holidy

result = session.query(Holidy).filter_by(holi_date=date(2024, 1, 1)).delete()
session.commit()