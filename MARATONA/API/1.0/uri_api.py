import urllib2, json, webbrowser
import sys, os
import random
import time
import utils

user_dict = {}
problem_dict = {}


def get_problems_from_html(html):
    last = ''
    problems = []
    num = 0
    print html
    now = time.time()
    for line in html:
        num += 1
        #print type(html)
        #print num
        #print line
        if '/judge/en/problems/view/' in line:
            tmp = line.split('/judge/en/problems/view/')
            identifier = tmp[1][:4]
            if identifier != last:
                if identifier not in problem_dict.keys():
                    problem_html = utils.get_html("problem", problem_id=identifier)
                    tmp_dict = dict()
                    tmp_dict["problem_id"] = identifier
                    now = time.time()
                    tmp_dict["level"] = utils.get_level_from_html(problem_html)
                    print "level", time.time() - now
                    now = time.time()
                    tmp_dict["category"] = utils.get_category_from_html(problem_html)
                    print "category", time.time() - now
                    now = time.time()
                    tmp_dict["title"] = utils.get_title_from_html(problem_html)
                    print "title", time.time() - now
                    problem_dict[identifier] = tmp_dict
                problems.append(identifier)
                last = identifier
        elif '<div class="site-coyright">' in line:
            break
    print time.time() - now
    return problems

class User:

    def __init__(self, profile_id):
        self.profile_id = profile_id
        profile_html = utils.get_html("profile", self.profile_id)
        self.name = utils.get_name_from_html(profile_html)
        self.solved = 0
        self.problems = []

    def get_name(self):
        return self.name

    def get_info(self):
        page = 1
        now = time.time()
        while True:
            page_html = utils.get_html("profile", self.profile_id, page)
            print "got page %d info html" % page
            if page_html == 'ERROR':
                break
            problems_this_page = get_problems_from_html(page_html)
            print "got page %d problems" % page
            self.problems.append(problems_this_page)
            page += 1
        print time.time() - now

    def get_problem(self, min_level=1, max_level=10, prohib=[]):
        minimum = 1001
        maximum = 2683
        url = 'https://www.urionlinejudge.com.br/judge/en/problems/view/'
        while True:
            problem_number = str(random.randint(minimum, maximum))
            if problem_number not in self.problems:
                problem = problem_dict[problem_number]
                if min_level <= problem["level"] <= max_level:
                    if problem["category"] not in prohib:
                        break
        webbrowser.open(url+str(problem_number))
        print "a level %d problem just for %s" % (int(problem["level"]), self.name)
        print url + str(problem_number)

if __name__ == "__main__":
    utils.load_dict(user_dict, 'user_dict')
    utils.load_dict(problem_dict, 'problem_dict')
    if len(sys.argv) < 4:
        print "try: python random_problem.py PROFILE_ID MIN_LEVEL MAX_LEVEL [-f]"
        exit()
    _, profile_identifier, minimum, maximum = sys.argv

    if sys.argv[-1] == '-f':
        try:
            del user_dict[profile_identifier]
        except KeyError:
            pass
    if profile_identifier in user_dict:
        user = user_dict[profile_identifier]
        print "loaded profile directly"
    else:
        user = User(profile_identifier)
        print "created user"
        user.get_info()
        print "got user info"
        user_dict[profile_identifier] = user
    user.get_problem()
    utils.save_dict(user_dict, 'user_dict')
    utils.save_dict(problem_dict, 'problem_dict')