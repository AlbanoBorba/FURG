import json
from requests_oauthlib import OAuth1Session
import time

CONSUMER_KEY = 'S9gZt34myOxtb4y3Xol4viQl5'
CONSUMER_SECRET = 'm7UTm5kg2ijMYOx4s2F0AA3lQ4fIxsQmUZaQiFHsBq3axjxzH8'
ACCESS_TOKEN = '59472114-0gh1hw0qfvWz8KNhs3pYJYYo42KUM2FVAxnm6ZC75'
ACCESS_SECRET = 'Bas7sKgVgz47L5IRwimrlcfPyuGPC8sEghq8Jj7utl4ws'

session = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

base_url = "https://api.twitter.com/1.1/"

def getUsernames(base_user):
    next_cursor = "-1"
    total = 0
    followers = []
    names_list = []
    while total < 900:
        try:
            print total
            response = session.get(base_url + "followers/list.json?screen_name=%s&cursor=%s" % (base_user, next_cursor))
            full = json.loads(response.content)
            followers += full["users"]
            next_cursor = full["next_cursor_str"]
            total += len(full["users"])
        except KeyError:
            print "waiting 3min"
            time.sleep(180)
    for user in followers:
        names_list.append(user["screen_name"])
    return names_list

def getUserInfo(user):
    response = session.get(base_url + "users/show.json?screen_name=%s" % user)
    info = json.loads(response.content)
    return info["screen_name"], info["followers_count"], info["friends_count"], info["statuses_count"]

def followersToDataset(names_list):
    dataset = []
    for user in names_list:
        print user
        try:
            info = getUserInfo(user)
            dataset.append(info)
        except KeyError:
            pass
    return dataset

def main():
    base_user = raw_input()
    names = getUsernames(base_user)
    dataset = followersToDataset(names)

    with open("dataset", "w") as f:
        for user in dataset:
            for item in user:
                f.write(str(item) + " ")
            f.write("\n")

if __name__ == "__main__":
    main()
