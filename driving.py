country = input('請問你是哪一國人：')
age = input('請輸入你的年齡：')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('可以考駕照')
    else:
        print('須滿18歲才可以考駕照')