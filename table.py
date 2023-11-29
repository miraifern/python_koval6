import psycopg2

db_params = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE Guests (
        guest_id SERIAL PRIMARY KEY,
        registration_number INT,
        last_name VARCHAR(255),
        first_name VARCHAR(255),
        middle_name VARCHAR(255),
        city VARCHAR(255)
    );
''')

cursor.execute('''
    CREATE TABLE Rooms (
        room_number INT PRIMARY KEY,
        room_type VARCHAR(50),
        floor INT,
        tv BOOLEAN,
        refrigerator BOOLEAN,
        capacity INT,
        category VARCHAR(20),
        cost_per_night DECIMAL(10, 2)
    );
''')

cursor.execute('''
    CREATE TABLE GuestRegistration (
        registration_code SERIAL PRIMARY KEY,
        guest_id INT REFERENCES Guests(guest_id),
        arrival_date DATE,
        stay_duration INT,
        room_number INT REFERENCES Rooms(room_number)
    );
''')

connection.commit()

cursor.close()
connection.close()
