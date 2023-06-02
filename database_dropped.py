import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='YUInbound2023!', db='menagerie')
c = conn.cursor()


def drop_db():
    c.execute('DROP DATABASE IF EXISTS menagerie')


def main():
    drop_db()


if __name__ == '__main__':
    main()
