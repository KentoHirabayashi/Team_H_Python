from datetime import date
#データベース接続
from database import session
#テーブル定義
from attendnum_table import Attendnum

#引数取得
import sys
args = sys.argv

#引数代入
day      =  args[1]
adult     =  int(args[2])
children  =  int(args[3])
seq = session.query(Attendnum).filter_by(entry_date=day).count()

attendnum = Attendnum(
    entry_date = day,
    adult = adult,
    child = children,
    seq = seq + 1
)

session.add(attendnum)
session.commit()