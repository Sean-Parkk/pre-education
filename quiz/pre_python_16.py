"""16. 1부터 50 까지의 숫자 중에서 3의 배수를 공백으로 구분하여 출력하시오.



<출력>
3  6  9  12  15  18  21  24  27  30  33  36  39  42  45  48  

"""
def muliple_of_3():
    result = ''
    for num in range(1, 51):
        if num % 3 == 0:
            result += str(num) + ' '
    return print(result[:-1])    # 마지막 공백 제거