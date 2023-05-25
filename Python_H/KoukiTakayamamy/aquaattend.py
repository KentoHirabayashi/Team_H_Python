import sys
import datetime
from database import session
from tables import Attendnum

args = sys.argv

in_data = (args[1],int(args[2]),int(args[3]))

dateargs = datetime.datetime.strptime(in_data[0], "%Y%m%d")

max_num = session.query(Attendnum).filter_by(date = dateargs).count()


attendnum = Attendnum(
    date = dateargs,
    seq = max_num + 1,
    adult = in_data[1],    
    child = in_data[2]
)

session.add(attendnum)

session.commit()


