def get_book_text(path):
    fcontent = ""
    
    with open(path) as f:
        fcontent = f.read()
    
    return fcontent


def get_num_words(content):
    list_content = content.split()

    return len(list_content)

