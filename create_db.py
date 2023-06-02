import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='YUInbound2023!', db='menagerie')
c = conn.cursor()


def menagerie_db():
    c.execute('CREATE DATABASE menagerie')
    writers = c.fetchall()
    for writer in writers:
        print(writer)


def main():
    menagerie_db()


if __name__ == '__main__':
    main()
