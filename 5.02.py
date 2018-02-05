#def name():
 #   file_name = input()
  #  return file_name

def first(file_name):
    with open (file_name, encoding = "utf-8"):
        lined = f.readlines()
    return lines
    
def second(raw_lines):
    all_texts = {}
    for line in lines:
        splitted = line.split(",")
        if len(splitted) > 3:
            name = splitted[2]
            text = ",".join(splitted[3:])
            text = text[1:]
            if name in character_all_text:
                character_all_texts[name] = character_all_texts[name] + "\n" + text
            else:
                character_all_texts[name] = text
    return character_all_texts

def main():
    raw_data = first('all-seasons.scv')
    all_texts = second(raw_data)
    texts_length = []
    for character in all_texts:
        if character not in all_texts:
            texts_length[character] = len(all_texts[character])
    main_characters_pre = text_length.items()
    main_characters = []
    for name, length in main_character_pre:
        main_characters.append([length, name])
    main_names = []
    print(sorted(main_charactes[:10], reverse = True) [:20])
    


if __name__ == '__main__':
    main()
