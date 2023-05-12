letter = list()
N = int(input("введите колчисетсво символов которые будете вводить "))
for i in range(N):
    letter.append(input(f"введите {i+1} букву "))

print(letter)
letter1 = set(letter)
result = ''
for i in letter1:
    if i in letter:
        count = 0
        for j in range(len(letter)):
            if letter[j] == i:
                count += 1
        result += i
        if count > 1:
            result += str(count)

print(result)