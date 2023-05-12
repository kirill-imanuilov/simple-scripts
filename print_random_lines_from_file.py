import random
import sys


def main():
    with open("file.txt", "r") as file:
        lines = file.readlines()
        n = len(lines)
    try:
        print("To show a new line, press Enter")
        while True:
            tmp = input()
            random_number = random.randint(0, n - 1)
            line = lines[random_number]
            print(line)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()

