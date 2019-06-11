def chumperizer(chumps: int):
    chumpResult = ''
    while chumps > 0:
        chumpResult = "chump" + chumpResult
        if chumps%3 == 0:
            chumpResult = "kick" + chumpResult
        elif chumps%5 == 0:
            chumpResult = "punch" + chumpResult
        chumps -= 1
    return chumpResult


def main():
    print(chumperizer(100))

if __name__ == '__main__':
    main()
