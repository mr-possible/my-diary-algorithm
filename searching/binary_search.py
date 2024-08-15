def main():
    collection: list[int] = [2, 7, 8, 4, 1]

    # Item to search ?
    number_to_search = 1
    answer = None

    # 1. Sort the collection
    collection.sort()

    # 2. Apply Binary Search
    start = 0
    end = len(collection) - 1

    while start <= end:
        mid = (start + end) // 2
        if number_to_search < collection[mid]:
            end = mid - 1
        elif number_to_search > collection[mid]:
            start = mid + 1
        else:
            answer = mid
            break

    # 3. Print the searched item
    print(f"Sorted collection => {collection}")
    if answer is None:
        print(f"{number_to_search} not found!")
    else:
        print(f"{number_to_search} found at position {answer} in the list!")


if __name__ == "__main__":
    main()
