import wikipedia


def print_wikipedia_results(word):
    results = wikipedia.search(word)

    for result in results:
        try:
            page = wikipedia.page(result)
        except wikipedia.exceptions.DisambiguationError:
            print("Error")
            continue
        except wikipedia.exceptions.PageError:
            print("PageError for results : " + result)
            continue

        print(page.summary)


if __name__ == '__main__':
    print_wikipedia_results("football")