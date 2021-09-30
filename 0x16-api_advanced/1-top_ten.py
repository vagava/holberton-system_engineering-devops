#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers """
import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(
        url, headers={'User-Agent': 'Va_gava'}, allow_redirects=False)
    if request.status_code != 200:
        print(None)
        return
    data = request.json()
    list_children = data['data']['children']
    for i in range(10):
        print(list_children[i]['data']['title'])
