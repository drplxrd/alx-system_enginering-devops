#!/usr/bin/python3
"""
Script to call the Reddit API and print out the titles of the first 10 posts
Listed for a provided subreddit
"""

import requests

def top_ten(subreddit):
    "Function to print out the titles of the first 10 posts listed for a given subreddit"
    r = requests.get("https://reddit.com/r/{}.json?sort=hot&limit=10".format(subreddit), headers={"User-Agent": "custom"})
    
    if (r.status_code != 200):
        for i in r.json().get("data").get("children"):
            print(i.get("data").get("title"))
        
    else:
        print("None")