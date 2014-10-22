#!/usr/bin/python

from teachdb import TeachDB
import requests
import sys
import codecs
import os

# Enable piping of Unicode output to files
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

login = sys.argv[1]
groupid = sys.argv[2]
year = int(sys.argv[3])

t = TeachDB(login)
year = t.get_all_students_from_year(year)

group = requests.get('https://graph.facebook.com/v2.1/' + groupid
                     + '/members?access_token='
                     + os.environ['FB_ACCESS']).json()['data']

matched_in_db = []
matched_in_group = []

for student in group:
    match = next((s for s in year
                  if student['name'] == s['firstname'] +
                  ' ' + s['lastname']), None)

    if match:
        matched_in_db.append(match)
        matched_in_group.append(student)

[group.remove(x) for x in matched_in_group]
[year.remove(x) for x in matched_in_db]

print "On Facebook group, but not in DB:"
for i in group:
    print i['name']
print "----------\nIn DB, but not on Facebook group:"
for i in year:
    print i['firstname'] + ' ' + i['lastname']
