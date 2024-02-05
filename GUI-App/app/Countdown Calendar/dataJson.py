#!/usr/bin/env python3 
import json
def create_data_file() :
    try :
        with open('data.json', 'x',) as f :
            print('JSON data created !')
        f.closed
    except FileExistsError as e :
        print('JSON data arleady exists !')

def add_events(event, date) :
    with open('data.json', 'r') as f :
        data = json.load(f)
        data["events"].append(event)
        data["dates"].append(date + ' 00:00')
    f.closed
    with open('data.json', 'w') as f :
        json.dump(data,f)
    f.closed

#add_events("Nouvelle An", "01/01/2025")