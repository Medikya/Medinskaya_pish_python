def anagramm(s1, s2):
    return sorted(s1) == sorted(s2)
string1 = "listen"
string2 = "silent"
print(anagramm(string1, string2))