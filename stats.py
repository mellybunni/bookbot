def get_num_words(text):
	words = text.split()
	return len(words)

def character_count(text):
	characters = {}
	lowercase_text = text.lower()
	for letter in lowercase_text:
		if letter in characters:
			characters[letter] += 1
		else:
			characters[letter] = 1
	return characters

def sort_on(item):
	return item["num"]

def sort_characters(characters):
    letter_list = []
    for letter, count in characters.items():
        letter_list.append({"char": letter, "num": count})
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
