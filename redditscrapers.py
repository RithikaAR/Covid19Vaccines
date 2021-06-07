import praw
import pandas as pd
from praw.models import MoreComments
import datetime

reddit = praw.Reddit(client_id='pm9diOFYiSsXHw',
                     client_secret='9Fv9V_8xe5gi8UpkiLro49oLgG0zSw',
                     user_agent='webscraper',
                     username='yash3277',
                     password='Yash@3277')

posts = []
subreddit = reddit.subreddit('Coronavirus')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('Coronavirus.csv', index=False)

posts = pd.read_csv('Coronavirus.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('CoronavirusComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('COVID19')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('COVID19.csv', index=False)

posts = pd.read_csv('COVID19.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('COVID19Comments.csv', index=False)

posts = []
subreddit = reddit.subreddit('CovidVaccine')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('CovidVaccine.csv', index=False)

posts = pd.read_csv('CovidVaccine.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('CovidVaccineComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('CovidVaccinated')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('CovidVaccinated.csv', index=False)

posts = pd.read_csv('CovidVaccinated.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('CovidVaccinatedComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('PfizerVaccine')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('PfizerVaccine.csv', index=False)

posts = pd.read_csv('PfizerVaccine.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('PfizerVaccineComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('modernavaccine')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('modernavaccine.csv', index=False)

posts = pd.read_csv('modernavaccine.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('modernavaccineComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('VACCINES')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('VACCINES.csv', index=False)

posts = pd.read_csv('VACCINES.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('VACCINESComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('antivax')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('antivax.csv', index=False)

posts = pd.read_csv('antivax.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('antivaxComments.csv', index=False)

posts = []
subreddit = reddit.subreddit('AntiVaxxers')
for post in subreddit.hot(limit=1000):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, datetime.datetime.fromtimestamp(post.created)])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created', 'date'])

posts.to_csv('AntiVaxxers.csv', index=False)

posts = pd.read_csv('AntiVaxxers.csv')
id_list = posts['id'].to_list()
comments=[]

for id in id_list:
    submission = reddit.submission(id=id)

    for comment in submission.comments.list():
        if isinstance(comment, MoreComments):
            continue
        comments.append([comment.body,id,datetime.datetime.fromtimestamp(comment.created)])

comments = pd.DataFrame(comments, columns=['comments','id', 'date'])
comments.to_csv('AntiVaxxersComments.csv', index=False)
