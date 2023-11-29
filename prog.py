import psycopg2
from faker import Faker
db_params = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database',
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

fake = Faker()

for room_number in range(1, 11):
    cursor.execute('''
        INSERT INTO Rooms (room_number, room_type, floor, tv, refrigerator, capacity, category, cost_per_night)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    ''', (
        room_number,
        fake.random_element(elements=('Single', 'Double', 'Suite')),
        fake.random_int(min=1, max=3),
        fake.boolean(),
        fake.boolean(),
        fake.random_int(min=1, max=4),
        fake.random_element(elements=('Standard', 'Deluxe', 'Luxury')),
        fake.random_int(min=50, max=300)
    ))

for guest_id in range(1, 8):
    cursor.execute('''
        INSERT INTO Guests (registration_number, last_name, first_name, middle_name, city)
        VALUES (%s, %s, %s, %s, %s);
    ''', (
        fake.unique.random_number(),
        fake.last_name(),
        fake.first_name_male(),
        fake.first_name_female(),
        fake.city()
    ))

for registration_code in range(1, 11):
    cursor.execute('''
        INSERT INTO GuestRegistration (guest_id, arrival_date, stay_duration, room_number)
        VALUES (%s, %s, %s, %s);
    ''', (
        fake.random_int(min=1, max=7),
        fake.date_this_year(),
        fake.random_int(min=1, max=10),
        fake.random_int(min=1, max=10)
    ))

connection.commit()

cursor.close()
connection.close()
