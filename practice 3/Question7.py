followers1 = input("Enter followers of User 1 (space separated): ").split()
followers2 = input("Enter followers of User 2 (space separated): ").split()

set1 = set(followers1)
set2 = set(followers2)

common_followers = set1.intersection(set2)

print("Common Followers:", common_followers)