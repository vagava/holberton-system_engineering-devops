#!/usr/bin/python3
""" function that queries the Reddit API and
returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and
    returns the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(
        url, headers={'User-Agent': 'Va_gava'}, allow_redirects=False)
    if request.status_code != 200:
        return 0
    else:
        data = request.json()
        return data['data']["subscribers"]
