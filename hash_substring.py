# python3

def read_input():
    input_choice, file = input().strip(), input().strip()
    if input_choice == 'I':
        return input().strip(), input().strip()
    elif input_choice == 'F':
        path = "./tests/" + file
        with open(path, 'r', encoding='utf-8') as file:
            return file.readline().strip(), file.readline().strip()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 31
    m= 10**9+9
    p_pow = 1
    pattern_hash = 0
    for c in pattern:
        pattern_hash = (pattern_hash +(ord(c)-ord('a')+1)*p_pow)%m
        p_pow = (p_pow*p)%m
    text_hash=0
    occurences = []
    for i in range(len(text)):
        text_hash = (text_hash * p + (ord(text[i]) - ord('a') + 1)) % m
        if i >= len(pattern):
            text_hash = (text_hash-(ord(text[i-len(pattern)])-ord('a')+1)*p**(len(pattern)))%m
        if i >= len(pattern) - 1 and text_hash == pattern_hash:
            if text[i-len(pattern)+1:i+1]==pattern:
                return [i-len(pattern)+1]
    return occurences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

