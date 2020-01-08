string = 'paypalishiring'
numlevels = 4


class zigzag():
    def __init__(self):
        pass

    matrix = {}
    counter = 0
    travelator = 0

    def zig(self, string, numlevels):
        for level in range(numlevels):
            line = zigzag.matrix[level]
            line[zigzag.travelator] = string[zigzag.counter]
            zigzag.counter += 1

    def zag(self, string, numlevels):
        levelcorrection = 2
        for level in range(numlevels - levelcorrection, 0, -1):
            line = zigzag.matrix[level]
            zigzag.travelator += 1
            line[zigzag.travelator] = string[zigzag.counter]
            zigzag.counter += 1

    def zoog(self, string, numlevels):
        totalchars = ''
        for level in range(numlevels):
            zigzag.matrix[level] = '-' * len(string)
        while zigzag.counter < len(string):
            self.zig(string, numlevels)
            self.zag(string, numlevels)
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
