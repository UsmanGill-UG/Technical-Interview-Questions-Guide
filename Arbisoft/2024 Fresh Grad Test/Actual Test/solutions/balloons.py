import sys


def get_ballon(pattern: str, position: int) -> str:
    """
    Returns the ballon that should be placed at particular postion
    as per the pattern provided
    """
    ballon_index = position % len(pattern)
    return pattern[ballon_index]


def get_ballon_count(pattern: str, start_postion: int, end_postion: int) -> dict:
    """
    Stores count of all the balloons by iterating over all the postions
    """
    ballon_count = {"b": 0, "o": 0, "w": 0}
    for pos in range(start_postion, end_postion + 1):
        ballon = get_ballon(pattern, pos)
        ballon_count[ballon] += 1
    return ballon_count


def print_ballon_count(ballon_count: dict):
    """
    Prints dictionary of balloon count
    """
    for key, val in ballon_count.items():
        print(f"{key}{val}", end="")


if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        pattern = file.readline().strip()
        start_postion = int(file.readline().strip())
        end_postion = int(file.readline().strip())
    ballon_count = get_ballon_count(pattern, start_postion, end_postion)
    print_ballon_count(ballon_count)
