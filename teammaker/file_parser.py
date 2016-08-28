import csv

from teammaker import firebase

def parse_file(file):
	file_reader = csv.reader(file)

	headers = [header.lower().replace(' ', '_') for header in file_reader.next()]

	for row in file_reader:
		create_user(headers, row)

def create_user(headers, row):
	user_data = {headers[i]: row[i] for i in range(len(headers))}
	print user_data

	email = user_data['email'].replace('.', '').replace('@', '')

	firebase.post('/users', data=user_data, params={'print': 'pretty'})
	print 'successfully created user ' + row[1] + ' ' + row[2]