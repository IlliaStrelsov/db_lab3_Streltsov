import csv
import psycopg2


INPUT_CSV_FILE = 'vgsales.csv'

query_delete = '''

DELETE FROM video_games  

'''

query = '''
INSERT INTO video_games (video_game_name, video_game_platform, video_game_genre, year_of_publication) VALUES (%s, %s, %s, %s)
'''

conn = psycopg2.connect(database="TestDataBase", user="playtender", password="playtender", host="localhost", port=5432)

with conn:
    cur = conn.cursor()
    cur.execute(query_delete)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if(row['Year'] != 'N/A'):
                values = (row['Name'], row['Platform'], row['Genre'], row['Year'])
                cur.execute(query, values)

    conn.commit()
