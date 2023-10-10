bad_chars = [';', ':', '!', "*", "?", ",", "-"]

def tokenize(sentence):
    for j in bad_chars:
        sentence = sentence.replace(j, '')
    token = sentence.replace("'", " ")
    token = token.split()
    for i in range(len(token)):
        token[i] = token[i].lower()   
    return token
