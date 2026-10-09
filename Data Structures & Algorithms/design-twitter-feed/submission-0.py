class Twitter:
    # Okay let's try again with the hint
    # 1. Data Structue
    # Use hashmap to store userID -> followees and userId -> Tweet feeds
    # Hashmap 1: Followee
    # {userID: set of followees, so unique followees (store ids)}
    # Hashmap 2: Tweets
    # {userID: [(count, tweetID)]}, where count tracks order of tweets and increment 1 each time a tweet is posted.
    # This way when we run postTweet, we just append (count, tweetID) to tweets[userID]
    # follow(): extend tweets[followeeID] -> tweets[followerID]
    # unfollow(): not sure
    # getNewsFeed(): use max heap to heappush values of tweets[userID] and heappop if list exceeds 10

    # Clarification: Can only follow or unfollow one at a time?

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        

       


        
