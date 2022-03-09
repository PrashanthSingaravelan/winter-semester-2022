import string


def makeList(key_word):
    azList = list(string.ascii_lowercase)
    for i in key_word:
        if i in azList:
            azList.remove(i)
    # to make i and j in the same cell
    azList.remove("j")
    return key_word + azList


def uniq(key_word):
    final = []
    for i in key_word:
        if i not in final:
            final.append(i)
    return final


def check(matrix, pair):
    lst = []
    a = matrix.index(pair[0])
    b = matrix.index(pair[1])
    print(f'pair[0]={a} & pair[1]={b}')
    for column in range(5):
        # Same row
        j = a // 5
        temp = 5 * j
        if pair[1] == matrix[temp + column]:
            ind_a = ((a + 1) % 5) + 5 * j
            ind_b = ((b + 1) % 5) + 5 * j
            print(f'same row index : {ind_a}')
            print(f'same row index : {ind_b}')
            lst.append(matrix[ind_a])
            lst.append(matrix[ind_b])
            break
    else:
        # Same column
        j = a % 5
        for row in range(5):
            if pair[1] == matrix[j + (row * 5)]:
                ind_a = (a + 5) % 20
                ind_b = (b + 5) % 20
                print(f'same column index : {ind_a}')
                print(f'same column index : {ind_b}')
                lst.append(matrix[ind_a])
                lst.append(matrix[ind_b])
                break
        else:
            # diff row and column
            x = a % 5
            y = b % 5
            z = x - y
            print(f'a:{a} b:{b}')
            if(z < 0):
                z = abs(z)
                print(f'diff1 a+z: {a+z} a+z: {b-z}')
                lst.append(matrix[a + z])
                lst.append(matrix[b - z])
            else:
                z = abs(z)
                print(f'diff2 a-z: {a-z} a+z: {b+z}')
                lst.append(matrix[a - z])
                lst.append(matrix[b + z])
    return lst


def split(word):
    tempLst = [word[0]]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            tempLst.append(word[i])
        else:
            tempLst.append('x')
            tempLst.append(word[i])
    if len(tempLst) % 2 != 0:
        tempLst.append('x')
    return [(tempLst[i], tempLst[i + 1]) for i in range(0, len(tempLst), 2)]


def encipher(matrix, word_pairs):
    result = []
    for i in word_pairs:
        a = (check(matrix, i))
        result.extend(a)
    return "".join(result)


key_text = input("Enter ur key_word: ")
#key_text = "playfairexample"
key_text = key_text.replace("j", "i")
key_list = list(key_text)
finalized = uniq(key_list)
toMatrix = makeList(finalized)
#word = "welcome"
word = input("Enter the word: ")
word_pairs = split(list(word))
print(encipher(toMatrix, word_pairs))
