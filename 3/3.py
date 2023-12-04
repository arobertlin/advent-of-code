import re

class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.input_list = input_list

    '''
    To solve this problem, iterate through all the rows. For each row, check if the numbers are adjacent
    to the symbols in the above row, current row, and row below. If they are adjacent, add the number to
    the sum.
    '''
    def solve1(self):
        my_sum = 0
        top_line_symbol_indices = []
        middle_line_symbol_indices = []
        middle_line_nums = []
        middle_line_num_indices = []

        # process all lines except the last line
        for line in self.input_list:
            # parse line into list of nums
            nums = re.findall(r'\d+', line)
            # get indices into list of tuples [(0,3), (5,8)], where each tuple is the start and end index of a number
            indices = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
            # get symbols into list of tuples [(0,3), (5,8)], where each tuple is the start and end index of a symbol
            symbol_indices = [(m.start(0), m.end(0)) for m in re.finditer(r'[^\.0-9\n]+', line)]

            # extend symbol indices to valid overlap window
            symbol_indices = self.preprocess_symbol_indices(symbol_indices)

            # use set to dedup numbers next to multiple symbols
            valid_nums = set()
            # compare to top
            valid_nums.update(self.overlap(top_line_symbol_indices, middle_line_num_indices))
            # compare to same line
            valid_nums.update(self.overlap(middle_line_symbol_indices, middle_line_num_indices))
            # compare to bottom
            valid_nums.update(self.overlap(symbol_indices, middle_line_num_indices))

            for num_index in valid_nums:
                my_sum += int(middle_line_nums[num_index])

            top_line_symbol_indices = middle_line_symbol_indices
            middle_line_symbol_indices = symbol_indices
            middle_line_nums = nums
            middle_line_num_indices = indices

        final_row_valid_nums = set()
        final_row_valid_nums.update(self.overlap(top_line_symbol_indices, middle_line_num_indices))
        final_row_valid_nums.update(self.overlap(middle_line_symbol_indices, middle_line_num_indices))

        for num_index in final_row_valid_nums:
            my_sum += int(middle_line_nums[num_index])

        return my_sum

    def overlap(self, symbol_indices, middle_line_num_indices):
        index_set = set()
        for i in range(len(middle_line_num_indices)):
            # if overlap
            if symbol_indices:
                for each_symbol_index in symbol_indices:
                    if each_symbol_index[0] <= middle_line_num_indices[i][0] <= each_symbol_index[1]:
                        index_set.add(i)
                    if each_symbol_index[0] <= middle_line_num_indices[i][1] - 1 <= each_symbol_index[1]:
                        index_set.add(i)
        return index_set

    def preprocess_symbol_indices(self, symbol_indices):
        new_symbol_indices = []
        for old_tuple in symbol_indices:
            new_tuple = (max(0, old_tuple[0] - 1), old_tuple[1])
            new_symbol_indices.append(new_tuple)
        return new_symbol_indices

    def solve2(self):
        my_sum = 0
        middle_line_symbol_indices = []
        top_line_num_indices = []
        middle_line_num_indices = []
        top_line_nums = []
        middle_line_nums = []

        top_line = ""
        middle_line = ""

        # process all lines except the last line
        for line in self.input_list:
            # parse line into list of nums
            nums = re.findall(r'\d+', line)
            # get indices into list of tuples [(0,3), (5,8)], where each tuple is the start and end index of a number
            indices = [(m.start(0), m.end(0)) for m in re.finditer(r'\d+', line)]
            # get symbols into list of tuples [(0,3), (5,8)], where each tuple is the start and end index of a symbol
            symbol_indices = [(m.start(0), m.end(0)) for m in re.finditer(r'[*]', line)]

            # extend symbol indices to valid overlap window
            symbol_indices = self.preprocess_symbol_indices(symbol_indices)

            for symbol in middle_line_symbol_indices:
                top_count, top_iter_prod = self.overlap2(symbol, top_line_num_indices, top_line_nums)
                mid_count, mid_iter_prod = self.overlap2(symbol, middle_line_num_indices, middle_line_nums)
                bottom_count, bottom_iter_prod = self.overlap2(symbol, indices, nums)
                if top_count + mid_count + bottom_count == 2:
                    my_sum = my_sum + (top_iter_prod * mid_iter_prod * bottom_iter_prod)

            middle_line_symbol_indices = symbol_indices

            top_line_num_indices = middle_line_num_indices
            middle_line_num_indices = indices

            top_line_nums = middle_line_nums
            middle_line_nums = nums

            top_line = middle_line
            middle_line = line

        # processing last line
        for symbol in middle_line_symbol_indices:
            top_count, top_iter_prod = self.overlap2(symbol, top_line_num_indices, top_line_nums)
            mid_count, mid_iter_prod = self.overlap2(symbol, middle_line_num_indices, middle_line_nums)
            if top_count + mid_count == 2:
                my_sum += (top_iter_prod * mid_iter_prod)

        return my_sum

    def overlap2(self, symbol_index, num_indices, nums):
        prod = 1
        count = 0
        if num_indices:
            for i in range(len(num_indices)):
                if symbol_index[0] <= num_indices[i][0] <= symbol_index[1]:
                    prod = prod * int(nums[i])
                    count += 1
                elif symbol_index[0] <= num_indices[i][1] - 1 <= symbol_index[1]:
                    prod = prod * int(nums[i])
                    count += 1
        return count, prod



if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("3_input.txt")

    answer1 = solution.solve1()
    answer2 = solution.solve2()
    print(answer1)
    print(answer2)

