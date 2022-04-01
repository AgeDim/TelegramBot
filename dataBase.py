import psycopg2
from data import data


def getPic(typeOfPic):
    global res
    res = []
    conn = psycopg2.connect(
      database="dd86jtje2j77cm",
      user="kywvximbjqrwcc",
      password="a3b29c5b241080cdc2d6a8b338a11d478da374452824e6738b0cac1e4504f7d9",
      host="ec2-34-231-63-30.compute-1.amazonaws.com",
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
