import webbrowser


def main():
    search_query = input("Enter a YouTube query: ")
    search_query = search_query.replace(" ", "+")
    webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")


if __name__ == "__main__":
    main()

