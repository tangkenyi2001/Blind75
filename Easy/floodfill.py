class Solution:
    def floodFill(self, image, sr, sc, color) :
        ori=image[sr][sc]
        def dfs(sr,sc,ori,color):
            if image[sr][sc]!=ori:
                return
            else:
                image[sr][sc]=color
                if sr>0:
                    dfs(sr-1,sc,ori,color)
                if sr<len(image)-1:
                    dfs(sr+1,sc,ori,color)
                if sc>0:
                    dfs(sr,sc-1,ori,color)
                if sc<len(image[0])-1:
                    dfs(sr,sc+1,ori,color)
        if ori!=color:
            dfs(sr,sc,ori,color)
        return image