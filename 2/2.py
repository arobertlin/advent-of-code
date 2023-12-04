class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.input_list = input_list

        self.max_red = 12
        self.max_green = 13
        self.max_blue = 14

    def solve1(self):
        game_number = 1
        sum = 0
        for game in self.input_list:
            valid = True
            # get
            x = game.index(":") + 2
            game = game[x:]
            trial_array = game.split(";")
            for trial in trial_array:
                count_and_ball = trial.split(",")
                for each in count_and_ball:
                    stripped = each.strip()
                    count_ball_array = stripped.split()
                    count = count_ball_array[0]
                    color = count_ball_array[1]

                    if color == "red" and int(count) > self.max_red:
                        valid = False
                    elif color == "green" and int(count) > self.max_green:
                        valid = False
                    elif color == "blue" and int(count) > self.max_blue:
                        valid = False
            if valid:
                print("Game Number " + str(game_number) + ": Valid")
                sum += game_number
            else:
                print("Game Number " + str(game_number) + ": Not Valid")

            game_number += 1

        return sum

    def solve2(self):
        my_sum = 0
        game_number = 1
        for game in self.input_list:
            game_max_red = 0
            game_max_green = 0
            game_max_blue = 0
            x = game.index(":") + 2
            game = game[x:]
            trial_array = game.split(";")
            for trial in trial_array:
                count_and_ball = trial.split(",")
                for each in count_and_ball:
                    stripped = each.strip()
                    count_ball_array = stripped.split()
                    count = int(count_ball_array[0])
                    color = count_ball_array[1]

                    if color == "red" and count > game_max_red:
                        game_max_red = count
                    elif color == "green" and count > game_max_green:
                        game_max_green = count
                    elif color == "blue" and count > game_max_blue:
                        game_max_blue = count
            power = game_max_red * game_max_green * game_max_blue
            my_sum += power
            print("Game Number " + str(game_number) + ": " + str(power))
            game_number += 1
        return my_sum



if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("2_input.txt")

    answer1 = solution.solve1()
    answer2 = solution.solve2()
    print(answer1)
    print(answer2)

