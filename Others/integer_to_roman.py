

def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    num.reverse()
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    sym.reverse()
    k = 0

    for i in num:
        if i <= number:
            div = number//i
            print(div*sym[k], end='')
            number %= div*i
        k += 1

if __name__ == "__main__":
    number = 3549
    print("Roman value is:", end=" ")
    printRoman(number)
