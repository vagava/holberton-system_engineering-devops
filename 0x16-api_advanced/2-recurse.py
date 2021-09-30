#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ function that queries the Reddit API and
    returns the number of subscribers"""
    # url configuration
    if after == "":
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit, after)
    # make request
    request = requests.get(
        url, headers={'User-Agent': 'Va_gava'}, allow_redirects=False)
    if request.status_code != 200:
        return 0
    data = request.json()
    keys = data['data'].keys()
    if 'after' in keys and data['data']['after'] is not None:
        print("un nivel mas")
        hot_list.extend(recurse(subreddit, after=data['data']['after']))
    list_children = data['data']['children']
    for i in range(len(list_children)):
        hot_list.append(list_children[i]['data']['title'])
    return hot_list
