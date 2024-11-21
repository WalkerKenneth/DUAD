import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        user="",
        dbname="lyfter_car_rental",
        password="",
    )
    return connection

def execute_query(query, params=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()    