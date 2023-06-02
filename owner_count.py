import mysql.connector as mc
conn = mc.connect(host='localhost', user='root', password='YUInbound2023!', db='menagerie')
c = conn.cursor()


def count_owner():
    c.execute('SELECT owner, COUNT(*) FROM pet GROUP BY owner')
    pets = c.fetchall()
    for pet in pets:
        print(pet)


def main():
    count_owner()


if __name__ == '__main__':
    main()
