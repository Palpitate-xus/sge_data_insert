import pymysql


# sh-cynosdbmysql-grp-9chdkjpu.sql.tencentcdb.com:23567
def insertToDatabase(defaultList = []):
    db = pymysql.connect(
        host='sh-cynosdbmysql-grp-9chdkjpu.sql.tencentcdb.com',
        user='XuSheng',
        password='XuSheng717',
        port=23567,
        db='precious_metal'
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

