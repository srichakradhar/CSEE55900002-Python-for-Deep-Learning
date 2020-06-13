from collections import Counter


def main():
    """
    A python program to find the wordcount in a file for each line and then
    print the output.
    Finally store the output back to the file.

    Input:a file includes two line
    Python Course
    Deep Learning Course

    Output:
    Python: 1
    Course: 2
    Deep: 1
    Learning: 1
    """
    file = open("input_file.txt", "r", encoding="utf-8")
    wordcount = Counter(file.read().split())
    f = open("output_file.txt", "w")
    for item in wordcount.items():
        f.write("{}: {}\n".format(*item))


if __name__ == "__main__":
    main()