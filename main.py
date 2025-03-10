from chain import Chain

def main():
    difficulty = input("Enter difficulty (or x to use default = 20): ")
    difficulty = difficulty if (difficulty.isnumeric() and int(difficulty) < 256 and int(difficulty) > 0) else '20'
    chain = Chain(int(difficulty))

    i = 0
    stop = False
    while not stop:
        data = input("Add smth to the block (or LEAVE EMPTY to exit): ")
        if data == "":
            stop = True
        else:
            chain.add_to_pool(data)
            chain.minecraft()
            i += 1
    print("Final Blockchain:")
    print(chain)
    return


if __name__=="__main__":
    main()