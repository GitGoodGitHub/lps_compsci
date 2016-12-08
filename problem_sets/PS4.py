print('Welcome to PumaPix!')
print('Enter your 5 favoriteTV shows.')
TV_Shows = []
shows = 0

while shows < 5:
        print('Enter a show name:')
        fav_shows = raw_input()
        shows = shows + 1
        TV_Shows.append(fav_shows)

print("Ok, here's  what you entered")
print(TV_Shows)

print("We've added a couple important ones.")
TV_Shows.append('Breaking Bad')
TV_Shows.append('The Wire')
TV_Shows.sort()

num = 0
for shows in TV_Shows:
        num = num + 1
        print(str(num) + '.' + shows)
