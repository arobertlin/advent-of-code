import re


class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.input_list = input_list

        self.num_dict = {"one": "1",
                         "two": "2",
                         "three": "3",
                         "four": "4",
                         "five": "5",
                         "six": "6",
                         "seven": "7",
                         "eight": "8",
                         "nine": "9"
                         }

        self.string_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    def solve2(self):
        my_sum = 0
        # for each line
        for line in self.input_list:
            my_dict = {}
            # create a dictionary where key is the index of the number in the line, and value is the number as a string
            # this is only for spelled-out numbers
            for num in self.string_nums:
                result = [m.start() for m in re.finditer(num, line)]
                for each_index in result:
                    my_dict[each_index] = self.num_dict[num]

            # update the dictionary adding numerical numbers
            first_num_str, index = self.get_first_num(line)
            my_dict[index] = first_num_str
            last_num_str, index = self.get_last_num(line)
            my_dict[index] = last_num_str

            sorted_dict = dict(sorted(my_dict.items()))
            # print(sorted_dict)

            first_digit_str = list(sorted_dict.values())[0]
            second_digit_str = list(sorted_dict.values())[-1]
            num_str = first_digit_str + second_digit_str
            num = int(num_str)
            my_sum += num
        return my_sum

    def solve1(self):
        my_sum = 0
        for line in self.input_list:
            first_digit_str, _ = self.get_first_num(line)
            second_digit_str, _ = self.get_last_num(line)
            num_str = first_digit_str + second_digit_str
            num = int(num_str)
            my_sum += num
        return my_sum

    def get_first_num(self, string):
        match = re.search(r'\d', string)
        if match:
            return match.group(), match.start()

    def get_last_num(self, string):
        match = re.search(r'\d', string[::-1])
        if match:
            return match.group(), len(string) - match.start() - 1

if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("1_input.txt")

    answer1 = solution.solve1()
    print(answer1)

    answer2 = solution.solve2()
    print(answer2)


