import psycopg2
from data import data


def getPic(typeOfPic):
    global res
    res = []
    conn = psycopg2.connect(
      database="d5o66qkp7fa9if",
      user="bozhbeiwwhicaz",
      password="1f36e00b25d90d1462a588ddabf2fae0ffbf09a1c3528c61d9888c8cecd0531d",
      host="ec2-34-194-73-236.compute-1.amazonaws.com",
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


def getPicById(id):
    result = data()
    conn = psycopg2.connect(
        database="d5o66qkp7fa9if",
        user="bozhbeiwwhicaz",
        password="1f36e00b25d90d1462a588ddabf2fae0ffbf09a1c3528c61d9888c8cecd0531d",
        host="ec2-34-194-73-236.compute-1.amazonaws.com",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, types, url, review from PIC")
    rows = cur.fetchall()
    for row in rows:
        if str(row[0]) == id:
            result = data(str(row[0]), str(row[1]), str(row[2]), str(row[3]))
    conn.close()
    return result
