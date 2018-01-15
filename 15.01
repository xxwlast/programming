def get_text(filename):
    with open('text.txt', encoding = 'utf-8') as f:
        text = f.read()
        return text

def tokenize(text):
    words = text.split() 
    return words

def extract_constr():
    return constr_list

#def write_results():

def main():
    raw_text = get_text('text.txt')
    tokens = tokenize(raw_text)
    print(tokens[:20])

main()
