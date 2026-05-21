class Twitter:

    def __init__(self):
        self.tweets = []
        self.relations = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.relations:
            self.relations[userId] = set([userId])

        heapq.heappush(self.tweets, [-len(self.tweets), tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.relations:
            self.relations[userId] = set([userId])

        tweets = self.tweets.copy()
        res = [] 

        while len(res) < 10 and tweets:
            p = heapq.heappop(tweets)

            if p[2] in self.relations[userId]:
                res.append(p[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.relations:
            self.relations[followerId] = set([followerId])
        self.relations[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.relations[followerId].discard(followeeId)
        
