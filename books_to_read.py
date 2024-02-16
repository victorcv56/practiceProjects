"""Simple program which will create reading lists for user."""


def reading_list(books):#create list of books user wants to read
    book = input("Please enter book name(enter 'q' to end): \n")
    while book != 'q':#while loop asking user to enter book until 'q' is entered
        books.append(book.title())
        book = input("Please enter book name(enter 'q' to end): \n")
    
    return books

#method that will add book given to list
def add_to_list(books):
    """Method to manipulate book list and distribute into new read, not read list"""
    read = []
    not_read = []#empty lists inside method to be filled
    print("This is your reading list: \n")

    # fixed input read and now only takes 'y' or 'n' chars
    for book in books:
        current_book = input(f"Have you read {book}? (y/n)\n")
        flag = True
        while flag:
            if current_book == 'y':
                read.append(book)
                flag = False
            elif current_book == 'n':
                not_read.append(book)
                flag = False
            elif book != 'y' or 'n':
                print("Invalid answer.")
                current_book = input(f"Have you read {book}? (y/n)\n")

    book_list = {'read': read, 'to_read': not_read}
    return book_list

#method to display contents of book list
def display_lists(book_lists):
    """Displays dictionary with lists of books read and not read"""
    for book_status, books in book_lists.items():
        print(f"Books {book_status} are: ")
        for book in books:
            print(f"{book}")
        print("")#print statement to leave an empty line

# add method that will write book lists to txt file
def write_to_file(book_lists, filepath):
    """Creates txt files to store lists created by user."""
    
    with open(filepath, 'w') as fo: # opening file to write to
        for book_status, books in book_lists.items(): # loop that iterates dicitonary
            fo.write("books {}: \n".format(book_status))
            for book in books:
                fo.write("{}\n".format(book))
            fo.write("\n")
            

books = []#list of books made by user
book_list = {}#dictionary with keys 'read' & 'not read' with lists as values
filename = "list_of_books.txt"

reading_list(books)
print('--------------------------------')
book_list = add_to_list(books)
print('--------------------------------')
display_lists(book_list)
write_to_file(book_list, filename)
 
# Add method to write books to file
# Need method to read lists and add to program