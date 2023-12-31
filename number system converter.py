list_of_digits = []
invalid = 0
try:
    initial_base = int(input('''Which base is the number to be converted from?
Press:
1 for decimal
2 for binary
3 for octal
4 for hexadecimal
>>> '''))
    convert_base = int(input('''To which base should the number be converted to?
Press:
1 for decimal
2 for binary
3 for octal
4 for hexadecimal
>>> '''))
    if initial_base == 1:
        n = input("Enter the decimal number: ")
    elif initial_base == 2:
        n = input("Enter the binary number: ")
        for l in "23456789":
            if l in n:
                invalid += 1
                break   
    elif initial_base == 3:
        n = input("Enter the octal number: ")
        if "8" in n or "9" in n:
            invalid += 1
    elif initial_base == 4:
        n = input("Enter the hexadecimal number: ")
        n = n.upper()
        for l in n:
            if l in "GHIJKLMNOPQRSTUVWXYZ":
                invalid += 1
                break

    def DecToBin(n):
        fcount = 0
        l1 = []
        try:
            n = int(n)
            while n > 0:
                rem = str(n%2)
                l1.insert(0, rem)
                n = n//2
            bi = ''
            for digit in l1:
                bi = bi + digit
            l1.clear()
        except ValueError:
            int_n, fl_n = n.split(".")
            int_n = int(int_n)
            fl_n = float("0." + fl_n)
            while int_n > 0:
                rem = str(int_n%2)
                l1.insert(0, rem)
                int_n = int_n//2
            bi = ''
            for digit in l1:
                bi = bi + digit
            l1.clear()
            while fl_n != 0 and fcount < 10:
                fcount += 1
                l1.append(str(int(fl_n * 2)))
                fl_n = round(fl_n*2 - int(fl_n * 2), len(str(fl_n*2)) - len(str(int(fl_n*2))) - 1)
            bi += "."
            for digit in l1:
                bi += digit
        return bi

    def DecToOct(n):
        fcount = 0
        l1 = []
        try:
            n = int(n)
            while n > 0:
                rem = str(n%8)
                l1.insert(0, rem)
                n = n//8
            octa = ''
            for digit in l1:
                octa = octa + digit
        except ValueError:
            int_n, fl_n = n.split(".")
            int_n = int(int_n)
            fl_n = float("0." + fl_n)
            while int_n > 0:
                rem = str(int_n%8)
                l1.insert(0, rem)
                int_n = int_n//8
            octa = ''
            for digit in l1:
                octa = octa + digit
            l1.clear()
            while fl_n != 0 and fcount < 10:
                fcount += 1
                l1.append(str(int(fl_n * 8)))
                fl_n = round(fl_n*8 - int(fl_n * 8), len(str(fl_n*8)) - len(str(int(fl_n*8))) - 1)
            octa += "."
            for digit in l1:
                octa += digit
        return octa

    def DecToHex(n):
        l1 = []
        fcount = 0
        try:
            n = int(n)
            while n > 0:
                rem = str(n%16)
                if rem == '10':
                    rem = 'A'
                elif rem == '11':
                    rem = 'B'
                elif rem == '12':
                    rem = 'C'
                elif rem == '13':
                    rem = 'D'
                elif rem == '14':
                    rem = 'E'
                elif rem == '15':
                    rem = 'F'
                l1.insert(0, rem)
                n = n//16
            hexa = ''
            for digit in l1:
                hexa = hexa + digit
            l1.clear()
        except ValueError:
            int_n, fl_n = str(n).split(".")
            int_n = int(int_n)
            fl_n = int(fl_n)/(10 ** len(fl_n))
            while int_n > 0:
                rem = str(int_n%16)
                if rem == '10':
                    rem = 'A'
                elif rem == '11':
                    rem = 'B'
                elif rem == '12':
                    rem = 'C'
                elif rem == '13':
                    rem = 'D'
                elif rem == '14':
                    rem = 'E'
                elif rem == '15':
                    rem = 'F'
                l1.insert(0, rem)
                int_n = int_n//16
            hexa = ''
            for digit in l1:
                hexa = hexa + digit
            l1.clear()
            while fl_n != 0 and fcount < 10:
                fcount += 1
                append_wala = int(fl_n * 16)
                if append_wala == 10:
                    append_wala = 'A'
                elif append_wala == 11:
                    append_wala = 'B'
                elif append_wala == 12:
                    append_wala = 'C'
                elif append_wala == 13:
                    append_wala = 'D'
                elif append_wala == 14:
                    append_wala = 'E'
                elif append_wala == 15:
                    append_wala = 'F'
                l1.append(str(append_wala))
                fl_n = round(fl_n*16 - int(fl_n * 16), len(str(fl_n*16)) - len(str(int(fl_n*16))) - 1)
            hexa += "."
            for digit in l1:
                hexa += digit
        return hexa

    def BinToDec(n):
        pow2 = 0
        dec = 0
        try:
            n = int(n)
            while n > 0:
                rem = n%10
                dec += rem*(2**pow2)
                pow2 += 1
                n = n//10
        except ValueError:
            int_n, fl_n = n.split(".")
            int_n = int(int_n)
            while int_n > 0:
                rem = int_n%10
                dec += rem*(2**pow2)
                pow2 += 1
                int_n = int_n//10
            ind = -1
            for i in fl_n:
                dec += int(i) * (2 ** ind)
                ind -= 1
        return dec

    def OctToDec(n):
        pow8 = 0
        dec = 0
        try:
            n = int(n)
            while n > 0:
                rem = n%10
                dec += rem*(8**pow8)
                pow8 += 1
                n = n//10
        except ValueError:
            int_n, fl_n = n.split(".")
            int_n = int(int_n)
            while int_n > 0:
                rem = int_n%10
                dec += rem*(8**pow8)
                pow8 += 1
                int_n = int_n//10
            ind = -1
            for i in fl_n:
                dec += int(i) * (8 ** ind)
                ind -= 1
        return dec

    def HexToDec(n):
        pow16 = 0
        dec = 0
        l1 = []
        if "." in n:
            int_n = n[0 : n.index('.')]
            fl_n = n[n.index('.') + 1 : ]
            for digit in int_n:
                if digit == "A":
                    digit = 10
                if digit == "B":
                    digit = 11
                if digit == "C":
                    digit = 12
                if digit == "D":
                    digit = 13
                if digit == "E":
                    digit = 14
                if digit == "F":
                    digit = 15
                l1.insert(0, int(digit))
            for digit in l1:
                dec += digit*(16**pow16)
                pow16 += 1
            l1.clear()
            ind = -1
            for digit in fl_n:
                if digit == "A":
                    digit = 10
                if digit == "B":
                    digit = 11
                if digit == "C":
                    digit = 12
                if digit == "D":
                    digit = 13
                if digit == "E":
                    digit = 14
                if digit == "F":
                    digit = 15
                l1.append(int(digit))
            for digit in l1:
                dec += digit*(16**ind)
                ind -= 1
        else:
            for digit in n:
                if digit == "A":
                    digit = 10
                if digit == "B":
                    digit = 11
                if digit == "C":
                    digit = 12
                if digit == "D":
                    digit = 13
                if digit == "E":
                    digit = 14
                if digit == "F":
                    digit = 15
                l1.insert(0, int(digit))
            for digit in l1:
                dec += digit*(16**pow16)
                pow16 += 1
        return dec

    if invalid == 0:
        if initial_base == 1:
            if convert_base == 2:
                print("Binary number =", DecToBin(n))
            elif convert_base == 3:
                print("Octal number =", DecToOct(n))
            elif convert_base == 4:
                print("Hexadecimal number =", DecToHex(n))
        elif initial_base == 2:
            if convert_base == 1:
                print("Decimal number =", BinToDec(n))
            elif convert_base == 3:
                n = BinToDec(n)
                print("Octal number =", DecToOct(n))
            elif convert_base == 4:
                n = BinToDec(n)
                print("Hexadecimal number =", DecToHex(n))        
        elif initial_base == 3:
            if convert_base == 1:
                print("Decimal number =", OctToDec(n))
            elif convert_base == 2:
                n = OctToDec(n)
                print("Binary number =", DecToBin(n))
            elif convert_base == 4:
                n = OctToDec(n)
                print("Hexadecimal number =", DecToHex(n))
        elif initial_base == 4:
            if convert_base == 1:
                print("Decimal number =", HexToDec(n))
            elif convert_base == 2:
                n = HexToDec(n)
                print("Binary number =", DecToBin(n))
            elif convert_base == 3:
                n = HexToDec(n)
                print("Octal number =", DecToOct(n))
    else:
        print("Invalid input.")
except ValueError:
    print("You have input a string data type into a number. Please re-run the code again.")
