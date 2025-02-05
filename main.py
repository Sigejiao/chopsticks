while True :
    A = None
    B = None
    C = 1
    D = 1

    while True:
        A = int(input("请输入A的值: "))
        B = int(input("请输入B的值: "))
        
        # 执行上述逻辑（从计算中间值到执行替换）
        one_prime = (A + C) % 10
        two_prime = (A + D) % 10
        three_prime = (B + C) % 10
        four_prime = (B + D) % 10


        five_prime = 10 - A
        six_prime = 10 - B

        if five_prime != C and five_prime != D and six_prime != C and six_prime != D:# 还没有赢
            if five_prime != one_prime and six_prime != one_prime :
                C = one_prime  # 或者根据具体情况替换 C
            elif five_prime != three_prime and six_prime != three_prime :
                C = three_prime  # 根据情况替换
            elif six_prime != two_prime and six_prime != two_prime :
                D = two_prime  # 或者根据具体情况替换 D
            elif six_prime != four_prime and six_prime != four_prime:
                D = four_prime  # 根据情况替换
            print(C)
            print(D)
        else:
            print('You LOSE')
            break
        
        # 省略中间逻辑代码，重复判断并替换C、D

    try_again = input("是否重新运行？(y/n): ").strip().lower()
    if try_again != 'y':
        print("程序结束。")
        break