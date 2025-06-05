def get_book_text(book):
    with open(book) as book_to_read:
        book_text = book_to_read.read()
    return book_text

def main():
    text_file = get_book_text('books/frankenstein.txt')
    return text_file
    
text_string = main()

def split(book_text):
    book_text_list = book_text.split()
    word_count = len(book_text_list)
    print(f"{word_count} words found in the document")

split(text_string)
    