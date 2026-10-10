s = input()

if not all(c.isdigit() or c == '-' for c in s):
    print('NO')
else:
    if len(s) == 12:
        if (s[0].isdigit() and s[1].isdigit() and s[2].isdigit()
            and s[3] == '-'
            and s[4].isdigit() and s[5].isdigit() and s[6].isdigit()
            and s[7] == '-'
            and s[8].isdigit() and s[9].isdigit() and s[10].isdigit() and s[11].isdigit()):
            print('YES')
        else:
            print('NO')

    elif len(s) == 14:
        if (s[0] == '7' and s[1] == '-'
            and s[2].isdigit() and s[3].isdigit() and s[4].isdigit()
            and s[5] == '-'
            and s[6].isdigit() and s[7].isdigit() and s[8].isdigit()
            and s[9] == '-'
            and s[10].isdigit() and s[11].isdigit() and s[12].isdigit() and s[13].isdigit()):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')
