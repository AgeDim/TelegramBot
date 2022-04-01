import psycopg2
from data import data


def getPic(typeOfPic):
    global res
    res = []
    conn = psycopg2.connect(
      database="123",
      user="123",
      password="123",
      host="123",
      port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, types, url, review from PIC")
    rows = cur.fetchall()
    for row in rows:
        if str(row[1]) == typeOfPic:
            res.append(data(str(row[0]), str(row[1]), str(row[2]), str(row[3])))
    conn.close()
    return res
