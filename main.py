import sys
from stats import get_num_words
from stats import character_count
from stats import sort_characters

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]

	text = get_book_text(book_path)
	num_words = get_num_words(text)
	chars = character_count(text)
	sorted_list = sort_characters(chars)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")

	for item in sorted_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")

	print("============= END ===============")

def get_book_text(path):
	with open(path) as f:
		return f.read()


main()
