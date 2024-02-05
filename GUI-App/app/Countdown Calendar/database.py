import sqlite3

def connect_to_database() :
    
    return sqlite3.connect('events.db')

def query(table_name, opt, data = [], value = [], id = 0) :
    db = connect_to_database()
    cursor = db.cursor()
    if opt == 'c' :
        sql = creating_table_sql(table_name, data)
    elif opt == 'a' :
        sql = adding_sql(table_name, data, value)
    elif opt == 's' :
        sql = selecting_sql(table_name)
        cursor.execute(sql)
        print(sql)

        return cursor.fetchall()
    elif opt == 'd' :
        sql = deleleting_sql(table_name, id)
    else : 

        return False
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()

    return True

def creating_table_sql(table_name, data) :
    sql = "CREATE TABLE {} (".format(table_name) 
    data_lists = ''
    for data in datas :
        data_lists += data + " "
        for datatype in datas[data] :
            data_lists += datatype + " "
        data_lists += ", "    
    data_lists = data_lists.rstrip(' ').rstrip(',')
     
    return sql + data_lists + ')'

def adding_sql(table_name, datas, values) :
    sql = "INSERT INTO {} (".format(table_name) 
    data_lists = ''
    for data in datas :
        data_lists += data + ", "
    data_lists = data_lists.rstrip(' ').rstrip(',')
    value_lists = ') VALUES (\''
    for value in values :
        value_lists += value + "', '"
    value_lists = value_lists.rstrip('\'').rstrip(' ').rstrip(',')
    
    return sql + data_lists + value_lists + ')'

def selecting_sql(table_name) :

    return 'SELECT * FROM {}'.format(table_name)

def deleleting_sql(table_name, id) :

    return 'DELETE FROM {} WHERE id = {}'.format(table_name, id)





#=============================================================
'''datas = OrderedDict()
datas['id'] = [
        "INTEGER",
        "PRIMARY KEY",
        "AUTOINCREMENT"
    ]
datas['event'] = [
        "TEXT",
        "NOT NULL"
    ]
datas['date'] = [
        "TEXT",
        "NOT NULL"
    ]

create_table('event', datas)

datas = [
    'event',
    'date'
]

values = [
    'Saint Valentin',
    '14/02/2024 00:00'
]

#print(adding_sql('event', datas, values))

query('events', 'a', datas, values)
for val in query('events', 's') :
    print(val)'''