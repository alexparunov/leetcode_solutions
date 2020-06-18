"""
https://leetcode.com/problems/design-twitter/

"""
import collections
from typing import List


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = collections.defaultdict(set)
        self.tweets = collections.defaultdict(set)
        self.tweet_num = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId].add((tweetId, self.tweet_num))
        self.tweet_num += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        # own tweets
        news_feed = self.tweets[userId].copy()

        for followeeId in self.users[userId]:
            news_feed.update(self.tweets[followeeId])

        news_feed = list(news_feed)
        news_feed.sort(key=lambda x: x[1], reverse=True)

        tweets = [tweetId for tweetId, _ in news_feed]
        return tweets[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.users[followerId].discard(followeeId)
