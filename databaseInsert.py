import pymysql


def insertToDatabase(defaultList = []):
    db = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        port=PORT,
        db=DB
    )
    cur = db.cursor()
    sql = 'INSERT INTO sge_data values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    for item in defaultList:
        print(item)
        try:
            row_counst = cur.execute(sql, item)
        except:
            print("insert error")
    # row_counst = cur.execute(sql, defaultList)
    db.commit()
    cur.close()
    db.close()

