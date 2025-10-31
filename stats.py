def get_book_text (filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents

def get_word_count (filepath):
    book = get_book_text(filepath)
    words = book.split()
    count = 0
    for word in words:
        count +=1
    return count

def sort_on(item):
    return item["num"]

def get_char_count (filepath):
    book = get_book_text(filepath)
    book = book.lower()
    unique = set ()
    dic = {}
    for char in book:
        unique.add (char)
    for char in unique:
        dic[char]=0
    for letter in book:
        for char in dic:
            if char == letter:
                dic[char] +=1 
    letters = []
    for char, count in dic.items():
        letters.append({"char":char,"num":count})
    
    letters.sort(reverse=True, key=sort_on)

    #for char in book:
    return letters