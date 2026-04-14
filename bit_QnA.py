import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_val(n, base):
    if base == 2: return bin(n)[2:].zfill(12)
    if base == 8: return oct(n)[2:]
    if base == 10: return str(n)
    if base == 16: return hex(n)[2:].upper()

# 프로그램 전체 루프
while True:
    # 1. 새로운 문제 생성 (r을 누르면 이 지점으로 다시 돌아옴)
    val1 = random.randint(0, 4095)
    val2 = random.randint(0, 4095)
    
    andV, orV, xorV = val1 & val2, val1 | val2, val1 ^ val2
    
    bases = [(2, "2진수"), (8, "8진수"), (10, "10진수"), (16, "16진수")]
    selected_bases = random.sample(bases, 2)
    b1_num, b1_name = selected_bases[0]
    b2_num, b2_name = selected_bases[1]
    
    bit1_str = format_val(val1, b1_num)
    bit2_str = format_val(val2, b2_num)
    
    res1, res2, res3 = "1. and", "2. or", "3. xor"
    
    # 한 문제 내에서의 루프
    while True:
        clear_screen()
        print(f"num1({b1_name}) = {bit1_str}")
        print(f"num2({b2_name}) = {bit2_str}")
        print("==========")
        print(res1)
        print(res2)
        print(res3)
        print("----------")
        print("r: 새 문제 / q: 종료")
        
        choice = input("\n선택: ").lower()

        if choice == '1':
            res1 = f"1. {bin(andV)[2:].zfill(12)} (결과: {andV})"
        elif choice == '2':
            res2 = f"2. {bin(orV)[2:].zfill(12)} (결과: {orV})"
        elif choice == '3':
            res3 = f"3. {bin(xorV)[2:].zfill(12)} (결과: {xorV})"
        elif choice == 'r':
            print("새 문제를 생성합니다...")
            time.sleep(0.3)
            break  # 안쪽 while문을 빠져나가서 위쪽의 문제 생성 코드로 이동
        elif choice == 'q':
            print("프로그램을 종료합니다.")
            exit() # 프로그램 전체 즉시 종료
        else:
            print("1, 2, 3, r, q 중에서 입력해주세요.")
            time.sleep(0.7)
