dict = {'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3',
        'G':'4', 'H':'4', 'I':'4', 'J':'5', 'K':'5', 'L':'5',
        'M':'6', 'N':'6', 'O':'6', 'P':'7', 'Q':'7', 'R':'7', 'S':'7',
        'T':'8', 'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':'9'}
# 딕셔너리 만들기 귀찮은데 진짜 이 방법 말고 다른 거 없을까???

DIAL = input()

sumV = 0
for char in DIAL:
    sumV += int(dict[char]) + 1

print(sumV)
