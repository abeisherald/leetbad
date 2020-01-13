heck = 'paypalishiringnottoday'
gogo = 5


class zigzag:

    matrix = {}
    counter = 0
    travelator = 0

    def zig(self, string, numlevels):
        for level in range(numlevels):
            if zigzag.counter < len(string):
                line = zigzag.matrix[level]
                line[zigzag.travelator] = string[zigzag.counter]
                zigzag.counter += 1

        

    def zag(self, string, numlevels):
        levelcorrection = 2
        for level in range(numlevels - levelcorrection, 0, -1):
            if zigzag.counter < len(string):
                line = zigzag.matrix[level]
                zigzag.travelator += 1
                line[zigzag.travelator] = string[zigzag.counter]
                zigzag.counter += 1
        zigzag.travelator += 1

        

    def zoog(self, string, numlevels):
        totalchars = ''
        for level in range(numlevels): 
            zigzag.matrix[level] = ['-'] * (len(string) // 2)
        while zigzag.counter < len(string):
            self.zig(string, numlevels)
            self.zag(string, numlevels)
        for line in list(zigzag.matrix.values()):
            for char in line:
                if char != '-':
                    totalchars += char
        for line in list(zigzag.matrix.values()):
            print(line)
        return totalchars


print(zigzag().zoog(heck, gogo))
