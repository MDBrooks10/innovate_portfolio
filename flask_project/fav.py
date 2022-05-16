music_list = [
    {
        "artist": "Radiohead",
        "song name": "Paranoid Android",
        "release year": "1997",
        "genre": "Alt Rock"
    },
    {
        "artist": "The Police",
        "song name": "Message in a Bottle",
        "release year": "1979",
        "genre": "Sting"
    },
    {
        "artist": "Led Zeppelin",
        "song name": "Trampled Under Foot",
        "release year": "1975",
        "genre": "Rock"
    },
    {
        "artist": "Red Hot Chili Peppers",
        "song name": "Strip my Mind",
        "release year": "2005",
        "genre": "Rock"
    },
]

for each_dict in music_list:
    print("\n")
    for dict_value in each_dict.values():
        print(dict_value)