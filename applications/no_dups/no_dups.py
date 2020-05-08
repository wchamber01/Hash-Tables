def no_dups(s):
    # Implement me.
    # split string into list of words
    s_list = s.split()
    hash_table = {}
    prev = None
    # iterate through list
    for word in s_list:
        if prev not in hash_table:
            if prev != word:
                if word not in hash_table:
                    hash_table[prev] = word
                    prev = word
    # chain None to end
    hash_table[prev] = None
    # loop through and create string with key, values
    no_dups_s = ''
    word = hash_table[None]
    while word != None:
        no_dups_s += word
        word = hash_table[word]
        if word is not None:
            no_dups_s += ' '

    return no_dups_s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
