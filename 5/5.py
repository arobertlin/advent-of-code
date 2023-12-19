class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.seeds = []
        self.maps = {}
        self.preprocess(input_list)

    '''
    Iterate through the data. Populate self.seeds as a list.
    Populate self.maps with key = name of map, value = list[list], where the outer look is each mapping
    and the inner loop contains dest, source, len for each mapping.
    '''

    def preprocess(self, input_list):

        # parse seeds
        x = input_list[0].index(":") + 2
        seeds = input_list[0][x:].split()
        self.seeds = seeds

        mappings = []
        key = ""
        # fill each map as nested lists
        for line in input_list[2:]:

            # get name of the map
            if ":" in line:
                key = line.split()[0]

            # add each dest, source, len as a list inside the mappings list
            elif not line.isspace():
                mappings.append(line.split())

            # set maps dict with name and list[list]
            else:
                self.maps[key] = mappings
                mappings = []

        # add final mapping
        self.maps[key] = mappings
        return

    def preprocess2(self):
        new_seeds = []
        for i in range(int(len(self.seeds) / 2)):
            start = int(self.seeds[2 * i])
            length = int(self.seeds[2 * i + 1])
            new_seeds.append((start, start + length - 1))
        self.seeds = new_seeds

    def solve1(self):
        seeds = []
        for seed in self.seeds:
            mapped_seed = int(seed)
            for _, mappings in self.maps.items():
                # check if the value is in each mapping range for each map
                # if the mapping is found, break out of the current map and move to the next map
                for each_map in mappings:
                    src = int(each_map[1])
                    dest = int(each_map[0])
                    range = int(each_map[2])
                    if src <= mapped_seed < (src + range):
                        mapped_seed += dest - src
                        break

            seeds.append(mapped_seed)
        return min(seeds)

    '''
    Brute Force is inefficient, and would do irreparable harm to my new laptop. I decided to optimize
    and map the ranges instead of individual seeds.
    
    This first preprocesses the seeds and stores them as tuples of start and end, e.g. 10, 10 = (10,19).
    For each seed, it processes through each set of maps. Because there are multiple mappings for each
    map, it uses the list next_map_map to store the already-processed mappings. Any unmapped seed ranges
    are passed to the next map in the same mapping using the next_line_map list.
    
    After all mappings within a single map are processed, the output seed ranges from the previous map
    become the input seed ranges to the next map. The minimum is calculated from the seed ranges after
    all the mappings have finished.
    '''

    def solve2(self):
        self.preprocess2()

        global_min = float('inf')
        for seed_tuple in self.seeds:
            old_map = []
            next_line_map = []
            next_map_map = []
            old_map.append(seed_tuple)
            for _, mappings in self.maps.items():
                for each_map in mappings:
                    while len(old_map) > 0:
                        my_tuple = old_map.pop(0)
                        seed_start = my_tuple[0]
                        seed_end = my_tuple[1]

                        src = int(each_map[1])
                        dest = int(each_map[0])
                        range = int(each_map[2])

                        # scenario 1: no overlap at all
                        if seed_end < src or seed_start >= src + range:
                            if (seed_start, seed_end) not in next_line_map:
                                next_line_map.append((seed_start, seed_end))

                        # scenario 2: overlap from below
                        elif seed_start < src < seed_end < src + range:
                            next_line_map.append((seed_start, src - 1))
                            next_map_map.append((dest, seed_end + dest - src))

                        # scenario 3: overlap from below to above
                        elif seed_start < src < (src + range) <= seed_end:
                            next_line_map.append((seed_start, src - 1))
                            next_map_map.append((dest, dest + range - 1))
                            next_line_map.append(((dest + range + (src - dest)), seed_end))

                        # scenario 4: perfect overlap
                        elif src == seed_start and (src + range - 1) == seed_end:
                            next_map_map.append((seed_start + (dest - src), dest + range - 1))

                        # scenario 5: overlap from above
                        elif src < seed_start < (src + range) < seed_end:
                            next_map_map.append((seed_start + (dest - src), dest + range - 1))
                            next_line_map.append(((dest + range + (src - dest)), seed_end))

                        # scenario 6: overlap is contained within window
                        elif src < seed_start < seed_end < (src + range):
                            next_map_map.append((seed_start + (dest - src), seed_end + (dest - src)))

                    old_map = next_line_map.copy()
                    next_line_map = []
                old_map = old_map.copy() + next_map_map.copy()
                next_line_map = []
                next_map_map = []

            my_min = float('inf')
            for tuple in old_map:
                if tuple[0] < my_min:
                    my_min = tuple[0]

            if my_min < global_min:
                global_min = my_min

        return global_min


if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("5_input.txt")

    answer1 = solution.solve1()
    answer2 = solution.solve2()
    print(answer1)
    print(answer2)
