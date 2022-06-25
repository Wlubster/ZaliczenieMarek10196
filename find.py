import json



def Find(q1, query):
    my_list = [+1]
    musicNumber = 1
    i = 0
    with open("search.json", "r", encoding="utf-8") as j:

        try:

            contents = json.load(j)

            for i in range(len(contents[q1.lower() + "s"]["items"])):
                if contents[q1.lower()+"s"]["items"][i]["name"] == query.title() or contents[q1.lower()+"s"]["items"][i]["name"] == query.lower() or contents[q1.lower()+"s"]["items"][i]["name"] == query.upper():
                    print("Name: " + contents[q1.lower()+"s"]["items"][i]["name"])

                    if q1.lower()+"s" == "artists":
                        print("Genres: " + str(contents[q1.lower() + "s"]["items"][i]["genres"]))
                        print("Popularity: " + str(contents[q1.lower() + "s"]["items"][i]["popularity"]))

                        try:
                            my_list.append(contents[q1.lower() + "s"]["items"][i]["external_urls"]["spotify"])
                            print("Artist's number: " + str(musicNumber))
                            print("Artist's site link: " + contents[q1.lower() + "s"]["items"][i]["external_urls"]["spotify"])
                        except(TypeError):
                            print("Ten Artysta nie ma strony!")
                        finally:
                            musicNumber +=1

                    if q1.lower()+"s" == "tracks":
                        #print(list(contents.keys()))
                        print("Type: " + contents[q1.lower() + "s"]["items"][i]["type"])
                        for a in range(len(contents[q1.lower() + "s"]["items"][i]["artists"])):
                            if a == 0:
                                print("Artist: " + contents[q1.lower() + "s"]["items"][i]["album"]["artists"][a]["name"])
                                #print(str(a) + "Au")
                            else:
                                print("Feat " + str(a) + ": " + contents[q1.lower() + "s"]["items"][i]["artists"][a]["name"])
                                #print(a)
                        try:
                            my_list.append(contents[q1.lower() + "s"]["items"][i]["preview_url"])
                            print("Music's Number: " + str(musicNumber))
                            print("Preview url: " + contents[q1.lower() + "s"]["items"][i]["preview_url"])
                        except TypeError:
                            print("Nie ma podglądu!")
                        finally:
                            musicNumber += 1
                    print("Popularity: " + str(contents[q1.lower()+"s"]["items"][i]["popularity"]))


                    print(contents[q1.lower()+"s"]["items"][i]["uri"])
                    print("[---------------------------------------------]")



        except IndexError:
            print("")

        finally:
            j.close()

    if q1 == "Track" or "Artist":
        if q1 == "Track":
            musicP = int(input("Music's Number (0 to quit): "))
        elif q1 == "Artist":
            musicP = int(input("Artist's Number (0 to quit): "))
        try:
            if musicP== 0:
                print("Quiting...")
                exit()
            elif my_list[musicP]:
                return my_list[musicP]
                #driver = webdriver.Chrome()
                #driver.get(my_list[musicP])
            elif not my_list[musicP]:
                print("Ta muzyka nie ma podglądu!")
                exit()
        except(IndexError):
            print("Takiego numeru nie ma w spisie!")