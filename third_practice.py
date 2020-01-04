#百分制成績轉換為等機成績
score = int(input('請輸入分數\n'))
if  (score >= 90):
    print('A等級')
elif(90 > score and score >= 80):
    print('B等級')
elif(80 > score and score >= 70):
    print('C等級')
elif(70 > score and score >= 60):
    print('D等級')
else:
    print('E等級')