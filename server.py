from flask import Flask, request
import argparse
import csv
import json
import sys

#Web app
app = Flask(__name__)

people_file = ""
keys_to_index = {}
people = []

@app.route('/ping',methods=['GET'])
def pingServer():
    '''
    Ping request to make sure server is alive, return 'pong'
    '''
    return 'pong'

@app.route('/people',methods=['GET'])
def getPeople():
    '''
    Return a standard JSON block of people in any order of format. Must be valid JSON
    '''
    return json.dumps(people)

@app.route('/people/age',methods=['GET'])
def sortPeopleByAge():
    '''
    Returns Json block containing a list of people sorted by age youngest to oldest
    '''
    age_index = keys_to_index.get("Age")
    sortedList = sorted(
        people,
        key=lambda person: int(person[age_index]) if person[age_index] != "" else float("inf")
    )

    return json.dumps(sortedList)

@app.route('/ids/lastname/<lastname>',methods=['GET'])
def getIdsByLastName(lastname):
    '''
    Returns Json block of ids found for the given last name
    Using path params
    '''
    id_index = keys_to_index.get("ID")
    last_name_index = keys_to_index.get("Last")
    ids = [person[id_index] for person in people if person[last_name_index].lower() == lastname.lower()]

    return json.dumps(ids)

@app.route('/people/add', methods=['POST'])
def addPerson():
    person_dict = request.get_json(force=True)

    person = []
    for key in keys:
        if key == "ID":
            person.append(str(len(people) + 1))
            continue

        v = person_dict.get(key, None)
        if v is not None:
            person.append(v)
        else:
            person.append("")

    people.append(person)
    with open(people_file, "a") as file_d:
        writer = csv.writer(file_d)
        writer.writerow(person)

    return json.dumps(people)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--debug", help="Optional Debug Mode for stack traces", action="store_true")

    parser.add_argument("port", help="Port to run the app on")
    parser.add_argument("file", help="File to import data from")
    args = parser.parse_args()

    people_file = args.file
    with open(people_file, 'r', encoding='utf-8-sig') as file_d:
        people_reader = csv.reader(file_d)

        keys = next(people_reader)
        keys_to_index = { key: index for index,key in enumerate(keys)}

        for person in people_reader:
            people.append(person)

    app.run(host='0.0.0.0', port=args.port, debug=args.debug)
