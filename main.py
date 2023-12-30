from typing import Dict

def main():
  content = book_content("./books/frankenstein.txt")

  # number of words
  print(number_of_words_in_book(content))
  
  char_count = count_by_alpha_characters_in_book(content)
  
  # character count dict
  print(char_count)

  print_char_count_by_number_of_occurrence(char_count)



# retrieves the book content from a local location
def book_content(book_url: str)-> str:
  with open(book_url) as f:
    return f.read()

# uses the full text of the book and returns the number of words it has
# by splitting it where there is a space or new line.
def number_of_words_in_book(book: str)-> int:
  words_in_text = book.split()
  return len(words_in_text)

# uses the full text of the book and returns a dictionary
# with a character and the number of times it appears on the book
def count_by_alpha_characters_in_book(book: str)-> Dict[str, int]:
  char_count = {}
  for char in book:
    curr_char = char.strip().lower()
    if len(curr_char) > 0 and curr_char.isalpha():
      if curr_char in char_count:
        char_count[curr_char]+=1
      else:
        char_count[curr_char]=1
  return char_count

# prints the character count by number of occurrence from the highest to the smallest
def print_char_count_by_number_of_occurrence(char_count: Dict[str, int])-> None:
  dict_keys = list(char_count.items())
  dict_keys.sort(key=lambda letter: letter[1], reverse=True)
  for key,value in dict_keys:
    print(f"The '{key}' character was found {value} times")

main()