import urllib2
import utils
problem_dict = {}



def load_problems():
    identifier = 1001
    utils.load_dict(problem_dict, 'problem_dict')
    while True:
        try:
            problem_id = str(identifier)
            if problem_id not in problem_dict.keys():
                print identifier
                problem_html = utils.get_html("problem", problem_id=problem_id)
                if problem_html == 'ERROR':
                    break
                tmp_dict = dict()
                tmp_dict["problem_id"] = problem_id
                tmp_dict["level"] = utils.get_level_from_html(problem_html)
                tmp_dict["category"] = utils.get_category_from_html(problem_html)
                tmp_dict["title"] = utils.get_title_from_html(problem_html)
                problem_dict[problem_id] = tmp_dict
                identifier += 1
        except KeyboardInterrupt:
            break
    utils.save_dict(problem_dict, 'problem_dict')

load_problems()