import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Shravani@123",  
        database="intellimedi"        
    )
def insert_patient(name, age, gender, symptoms):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO patients (name, age, gender, symptoms) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (name, age, gender, symptoms))
    conn.commit()
    conn.close()