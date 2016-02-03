movies = ["The Holy Grail", "The Life of Brain", "The Meaning of Life"]
print(movies)

movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)
print(movies)

fav_movies = ["The Holy Grail", "The Life of Brian"]

for each_flick in fav_movies:
    print(each_flick)

count = 0
while count < len(fav_movies):
    print(fav_movies[count])
    count += 1

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
    [
        "Graham Chapman",
        ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]
    ]
]

print(movies[4][1][3])

for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

print(dir(__builtins__))

print(help(input))


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)

