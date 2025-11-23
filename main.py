import sys
from stats import word_count 
from stats import character_count
from stats import myFunc
from stats import sort
def main ():
   
    print("============ BOOKBOT ============")
   # print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    try:
        book_text = get_book_text(f"{sys.argv[1]}") 
    
        
    #print(book_text)
        number = word_count(book_text)
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    print (f"Found {number} total words")
    print("--------- Character Count -------")
    char = character_count(book_text)
  #  print (char)
    order = sort(char)
    for l in order:
        print (f"{l["char"]}: {l["num"]}")
    print("============= END ===============")

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()