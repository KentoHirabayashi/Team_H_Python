from datetime import date
from database import session
from tables import Holiday

holiday = session.query(Holiday).filter_by(holi_date = date(2023,1,1)).delete()

session.commit()