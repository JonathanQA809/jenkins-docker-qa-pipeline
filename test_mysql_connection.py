
import pymysql

def test_mysql_connection():
    connection = pymysql.connect(
        host="mysql-db",
        user="qa_user",
        password="qapassword",
        port=3306
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            result = cursor.fetchone()

        assert result[0] == 1

    finally:
        connection.close()