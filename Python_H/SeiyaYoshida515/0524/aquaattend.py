from datetime import date
from database import session
from tables import Attendnum

#引数を受け取るための設定
import sys
args = sys.argv
#引数を変数に格納
date_str = args[1]
adult_num = int(args[2])
child_num = int(args[3])
#日付をリスト化
date_list = [int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8])]
#dateクラスに格納
date_tmp = date(date_list[0], date_list[1], date_list[2])

tmp = session.query(Attendnum).filter_by(date = date_tmp).count()
#リストに追加
adddata = Attendnum(
    date = date_tmp,
    seq = tmp + 1,
    adult = adult_num,
    child = child_num
)
session.add(adddata)
session.commit()