import argparse


# main/entry method
def main():
    parser = argparse.ArgumentParser(description="Github issue search tool")
    parser.add_argument("-l", "--language", nargs=1, default=None, type=str, help="Search by language.")
    parser.add_argument("-r", "--repository", nargs=1, default=None, type=str, help="Search by repository")
    parser.add_argument("-u", "--user", nargs=1, default=None, type=str, help="Search by user")
    parser.add_argument("-t", "--topic", nargs=1, default=None,type=str, help="Search by topic")
    parser.parse_args()


if __name__ == "__main__":
    main()
