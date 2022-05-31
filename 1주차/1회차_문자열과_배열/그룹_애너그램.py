### GROUP ANAGRAM ###
# l2 = []


# l2 = {}

def anagram(str_list):
    l = {}
    for i in range(len(str_list)):
        word = "".join(sorted(str_list[i]))
        if word not in l:
            l[word] = [str_list[i]]
        else:
            l[word] += [str_list[i]]
    return l.values()


l1 = ["eat", "tea", "tan", "ate", "nat", "bat"]


print(anagram(l1))