# Lauren Holley
# 1861058
roster = {}
count = 1
for player in range(5):
    player_jersey = int(input("Enter player {}'s jersey number:".format(count)))
    print()
    player_rate = int(input("Enter player {}'s rating:".format(count)))
    count += 1
    print()
    print()
    roster[player_jersey] = player_rate
roster_items = roster.items()
sorted_players = sorted(roster_items)
print("ROSTER")
for jersey, rating in sorted_players:
    print("Jersey number: {}, Rating: {}".format(jersey, rating))
print()
print("MENU")
print("a - Add player")
print("d - Remove player")
print("u - Update player rating")
print("r - Output players above a rating")
print("o - Output roster")
print("q - Quit")
print()
user_choice = input("Choose an option:")
print()
while user_choice != 'q':
    if user_choice == 'o':
        print("ROSTER")
        roster_items = roster.items()
        sorted_players = sorted(roster_items)
        for jersey, rating in sorted_players:
            print("Jersey number: {}, Rating: {}".format(jersey, rating))
        print()

    if user_choice == 'a':
        player_jersey = int(input("Enter a new player's jersey number:"))
        print()
        player_rate = int(input("Enter a new player's rating:"))
        roster[player_jersey] = player_rate
        print()

    if user_choice == 'd':
        key = int(input("Enter a jersey number:"))
        if key in roster:
            del roster[key]

    if user_choice == 'u':
        update_num = int(input("Enter a jersey number:"))
        print()
        new_rating = input("Enter a new rating for player:")
        if update_num in roster:
            roster[update_num] = new_rating

    if user_choice == 'r':
        rating_above = int(input("Enter a rating:"))
        print("ABOVE {}".format(rating_above))
        for jersey, rating in sorted_players:
            if rating > rating_above:
                print("Jersey number: {}, Rating: {}".format(jersey, rating))
        print()

    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    user_choice = input("Choose an option:")
    print()
