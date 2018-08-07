class Solution(object):
    def func(self, image, sr, sc, oldColor, newColor): 
        rowlen = len(image)
        collen = len(image[0])
        if sr < 0 or sr >= rowlen or sc < 0 or sc >= collen: 
            return image
        thisColor = image[sr][sc]
        if thisColor != oldColor: 
            return image
        image[sr][sc] = newColor
        image = self.func(image, sr - 1, sc, oldColor, newColor)
        image = self.func(image, sr + 1, sc, oldColor, newColor)
        image = self.func(image, sr, sc - 1, oldColor, newColor)
        image = self.func(image, sr, sc + 1, oldColor, newColor)
        return image
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        ## why not using a queue??? 
        rowlen = len(image)
        collen = len(image[0])
        if sr < 0 or sr >= rowlen or sc < 0 or sc >= collen: 
            return image
        if image[sr][sc] == newColor: 
            return image
        return self.func(image, sr, sc, image[sr][sc], newColor)
        
