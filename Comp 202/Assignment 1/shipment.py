#Marie-Elise Latorre
#260981320
 
 
#calculate checksum
def calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9):
    """
    (int, int, int, int, int, int, int, int, int) -> str
    Returns the checksum as a string
    
    >>> calculate_isbn_checksum_by_digits(8,7,1,1,0,7,5,5,9)
    '7'
    >>> calculate_isbn_checksum_by_digits(1,1,1,1,1,1,1,1,1)
    '1'
    >>> calculate_isbn_checksum_by_digits(0,0,0,0,0,0,0,0,0,)
    '0'
    
    """
    #calaculations for checksum
    a = (d1 + 2*d2 + 3*d3 + 4*d4 + 5*d5 + 6*d6 + 7*d7 + 8*d8 + 9*d9) % 11
    if a == 10:
        return str(X)
    else:
        return str(a)
 
 
def calculate_isbn_checksum(isbn):
    """
    (int) -> str
    Returns the checksum as a string
    
    >>>calculate_isbn_checksum(871107759)
    '7'
    >>>calculate_isbn_checksum(993947583)
    '7'
    >>>calculate_isbn_checksum(995843879)
    '8'
    """
    #ISBN to numbers 
    d9 = isbn % 10
    isbn = isbn // 10
    d8 = isbn % 10
    isbn = isbn // 10
    d7 = isbn % 10
    isbn = isbn // 10
    d6 = isbn % 10
    isbn = isbn // 10
    d5 = isbn % 10
    isbn = isbn // 10
    d4 = isbn % 10
    isbn = isbn // 10
    d3 = isbn % 10
    isbn = isbn // 10
    d2 = isbn % 10
    isbn = isbn // 10
    d1 = isbn % 10
    
    #math 
    a = calculate_isbn_checksum_by_digits(d1, d2, d3, d4, d5, d6, d7, d8, d9)
    return a
    
def is_isbn(isbn, checksum):
    """
    (int, str) -> bool
    Returns True if the ISBN is valid
    
    >>>is_isbn(871107559, '4')
    False
    
    >>>is_isbn(993947583, 7)
    True
    
    >>>is_isbn(728901886, 0)
    False
    """
    #ISBN to numbers
    d9 = isbn % 10
    isbn = isbn // 10
    d8 = isbn % 10
    isbn = isbn // 10
    d7 = isbn % 10
    isbn = isbn // 10
    d6 = isbn % 10
    isbn = isbn // 10
    d5 = isbn % 10
    isbn = isbn // 10
    d4 = isbn % 10
    isbn = isbn // 10
    d3 = isbn % 10
    isbn = isbn // 10
    d2 = isbn % 10
    isbn = isbn // 10
    d1 = isbn % 10
    
    #math 
    a = (d1 + 2*d2 + 3*d3 + 4*d4 + 5*d5 + 6*d6 + 7*d7 + 8*d8 + 9*d9) % 11
    if checksum == a:
        return True
    else:
        return False
 
 
def book_fits_in_box(box_w, box_d, box_h, book_w, book_d, book_h):
    """
    (int, int, int, int, int, int, int,) -> bool
    Returns True if the specified book can fit in the specified box
    
    >>>book_fits_in_box(15, 2, 2, 2, 15, 2)
    True
    >>>book_fits_in_box(10, 10, 10, 2, 15, 2)
    False
    >>>book_fits_in_box(3, 3, 3, 3, 3, 3)
    True
    """
    #box
    if box_w > box_h and box_w > box_d:
        big_box = box_w
        if box_h > box_d:
            med_box = box_h
            small_box = box_d
        else:
            med_box = box_d
            small_box = box_h
    elif box_h > box_d:
        big_box = box_h
        if box_d > box_w:
            med_box = box_d
            small_box = box_w
        else:
            med_box = box_w
            small_box = box_d
    else:
        big_box = box_d
        if box_h > box_w:
            med_box = box_h
            small_box = box_w
        else:
            med_box = box_w
            small_box = box_h
            
    #book
    if book_w > book_h and book_w > book_d:
        big_book = book_w
        if book_h > book_d:
            med_book = book_h
            small_book = book_d
        else:
            med_book = book_d
            small_book = book_h
    elif book_h > book_d:
        big_book = book_h
        if book_d > book_w:
            med_book = book_d
            small_book = book_w
        else:
            med_book = book_w
            small_book = book_d
    else:
        big_book = book_d
        if book_h > book_w:
            med_book = book_h
            small_book = book_w
        else:
            med_book = book_w
            small_book = book_h
            
    
    return big_box >= big_book and med_box >= med_book and small_box >= small_book
            
    
