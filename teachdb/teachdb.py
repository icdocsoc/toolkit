from bs4 import BeautifulSoup
import requests
import os


class TeachDB:

    params = {
        'Student': [
            'login', 'firstname', 'lastname',
            'dept', 'lettyr', 'degree', 'year',
            'studentstatus', 'entryyear'
        ]
    }

    def __init__(self, username):
        self.username = username

    def fetch_from_teachdb(self, table, **kwargs):
        url = 'https://teachdb.doc.ic.ac.uk/db/viewtab?table=' + table
        for k, v in kwargs.iteritems():
            tab = self.params[table]
            if k in tab:
                url += '&arg' + str(tab.index(k) + 1) + '=' + str(v)
        r = requests.get(url, auth=(self.username, os.environ.get('IC_PASS')))
        if r.status_code == 401:
            raise Exception("Invalid login details")
        soup = BeautifulSoup(r.text)
        trs = soup.form.table.find_all('tr')[2:]
        results = []
        for tr in trs:
            tds = tr.find_all('td')[2:]
            result = {}
            for i in range(0, len(tds)):
                result[self.params[table][i]] = tds[i].string
            results.append(result)
        return results

    def get_all_students_from_year(self, year):
        return self.fetch_from_teachdb('Student', year=year)
