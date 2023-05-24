from datetime import date
from database import session
from tables import Holiday
from tables import Attendnum
import datetime
import sys
args = sys.argv

input_date = str(args[1]) #日付、文字列 
adult_num = int(args[2]) #人数
child_num = int(args[3]) #人数

dt = datetime.datetime.strptime(input_date, "%Y%m%d") # 5行目の文字列→日付(20XX, XX, XX)
#youbi = datetime.datetime.strftime(dt,"%a")           #日付→文字列（曜日）

#連番取得
sequence = session.query(Attendnum.seq).filter_by(entry_date = dt).order_by(Attendnum.seq.desc()).first()
#連番かどうか確認
if sequence is None:
    seq_num = 1
else:
    seq_num = sequence.seq + 1

#来場者管理
attendnum = Attendnum(
    entry_date = dt, 
    seq = seq_num,
    adult = adult_num,
    child = child_num
)

session.add(attendnum)
session.commit()