def find_missing_letter(chars):
    alphabet = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26} 
    charnum = []
    for char in chars:
        charnum.append(alphabet[char])
    for num in charnum:
        for nextnum in charnum[charnum.index(num) + 1:]: 
            if nextnum != (num + 1):
                return list(alphabet.keys())[list(alphabet.values()).index(num + 1)]
            else:
                break

print(find_missing_letter(['a', 'b', 'c', 'd', 'f', 'g']))
