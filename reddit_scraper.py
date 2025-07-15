import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="reddit_user_persona_script"
)

def scrape_user_content(username, limit=20):
    user = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=limit):
            posts.append(f"[POST] {submission.title}\n{submission.selftext}")
    except Exception as e:
        print(f" Could not fetch submissions: {e}")

    try:
        for comment in user.comments.new(limit=limit):
            comments.append(f"[COMMENT] {comment.body}")
    except Exception as e:
        print(f" Could not fetch comments: {e}")

    return posts + comments
