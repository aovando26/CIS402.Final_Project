import mysql.connector as mc

conn = mc.connect(host='localhost', user='root', password='YUInbound2023!', db='menagerie')
c = conn.cursor()


def show_data():
    c.execute("select * from pet")
    databases = c.fetchall()
    for show in databases:
        print(show)


def main():
    show_data()


if __name__ == '__main__':
    main()
