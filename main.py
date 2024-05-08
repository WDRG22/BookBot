def main():    
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} found in the document")
    
    for item in chars_sorted_list:
        print(f"The {item["char"]} character was found {item["num"]} times")
        
    print("--- End report ---")
    
    
def get_book_text(path):
    with open(path) as f:
        return f.read()    
    
def count_words(text):
    words = text.split()
    return len(words)

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(dict):
    sorted_list = []
    for c in dict:
        sorted_list.append({"char": c, "num": dict[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

def get_chars_dict(text):
    counts = {}    
    for c in text:
        c = c.lower()
        if c in counts:
            counts[c] += 1
        elif c.isalpha():
            counts[c] = 1                
    return counts
    
main()
    