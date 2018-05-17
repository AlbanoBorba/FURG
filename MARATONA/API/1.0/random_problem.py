#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import random
import sys
import json
import webbrowser
import os
import time

user_info = {}

def get_problem_properties(url):
    info = urllib2.urlopen(url)
    lines = info.readlines()
    print lines[102]
    tmp = lines[102].split(' / ')[0] 
    level = tmp.split()[-1]
    try:
        tmp = lines[119].split('target="_blank">')[1]
    except IndexError:
        tmp = lines[210].split('target="_blank">')[1]
    category = tmp.split('</a>')[0]
    return level, category

def get_user_html(profile_id):
    with open(profile_id, 'w') as f:
        page = 1
        while True:
            try:
                url = 'https://www.urionlinejudge.com.br/judge/en/profile/%s?page=%d' % \
                        (profile_id, page)
                info = urllib2.urlopen(url)
                f.write(info.read())
                page += 1
            except urllib2.HTTPError:
                break

def get_user_info(html):
    count = 0
    last = ''
    problems_solved = []

    found_name = False
    for line in html:
        #print line
        if not found_name and ' @ URI Online Judge</title>' in line:
            tmp = line.split(' @ ')[0]
            name = tmp.split('>')[-1]
            found_name = True
        if '/judge/en/problems/view/' in line:
            halfs = line.split('/judge/en/problems/view/')
            problem = halfs[1][:4]
            if problem != last:
                problems_solved.append(int(problem))
                last = problem
                count += 1
    return name, problems_solved, count

def get_random_problem(name, solved, min_level=1, max_level=10, prohib=[]):
    minimum = 1000
    maximum = 2683

    while True:
        problem_number = random.randint(minimum, maximum)
        if problem_number not in solved:
            url = 'https://www.urionlinejudge.com.br/judge/en/problems/view/' + str(problem_number)
            level, category = get_problem_properties(url)
            if min_level <= int(level) <= max_level and category not in prohib:
                break
    webbrowser.open(url)
    print "a problem level %d just for %s:" % (int(level), name)
    print url

def save_dict(user_info):
    with open('user_info.json', 'w') as fp:
        json.dump(user_info, fp, sort_keys=True, indent=4)

def load_dict():
    try:
        with open('user_info.json', 'r+') as fp:
            try:
                return json.load(fp)
            except ValueError:
                return {}
    except IOError:
        return {}


if __name__ == "__main__":
    user_info = load_dict()
    try:
        profile_id, min_level, max_level = sys.argv[1:4]
    except ValueError:
        print "try: python random_problem.py PROFILE_ID MIN_LEVEL MAX_LEVEL [-f]"
        exit()
    if len(sys.argv) == 3 and sys.argv[2] == '-f':
        try:
            del user_info[profile_id]
        except KeyError:
            pass
    try:
        solved = user_info[profile_id]['solved']
        name = user_info[profile_id]['name']
    except KeyError:
        user_info[profile_id] = {}
        get_user_html(profile_id)
        with open(profile_id, "r") as f:
            name, solved, count = get_user_info(f)
            user_info[profile_id]['name'] = name
            user_info[profile_id]['solved'] = solved
            user_info[profile_id]['count'] = count
        solved = user_info[profile_id]['solved']
    get_random_problem(name, solved, int(min_level), int(max_level))
    try:
        os.remove(profile_id)
    except OSError:
        pass
    save_dict(user_info)