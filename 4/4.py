class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        input_list = file.readlines()
        file.close()
        self.input_list = input_list
        self.clean_input = []

    def solve1(self):
        my_sum = 0
        for game in self.input_list:
            # get
            x = game.index(":") + 2
            game = game[x:]
            scratchers = game.split("|")
            winners = scratchers[0]
            winners = set(winners.split())
            # print(winners)
            my_cards = scratchers[1]
            my_cards = set(my_cards.split())
            # print(my_cards)

            overlap = winners & my_cards
            # print(len(overlap))

            if len(overlap) > 0:
                my_sum += 2 ** (len(overlap) - 1)
        return my_sum

    def solve2(self):
        card_count = 0
        card_counter_dict = {}
        # initialize card_counter_dict and preprocess input
        for i in range(len(self.input_list)):
            card_counter_dict[i] = 1
            game = self.input_list[i]
            x = game.index(":") + 2
            game = game[x:]

            scratchers = game.split("|")
            winners = scratchers[0]
            winners = set(winners.split())
            my_cards = scratchers[1]
            my_cards = set(my_cards.split())
            self.clean_input.append([winners, my_cards])

        # for every game
        for i in range(len(self.clean_input)):
            # for each copy of the game
            for j in range(card_counter_dict.get(i)):
                card_count += 1
                winners = self.clean_input[i][0]
                my_cards = self.clean_input[i][1]
                overlap = winners & my_cards
                # for each overlap, update the card_counter_dict to have relevant copies of cards
                for k in range(len(overlap)):
                    if i+k+1 < len(self.clean_input):
                        card_counter_dict[i+k+1] = card_counter_dict[i+k+1] + 1
        return card_count



if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("4_input.txt")

    answer1 = solution.solve1()
    answer2 = solution.solve2()
    print(answer1)
    print(answer2)

