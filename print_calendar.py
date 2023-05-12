import calendar


def main():
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    output = calendar.month(year, month)
    print(output)


if __name__ == "__main__":
    main()

