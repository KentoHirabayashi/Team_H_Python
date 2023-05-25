import sys
import datetime
from database import session
from tables import Holiday

args = sys.argv

in_data = (args[1],int(args[2]),int(args[3]))

dateargs = datetime.datetime.strptime(in_data[0], "%Y%m%d")

weekday = datetime.datetime.strftime(dateargs,"%a")



if(weekday == "Sat") or (weekday == "Sun"):
    adult_total_price = 2400 * in_data[1]
    child_total_price = 1500 * in_data[2]

else:
    holiday = session.query(Holiday.holi_date).filter_by(holi_date = dateargs).first()

    if holiday is None:
        adult_total_price = 2000 * in_data[1]
        child_total_price = 1200 * in_data[2]  
    else:      
        adult_total_price = 2400 * in_data[1]
        child_total_price = 1500 * in_data[2]





total_price = adult_total_price + child_total_price
print(total_price,end="")