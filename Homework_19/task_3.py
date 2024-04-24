friendships = {}

print("Enter friendships : 'Friend1 - Friend2' or FINISH")
while True:
    friendship = input("Friendship: ")
    if friendship == 'FINISH':
        break

    friend1, friend2 = friendship.split(' - ')
    friendships[friend1] = friendships.get(friend1, []) + [friend2]
    friendships[friend2] = friendships.get(friend2, []) + [friend1]

print("Friendships:")
for friend, friends_list in friendships.items():
    print(f"{friend} - {', '.join(friends_list)}")


######### VERSION 2 (using def) ##############

def input_friendships():
    friendships = {}

    print("Enter friendships : 'Friend1 - Friend2' or FINISH")
    while True:
        friendship = input("Friendship: ")
        if friendship == 'FINISH':
            break

        friend1, friend2 = friendship.split(' - ')
        friendships[friend1] = friendships.get(friend1, []) + [friend2]
        friendships[friend2] = friendships.get(friend2, []) + [friend1]

    return friendships

def print_friendships(friendships):
    print("Friendships:")
    for friend, friends_list in friendships.items():
        print(f"{friend} - {', '.join(friends_list)}")

def main():
    friendships_dict = input_friendships()
    print_friendships(friendships_dict)

if __name__ == "__main__":
    main()

