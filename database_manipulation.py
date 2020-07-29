import pymysql
import traceback

def News_insert(NewsTitle,NewsContent,NewsTime):
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "12345678", "News")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO news(News_Title, News_content,News_Time)  VALUES (%s, %s, %s)"
    try:
       # 执行sql语句
       print('Inserting data....')
       cursor.execute(sql,[NewsTitle, NewsContent, NewsTime])
       # 提交到数据库执行
       db.commit()
    except:
       print('Data insert error....')
       # 发生错误时回滚
       db.rollback()

    # 关闭数据库连接
    db.close()