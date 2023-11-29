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

cursor.execute('SELECT * FROM Rooms WHERE tv = TRUE;')
print("Номери з телевізором:")
print(cursor.fetchall())

cursor.execute('''
    SELECT guest_id, arrival_date, stay_duration, arrival_date + stay_duration AS departure_date
    FROM GuestRegistration;
''')
print("\nКінцева дата проживання для кожного гостя:")
print(cursor.fetchall())

cursor.execute('''
    SELECT category, COUNT(*) AS room_count
    FROM Rooms
    GROUP BY category;
''')
print("\nКількість номерів кожної категорії:")
print(cursor.fetchall())

cursor.execute('''
    SELECT
        gr.guest_id,
        g.last_name,
        g.first_name,
        g.middle_name,
        SUM(r.cost_per_night * gr.stay_duration) AS total_cost
    FROM GuestRegistration gr
    JOIN Guests g ON gr.guest_id = g.guest_id
    JOIN Rooms r ON gr.room_number = r.room_number
    GROUP BY gr.guest_id, g.last_name, g.first_name, g.middle_name;
''')
print("\nПовна вартість проживання для кожного гостя:")
print(cursor.fetchall())

cursor.execute('''
    SELECT
        floor,
        category,
        COUNT(*) AS room_count
    FROM Rooms
    GROUP BY floor, category
    ORDER BY floor, category;
''')
print("\nКількість номерів кожної категорії на кожному поверсі:")
print(cursor.fetchall())

selected_category = 'Standard'
cursor.execute('''
    SELECT
        g.last_name,
        g.first_name,
        g.middle_name,
        r.room_number,
        r.category
    FROM Guests g
    JOIN GuestRegistration gr ON g.guest_id = gr.guest_id
    JOIN Rooms r ON gr.room_number = r.room_number
    WHERE r.category = %s;
''', (selected_category,))
print(f"\nГості в номерах категорії '{selected_category}':")
print(cursor.fetchall())

cursor.execute('''
    SELECT *
    FROM Guests
    ORDER BY last_name;
''')
print("\nГості, відсортовані по прізвищу:")
print(cursor.fetchall())

cursor.close()
connection.close()
