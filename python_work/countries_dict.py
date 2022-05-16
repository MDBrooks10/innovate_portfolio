countries_dict = {
    "U.K.":"London",
    "France":"Paris",                                   #   Dictionary for list of
    "Germany":"Berlin",                                 #       countries and their capital cities
    "Spain":"Madrid",
    "Italy":"Rome",
}

countries_dict.setdefault("Denmark","Copenhagen")       #   Added another two
countries_dict.setdefault("Norway", "Oslo")             #       entries to the dictionary

print(countries_dict.items())                           #   Print as items 
                                                        #       so that it's easier to visualise
countries_dict["U.K."] = "English"
countries_dict["France"] = "French"
countries_dict["Germany"] = "German"                    #   Dictionary updated to store 
countries_dict["Spain"] = "Spanish"                     #       info on languages spoken and not capital cities
countries_dict["Italy"] = "Italian"
countries_dict["Denmark"] = "Danish"
countries_dict["Norway"] = "Norwegian"

print(countries_dict.items())