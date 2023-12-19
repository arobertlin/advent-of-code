class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.times = []
        self.distances = []
        self.preprocess(input_list)

    def preprocess(self, input_list):
        self.times = input_list[0].split()[1:]
        self.distances = input_list[1].split()[1:]
        return

    def preprocess2(self):
        concatted_time = ""
        for val in self.times:
            concatted_time = concatted_time + val
        self.times = concatted_time

        concatted_dist = ""
        for val in self.distances:
            concatted_dist = concatted_dist + val
        self.distances = concatted_dist

    def solve1(self):
        counters = []
        for i in range(len(self.times)):
            counter = 0
            for j in range(int(self.times[i])):
                if j * (int(self.times[i]) - j) > int(self.distances[i]):
                    counter += 1
            counters.append(counter)
        prod = 1
        for val in counters:
            prod = prod * val
        return prod

    def solve2(self):
        left_cutoff = 0
        right_cutoff = 0
        self.preprocess2()
        for i in range(int(self.times)):
            if i * (int(self.times) - i) > int(self.distances):
                left_cutoff = i
                break
        for i in range(int(self.times),-1,-1):
            if i * (int(self.times) - i) > int(self.distances):
                right_cutoff = i+1
                break
        return right_cutoff - left_cutoff


if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("6_input.txt")

    answer1 = solution.solve1()
    answer2 = solution.solve2()
    print(answer1)
    print(answer2)
