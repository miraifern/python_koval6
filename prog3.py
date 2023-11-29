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

tables = ['Guests', 'Rooms', 'GuestRegistration']

for table in tables:
    cursor.execute(f'SELECT column_name, data_type FROM information_schema.columns WHERE table_name = \'{table}\';')
    columns_info = cursor.fetchall()
    print(f"\nСтруктура таблиці '{table}':")
    print("|".join(["Column Name", "Data Type"]))
    print("-" * 30)
    for column_info in columns_info:
        print("|".join(map(str, column_info)))

    cursor.execute(f'SELECT * FROM {table};')
    rows = cursor.fetchall()
    print(f"\nДані таблиці '{table}':")
    for row in rows:
        print("|".join(map(str, row)))

cursor.close()
connection.close()
