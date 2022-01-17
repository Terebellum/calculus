def calculator(number, program):
    calculus = number
    for i in program:
        if i == "1":
            calculus = calculus-2
        if i == "2":
            calculus = calculus*3
    return calculus
def findprogram(start, end):
    m = "12*"
    for i in m:
        for j in m:
            for l in m:
                for s in m:
                    for r in m:
                        program = "".join([i, j, l, s, r])
                        if calculator(start, program) == end:
                            return program
    return None
                




if __name__ == '__main__':
    print(findprogram(3, 17))
