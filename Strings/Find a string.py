def count_substring(string, sub_string):
    j=0
    while True:
        if (string.find(sub_string)!=(-1)):
            j+=1
            string=string[string.index(sub_string)+1:]
        else:
             break
    return j

