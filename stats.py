def get_num_words(text):
    split_text = text.split()
    return len(split_text)

def character_count(text):
    lower_text = text.lower()
    character_dict = {}
    for char in lower_text:
        if char in character_dict:
            character_dict[char] += 1 #if its in dic character is counted
        else:
            character_dict[char] = 1 #if its not in dic character is added and set to 1
            
    return character_dict


def sorted_dict(char_dict):
    char_list = []
    for char in char_dict:
        count = char_dict[char]
        char_list.append({"char":char,"num":count})#breaks dic up into a list of dictonaries
    
    def sort_on(item):

        return item["num"]

    char_list.sort(reverse=True,key=sort_on)
    return char_list