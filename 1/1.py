import re


class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.input_list = input_list

    def solve(self):
        my_sum = 0
        i = 0
        for line in self.input_list:
            first_digit_str = self.get_first_num(line)
            second_digit_str = self.get_last_num(line)
            num_str = first_digit_str + second_digit_str
            num = int(num_str)
            my_sum += num
        return my_sum

    def get_first_num(self, string):
        match = re.search(r'\d', string)
        if match:
            return match.group()
        else:
            raise

    def get_last_num(self, string):
        match = re.search(r'\d', string[::-1])
        if match:
            return match.group()
        else:
            raise

if __name__ == '__main__':
    solution = Solution("1_input.txt")
    answer = solution.solve()
    print(answer)


