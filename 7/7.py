from functools import cmp_to_key
from collections import Counter

card_values_1 = {"A": 14,
                 "K": 13,
                 "Q": 12,
                 "J": 11,
                 "T": 10,
                 "9": 9,
                 "8": 8,
                 "7": 7,
                 "6": 6,
                 "5": 5,
                 "4": 4,
                 "3": 3,
                 "2": 2}

card_values_2 = {"A": 14,
                 "K": 13,
                 "Q": 12,
                 "T": 10,
                 "9": 9,
                 "8": 8,
                 "7": 7,
                 "6": 6,
                 "5": 5,
                 "4": 4,
                 "3": 3,
                 "2": 2,
                 "J": 1}


def compare_hands_1(hand1, hand2):
    for i in range(len(hand1[0])):
        result = compare_cards_1(hand1[0][i], hand2[0][i])
        if result != 0:
            return result
    return 0


def compare_hands_2(hand1, hand2):
    for i in range(len(hand1[0])):
        result = compare_cards_2(hand1[0][i], hand2[0][i])
        if result != 0:
            return result
    return 0


def compare_cards_1(card1, card2):
    if card_values_1[card1] > card_values_1[card2]:
        return 1
    if card_values_1[card1] < card_values_1[card2]:
        return -1
    return 0


def compare_cards_2(card1, card2):
    if card_values_2[card1] > card_values_2[card2]:
        return 1
    if card_values_2[card1] < card_values_2[card2]:
        return -1
    return 0


class Solution:
    def __init__(self, input_str):
        file = open(input_str, "r")
        self.input_list = file.readlines()
        file.close()
        self.high_cards = []
        self.one_pairs = []
        self.two_pairs = []
        self.three_of_a_kind = []
        self.full_house = []
        self.four_of_a_kind = []
        self.five_of_a_kind = []
        self.preprocess(self.input_list)

    def preprocess(self, input_list):
        for line in input_list:
            line_list = line.split()
            cards = line_list[0]
            bets = line_list[1]
            result = Counter(cards)
            print(result)
            single_counter = 0
            pair_counter = 0
            triple_counter = 0
            four_counter = 0
            five_counter = 0
            for key, value in result.items():
                if value == 1:
                    single_counter += 1
                elif value == 2:
                    pair_counter += 1
                elif value == 3:
                    triple_counter += 1
                elif value == 4:
                    four_counter += 1
                    break
                elif value == 5:
                    five_counter += 1
                    break

            if five_counter == 1:
                self.five_of_a_kind.append((cards, bets))

            elif four_counter == 1:
                self.four_of_a_kind.append((cards, bets))

            elif triple_counter == 1 and pair_counter == 1:
                self.full_house.append((cards, bets))

            elif triple_counter == 1 and pair_counter == 0:
                self.three_of_a_kind.append((cards, bets))

            elif pair_counter == 2:
                self.two_pairs.append((cards, bets))

            elif pair_counter == 1:
                self.one_pairs.append((cards, bets))

            else:
                self.high_cards.append((cards, bets))

        return

    def preprocess2(self, input_list):
        for line in input_list:
            line_list = line.split()
            cards = line_list[0]
            bets = line_list[1]
            result = Counter(cards)
            print(result)
            single_counter = 0
            pair_counter = 0
            triple_counter = 0
            four_counter = 0
            five_counter = 0
            j_counter = 0
            for key, value in result.items():
                if key == "J":
                    j_counter = value
                elif value == 1:
                    single_counter += 1
                elif value == 2:
                    pair_counter += 1
                elif value == 3:
                    triple_counter += 1
                elif value == 4:
                    four_counter += 1
                elif value == 5:
                    five_counter += 1

            if five_counter == 1:
                self.five_of_a_kind.append((cards, bets))

            elif four_counter == 1:
                if j_counter == 1:
                    self.five_of_a_kind.append((cards, bets))
                else:
                    self.four_of_a_kind.append((cards, bets))

            elif triple_counter == 1 and pair_counter == 1:
                self.full_house.append((cards, bets))

            elif triple_counter == 1 and pair_counter == 0:
                if j_counter == 2:
                    self.five_of_a_kind.append((cards, bets))
                elif j_counter == 1:
                    self.four_of_a_kind.append((cards, bets))
                else:
                    self.three_of_a_kind.append((cards, bets))

            elif pair_counter == 2:
                if j_counter == 1:
                    self.full_house.append((cards, bets))
                else:
                    self.two_pairs.append((cards, bets))

            elif pair_counter == 1:
                if j_counter == 3:
                    self.five_of_a_kind.append((cards, bets))
                elif j_counter == 2:
                    self.four_of_a_kind.append((cards, bets))
                elif j_counter == 1:
                    self.three_of_a_kind.append((cards, bets))
                else:
                    self.one_pairs.append((cards, bets))

            else:

                if j_counter == 4 or j_counter == 5:
                    self.five_of_a_kind.append((cards, bets))
                elif j_counter == 3:
                    self.four_of_a_kind.append((cards, bets))
                elif j_counter == 2:
                    self.three_of_a_kind.append((cards, bets))
                elif j_counter == 1:
                    self.one_pairs.append((cards, bets))
                else:
                    self.high_cards.append((cards, bets))

        return

    def solve1(self):

        score = 0
        rank = 1
        for hand in sorted(self.high_cards, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.one_pairs, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.two_pairs, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.three_of_a_kind, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.full_house, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.four_of_a_kind, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.five_of_a_kind, key=cmp_to_key(compare_hands_1)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1

        return score

    def solve2(self):
        self.high_cards = []
        self.one_pairs = []
        self.two_pairs = []
        self.three_of_a_kind = []
        self.full_house = []
        self.four_of_a_kind = []
        self.five_of_a_kind = []
        self.preprocess2(self.input_list)

        score = 0
        rank = 1
        for hand in sorted(self.high_cards, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.one_pairs, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.two_pairs, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.three_of_a_kind, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.full_house, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.four_of_a_kind, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1
        print("________")
        for hand in sorted(self.five_of_a_kind, key=cmp_to_key(compare_hands_2)):
            print(str(int(hand[1]) * rank) + " " + str(hand))
            score += (int(hand[1]) * rank)
            rank += 1

        print(rank)

        return score


if __name__ == '__main__':
    # uncomment this to test on a small subset of data
    # solution = Solution("test.txt")

    solution = Solution("7_input.txt")

    answer1 = solution.solve1()
    answer2 = solution.solve2()
    print(answer1)
    print(answer2)
