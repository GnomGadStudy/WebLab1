import os
import re

listdir = [ i for i in os.listdir() if os.path.exists(i) and os.path.isfile(i) and i[-4:]=="html"]

TAG_VIEWS = False

def get_words_dict(words):
    words_dict = dict()
    global counter
    for word in words:
        if word in BAD_TAGS:
            continue
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
        if  word in counter:
            counter[word] = counter[word] + 1
        else:
            counter[word] = 1
    
    return words_dict

BAD_TAGS =["<link/>", "<head>", "<body>", "<title>", "<meta>", "<html>"]
counter = dict()
total_count = 0
for i in listdir:
    with open(i,"r",encoding="UTF-8") as f:
        text = f.readlines()
        text = '\n'.join(text)
        print("File:",i)
        solo_tags = re.findall("<[a-z]* .*\/>",text)
        new_solo_tags = list()
        for i in solo_tags:
            new_solo_tags.append(i[:i.find(" ")]+"/>")
        tags = re.findall("<[a-z]*>",text) +new_solo_tags
        opening_tags = get_words_dict(tags)
        #closing_tags = get_words_dict(re.findall("<\/[a-z]*>",text))
        all_count = 0
        for i in opening_tags:
                if TAG_VIEWS:
                    print("\t",i,":",opening_tags[i])
                all_count+=opening_tags[i]
                total_count+=opening_tags[i]
        print("file statistics:")
        print("\tdifferent tags:",len(opening_tags),"opening tags:",all_count)
        print("total statistics")
        print("\tdifferent tags:",len(counter),"opening tags:",total_count)
        if TAG_VIEWS:
            input("\npress any key for next turn\n")



