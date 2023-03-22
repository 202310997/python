def exchange(change) :
    remainder_1 = change // 500
    remainder_2 = change % 500
    remainder_3 = remainder_2 // 100
    remainder_4 = remainder_2 % 100
    remainder_5 = remainder_4 // 50
    remainder_6 = remainder_4 % 50
    remainder_7 = remainder_6 // 10
    remainder_8 = remainder_6 % 10
    print('500원 동전의 개수:',remainder_1)
    print('100원 동전의 개수:',remainder_3)
    print('50원 동전의 개수:',remainder_5)
    print('10원 동전의 개수:',remainder_7)

def get_integer(prompt) :
    res = int(input(prompt))
    return res


prompt = '동전으로 교환하고자 하는 금액은?'
input_money = get_integer(prompt)
#change = int(input('동전으로 교환하고자 하는 금액은?'))
exchange(input_money)
