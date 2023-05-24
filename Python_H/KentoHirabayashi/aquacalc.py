from datetime import date, datetime
import sys
import re


def get_date(date_string: str) -> date:
    """概要

    区切り文字が無い日付の入力を、dateオブジェクトに変換

    Parameters
    ----------
    date_string: string
        20220516のように、区切り文字が無い日付
    

    Returns
    -------
    dt: date
        日付の処理を行える、datetimeオブジェクトを生成
    """

    ## splite date 
    pattern = r"(\d{4})(\d{2})(\d{2})"
    splite_date = re.search(pattern, input_date)
    year, month, day = splite_date.groups()

    ## create date object
    dt = date(int(year), int(month), int(day))

    return dt

def calc_aqua_admission(date: date, adult_cnt: int, child_cnt: int) -> int:
    """概要

    平日・休日料金を求めて、総額を返却

    Parameters
    ----------
    date: date
        入力された日付のdateオブジェクト
    adult_cnt: int
        大人の人数
    child_cnt: int
        子供の人数
    

    Returns
    -------
    pay: int
        入場料の総額を計算する
    """

    #休日料金
    if date.weekday() >= 5:
        pay = 2400 * adult_cnt + 1500 * child_cnt
    #平日料金
    else:
        pay = 2000 * adult_cnt + 1200 * child_cnt

    return pay


args = sys.argv

#引数を変数に代入
input_date = args[1]
adult = int(args[2])
child = int(args[3])

#dateオブジェクトに変換 -> 平日休日を考慮した入場料計算
# date = get_date(input_date)
date = datetime.strptime(input_date, "%Y%m%d")
pay = calc_aqua_admission(date, adult, child)
print(pay, end="")