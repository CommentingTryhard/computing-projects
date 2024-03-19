def scoreboard():


    def database():
        #Guide to reading lists: L1 [0] = "N" [1] = "L" L2 [0] = "line" [1] = "timestamp" [2] = "teamid" [3] = "problemid" [4] = "inputid" [5] = "scored"
        database = [[5,5],[1,1,1,1,1,0],[2,2,1,1,1,1],[3,2,4,1,2,1],[4,3,2,1,2,0],[5,4,2,1,1,1]]
        return database
    def parameter():
        data = database()
        scorelist = []
        for o in range(len(data)-1):
            scorelist.append([])
        for i in range(5):
            score = data[i+1][5]
            scorelist[i].append(score)
            scorelist[i].append(data[i+1][1])



