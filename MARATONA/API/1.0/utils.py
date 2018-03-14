import urllib2
import json

def load_dict(d, dict_name):
    try:
        with open('%s.json' % dict_name, 'r+') as fp:
            try:
                d = json.load(fp)
            except ValueError:
                d = {}
    except IOError:
        pass
        
def save_dict(d, dict_name):
    with open('%s.json' % dict_name, 'w') as fp:
        json.dump(d, fp, sort_keys=True, indent=4)

def get_html(page_type, profile_id='0', page=1, problem_id='1001'):
    if page_type == "profile":
        profile_url = 'https://www.urionlinejudge.com.br/judge/en/profile/'
        page_url = '?page=' + str(page)
        try:
            return urllib2.urlopen(profile_url + profile_id + page_url)
        except urllib2.HTTPError:
            return 'ERROR'
    elif page_type == "problem":
        problem_url = 'https://www.urionlinejudge.com.br/judge/en/problems/view/'
        return urllib2.urlopen(problem_url + problem_id)

def get_name_from_html(html):
    for line in html:
        if '<title>' in line:
            tmp = line.split(' @ ')[0]
            return tmp.split('<title>')[-1]

def get_title_from_html(html):
    for line in html:
        if '<title>' in line:
            return line.split(' - ')[1]

def get_level_from_html(html):
    for line in html:
        if '/ 10</span>' in line:
            tmp = line.split(' / ')[0]
            return tmp.split()[-1]

def get_category_from_html(html):
    for line in html:
        if '/judge/pt/problems/index/' in line:
            print line
            tmp = line.split('target="_blank">')[1]
            return tmp.split('</a>')[0]