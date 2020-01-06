class Solution:
    def myAtoi(self, s):
        int_dict = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        sign_flag = False
        neg_flag = False
        int_list = []


        for char in s:
            if char in int_dict or char == '-':
                # check to see if first time seeing '-'
                if char == '-':
                    if sign_flag == True and bool(int_list) == False:
                        return 0
                    else:
                        # check if int list is full yet. If full, break. If not, set negative flag
                        if int_list:
                            return self.whatnow(int_list, neg_flag)
                        else:
                            neg_flag = True
                            sign_flag = True
                # convert and save to int list
                else:
                    int_list.append(int_dict[char])
            elif char == ' ':
                # if int list is empty, continue. Otherwise, break and return int list
                if sign_flag == True and bool(int_list) == False:
                    return 0
                elif sign_flag == True or int_list:
                    return self.whatnow(int_list, neg_flag)
                else:
                    continue
            elif char == '+':
                # if int list is empty, continue. Otherwise, break and return int list
                if sign_flag == True and bool(int_list) == False:
                    return 0
                elif bool(sign_flag) == True and bool(int_list) == True:
                    return self.whatnow(int_list, neg_flag)
                elif bool(sign_flag) == False and int_list:
                    return self.whatnow(int_list, neg_flag)
                else:
                    sign_flag = True
                    continue
            else:
                # return 0 or current int list
                if int_list:
                    return self.whatnow(int_list, neg_flag)
                else:
                    return 0
        return self.whatnow(int_list, neg_flag)

    def whatnow(self, L, neg_flag):
        # stripping the chars out of the list
        stripped_int = 0
        for v in L:
            stripped_int *= 10
            stripped_int += v
        # Determing negativity
        if neg_flag == True:
            stripped_int = -1*stripped_int
        # final test to ensure it doesnt overspill the bounds
        if stripped_int <= (2 ** 31 - 1) and stripped_int >= (-2 ** 31 - 1):
            return stripped_int
        elif stripped_int <= (-2 ** 31 - 1):
            return (-2 ** 31)
        else:
            return (2 ** 31)

print(Solution().myAtoi('+8'))
