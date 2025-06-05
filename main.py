def get_book_text(book):
    with open(book) as book_to_read:
        book_text = book_to_read.read()
    return book_text

text = ""
def main():
    text = get_book_text('books/frankenstein.txt')
    print(text)

main()
