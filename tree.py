
def main():
    height = int(input("Enter tree height: "))
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))
    
    print(" " * (height - 1) + "*")

    leave = input("Press enter to leave")

if __name__ == "__main__":
    main()