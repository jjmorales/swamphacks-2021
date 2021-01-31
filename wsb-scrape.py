import praw
import config
import csv
import pandas as pd

##################
# reddit scrape #
##################
# https://towardsdatascience.com/scraping-reddit-data-1c0af3040768

reddit = praw.Reddit(client_id=config.CLIENT_ID, client_secret=config.CLIENT_SECRET, user_agent=config.USER_AGENT)


wsb = reddit.subreddit('wallstreetbets').hot(limit=15)
posts = []

for post in wsb:
    post.comments.replace_more(limit=0)
    all_comments = post.comments.list()
    scraped_comments = []
    for comment in all_comments:
        scraped_comments.append(comment.body)

    posts.append([post.title, post.score, post.id, post.url, post.selftext, post.created, post.num_comments, scraped_comments])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'url', 'body', 'created','comments_count', 'comments_body'])

posts.to_csv(r'/Users/raulsalazar/Downloads/swampHacks/posts.csv')
