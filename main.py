import psycopg2
import matplotlib.pyplot as plt

query_1 = ''' 
CREATE VIEW VideoGameGenre as 
SELECT DISTINCT(video_game_genre),COUNT(video_game_genre) FROM video_games GROUP BY video_game_genre
'''

query_2 = '''
CREATE VIEW VideoGameSalesRegion as
SELECT SUM(na.na_sales) as sumNa,SUM(eu.eu_sales)as sumEu,SUM(jp.jp_sales) as sumJp,SUM(other.other_sales) as sumOther FROM na_sales na JOIN eu_sales eu ON na.video_game_id = eu.video_game_id
JOIN jp_sales jp ON jp.video_game_id = eu.video_game_id JOIN other_sales other ON other.video_game_id = jp.video_game_id
'''

query_3 = '''
CREATE VIEW VideoGameGenreToPlatform as 
SELECT video_game_platform,video_game_genre FROM video_games
'''

connection = psycopg2.connect(database="TestDataBase", user="playtender", password="playtender", host="localhost", port=5432)



with connection:

    cursor = connection.cursor()
    cursor.execute('DROP VIEW IF EXISTS VideoGameGenre')
    cursor.execute(query_1)
    cursor.execute('SELECT * FROM VideoGameGenre')
    record1 = cursor.fetchall()

    cursor.execute('DROP VIEW IF EXISTS VideoGameSalesRegion')
    cursor.execute(query_2)
    cursor.execute('SELECT * FROM VideoGameSalesRegion')
    record2 = cursor.fetchall()

    cursor.execute('DROP VIEW IF EXISTS VideoGameGenreToPlatform')
    cursor.execute(query_3)
    cursor.execute('SELECT * FROM VideoGameGenreToPlatform')
    record3 = cursor.fetchall()

    helpingArr = {}
    for i in range(len(record1)):
        helpingArr[record1[i][0]] = record1[i][1]

    plt.bar(helpingArr.keys(), helpingArr.values(), width=0.5)
    plt.xlabel('Жанри ігор')
    plt.ylabel('Кількість')
    plt.show()

    helpingArr = {
        'Na sales': record2[0][0],
        'Jp sales': record2[0][1],
        'Eu sales': record2[0][2],
        'Other sales': record2[0][3],
    }

    fig, ax = plt.subplots()
    ax.pie(helpingArr.values(), labels=helpingArr.keys(), autopct='%1.1f%%', shadow=True, rotatelabels=True)
    plt.show()

    helpingArr = {}
    for i in range(len(record3)):
        helpingArr[record3[i][0]] = record3[i][1]

    fig, ax = plt.subplots()
    ax.plot(helpingArr.keys(), helpingArr.values(), )

    plt.xlabel('Platform')
    plt.ylabel('Genre')
    plt.show()