def get_smallest_box_for_book(book_w, book_d, book_h):
    """
    (int, int, int) -> str
    Returns a string corresponding to the smallest box size in which the book can fit
    
    >>>get_smallest_box_for_book(12, 12, 2)
    medium
    >>>get_smallest_box_for_book(10, 8, 2)
    small
    >>>get_smallest_box_for_book(30, 30, 2)
    None
    >>>get_smallest_box_for_book(20, 20, 2)
    big
    """
    if book_fits_in_box(10, 10, 2, book_w, book_d, book_h):
        return "small"
    if book_fits_in_box(15, 15, 3, book_w, book_d, book_h):
        return "medium"
    if book_fits_in_box(20, 20, 4, book_w, book_d, book_h):
        return "big"
 
def get_num_books_for_box(box_w, box_d, box_h, book_w, book_d, book_h):
    """
    (int, int, int, int, int, int, int,) -> int
    Returns the maximum number of copies of specied books that can fit into a specified box
    
    >>>get_num_books_for_box(10, 5, 5, 5, 5, 2)
    4
    >>>get_num_books_for_box(4, 4, 4, 4, 4, 4)
    0
    >>>get_num_books_for_box(200, 4, 4, 4, 4, 4)
    49
    """
    b = box_w*box_h*box_d
    f = book_w*book_d*book_h
   
    return (b//f)-1
 
def main():
    """
    ()-> NoneType
    Prints greetings and gives back functions
    
    >>>main()
    Welcome to the shipment calculation system.
    1)   Check ISBN
    2)   Check box/book size
    3)   Get smallest box size for book
    4)   Get num equally-sized books per box
    Enter choice (1-4):1
    Enter ISBN:100101011
    Enter checksum:1
    ISBN is not valid (checksum did not match).
    
    >>>main()
    Welcome to the shipment calculation system.
    1)   Check ISBN
    2)   Check box/book size
    3)   Get smallest box size for book
    4)   Get num equally-sized books per box
    Enter choice (1-4):2
    Width of box:15
    Depth of box:2
    Height of box:2
    Width of book:2
    Depth of book:15
    Height of book:2
    Will the book fit in the box?: True
    
    >>>main()
    Welcome to the shipment calculation system.
    1)   Check ISBN
    2)   Check box/book size
    3)   Get smallest box size for book
    4)   Get num equally-sized books per box
    Enter choice (1-4):3
    Width of book:12
    Depth of book:12
    Height of book:2
    The smallest box for your book is medium
    
    >>>main()
    Welcome to the shipment calculation system.
    1)	 Check ISBN
    2)	 Check box/book size
    3)	 Get smallest box size for book
    4)	 Get num equally-sized books per box
    Enter choice (1-4):4
    Width of box:10
    Depth of box:5
    Height of box:5
    Width of book:5
    Depth of book:5
    Height of book:2
    The amount of books that can be placed in the box are 4
    
    """
    print("Welcome to the shipment calculation system.")
    print("1)\t Check ISBN")
    print("2)\t Check box/book size")
    print("3)\t Get smallest box size for book")
    print("4)\t Get num equally-sized books per box")
    c = int(input("Enter choice (1-4):" ))
    
    if c == 1:
        p = int(input("Enter ISBN:" ))
        f = int(input("Enter checksum:" ))
        u = is_isbn(p, f)
        if u == True:
            print("ISBN is valid (checksum did match).")
        else:
            print("ISBN is not valid (checksum did not match).")
    elif c == 2:
        l = input("Width of box:" )
        m = input("Depth of box:" )
        n = input("Height of box:" )
        o = input("Width of book:" )
        q = input("Depth of book:" )
        z = input("Height of book:" )
        r = book_fits_in_box(l, m, n, o, q, z)
        print("Will the book fit in the box?:", r)
    elif c == 3:
        y = int(input("Width of book:" ))
        x = int(input("Depth of book:" ))
        a = int(input("Height of book:" ))
        t = get_smallest_box_for_book(y, x, a)
        print("The smallest box for your book is", t)
    elif c == 4:
        k = int(input("Width of box:" ))
        p = int(input("Depth of box:" ))
        g = int(input("Height of box:" ))
        i = int(input("Width of book:" ))
        j = int(input("Depth of book:" ))
        v = int(input("Height of book:" ))
        s = get_num_books_for_box(k, p, g, i, j, v)
        if s < 0:
            print("0 books can be put in the given box")
        else:
            print("The amount of books that can be placed in the box are", s) 
