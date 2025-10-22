# Design Twitter

# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

# Users and tweets are uniquely identified by their IDs (integers).

# Implement the following methods:

#     Twitter() Initializes the twitter object.
#     void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
#     List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
#     void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
#     void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.

# Example 1:

# Input:
# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   // User 1 unfollows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].

# Constraints:

#     1 <= userId, followerId, followeeId <= 100
#     0 <= tweetId <= 1000

import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweet_map[userId].append([self.time, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        # get followed users and self
        users = set(self.follow_map[userId])
        users.add(userId)

        # get 1 latest tweets from self and followed users
        users_tweets = []
        for uid in users:
            tweets = self.tweet_map[uid]
            if tweets:
                idx = len(tweets) - 1           # find the idx of latest tweet
                t, tid = tweets[idx]            # grab the latest tweet
                heapq.heappush(users_tweets, (-t, uid, idx, tid))


        feed = []
        while users_tweets and len(feed) < 10:
            t, user_id, idx, tweet_id = heapq.heappop(users_tweets)
            feed.append(tweet_id)

            if idx - 1 >= 0:
                t2, tid2 = self.tweet_map[user_id][idx - 1]
                heapq.heappush(users_tweets, (-t2, user_id, idx - 1, tid2))
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)

