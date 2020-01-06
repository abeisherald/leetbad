string = 'paypalishungry'
numlevels = 3


class zigzag():
    def __init__(self):
        pass

    matrix = {}
    counter = 0
    travelator = 0

    def zig(self, string, numlevels):
        if not zigzag.matrix:
            for level in range(numlevels):
                zigzag.matrix[level] = ['-' for i in range(len(string))]
        for level in range(numlevels):
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
        zigzag.travelator += 1
        # print(zigzag.matrix)
        self.zig(string, numlevels)
        

    def zoog(self, string, numlevels):
        totalchars = ''
        self.zig(string, numlevels)
        for char in zigzag.matrix:
            if char != '-' and isinstance(char, str):
                totalchars += char
            else:
                continue
        return totalchars


zigzag().zoog(string, numlevels)
