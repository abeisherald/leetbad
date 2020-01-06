string = 'paypalishiring'
numlevels = 4


class zigzag():
    def __init__(self):
        pass

    matrix = {}
    counter = 0
    travelator = 0
    levelstart = 0

    def zig(self, string, numlevels):
        if not zigzag.matrix:
            for level in range(numlevels):
                zigzag.matrix[level] = ['-' for i in range(len(string))]
        for level in range(zigzag.levelstart, numlevels):
            if (zigzag.counter < len(string)):
                line = zigzag.matrix[level]
                line[zigzag.travelator] = string[zigzag.counter]
                zigzag.counter += 1
            else:
                return f'Done zig, {zigzag.matrix}'
        # print(zigzag.matrix)
        self.zag(string, numlevels)
        

    def zag(self, string, numlevels):
        levelcorrection = 2
        for level in range(numlevels - levelcorrection, -1, -1):
            if (zigzag.counter < len(string)):
                line = zigzag.matrix[level]
                zigzag.travelator += 1
                line[zigzag.travelator] = string[zigzag.counter]
                zigzag.counter += 1
            else:
                return f'Done zag, {zigzag.matrix}'
        zigzag.levelstart = 1
        # print(zigzag.matrix)
        self.zig(string, numlevels)
        

    def zoog(self, string, numlevels):
        totalchars = ''
        self.zig(string, numlevels)
        listoflines = list(zigzag.matrix.values())
        for line in listoflines:
            for char in line:
                if char != '-' and isinstance(char, str):
                    totalchars += char
                else:
                    continue
        print(zigzag.matrix)
        return totalchars


print(zigzag().zoog(string, numlevels))
