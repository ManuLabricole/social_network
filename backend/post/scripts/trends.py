import os
import sys
import django
import re
from collections import Counter


sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
print(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from post.models import Post, Trend


def compute_top_hashtags():
    # Fetch all post contents
    posts = Post.objects.all().values_list("body", flat=True)

    # Extract hashtags from each post
    hashtags = [
        hashtag.lower().replace(".", "")
        for post in posts
        for hashtag in re.findall(r"#(\w+)", post)
    ]

    # Compute the ten most frequent hashtags
    top_hashtags = Counter(hashtags).most_common(5)

    return top_hashtags


def create_trend_model():
    print("CALLED")
    top_hashtags = compute_top_hashtags()
    trends = Trend.objects.all()
    for trend in trends:
        trend.delete()
        print("Trend deleted")

    for top_hashtag in top_hashtags:
        trend = Trend(hashtag=top_hashtag[0], count=top_hashtag[1])
        trend.save()
