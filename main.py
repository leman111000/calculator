

def main():
    try:
        a, b, c = (input().split(" "))
        num1 = int(a)
        num2 = int(c)
        if num1 > 10 or num2 > 10:
            print("Одно из чисел больше 10")
        else:
            result = eval(f"{a} {b} {c}")
            print(int(result))
    except Exception as e:
        print(f"Произошла ошибка: {e}")






if __name__ == "__main__":
    main()