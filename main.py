

def main():
    try:
        a, b, c = (input().split(" "))
        num1 = int(a)
        num2 = int(c)
        if num1 > 10 or num2 > 10:
            print("Одно из чисел больше 10")
        elif num1 < 1 or num2 < 1:
            print("Одно из чисел меньше 1")
        else:
            result = eval(f"{a} {b} {c}")
            new_result = int(result)
            print(str(new_result))
    except Exception as e:
        print(f"Произошла ошибка: {e}")






if __name__ == "__main__":
    main()