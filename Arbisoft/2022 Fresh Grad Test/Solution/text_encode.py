data_array = [
    "ABCDE",
    "FGHIJ",
    "KLMNO",
    "PQRST",
    "UVWXY",
    "Z",
]


def finder(pattern):
    last_row, last_col = 0, 0
    result = []
    answer = ""

    for char in pattern:
        if char == " ":
            answer += "".join(result)
            result.clear()
            last_row, last_col = 0, 0

        for index, alpha_array in enumerate(data_array):
            if char in alpha_array:
                current_row = index
                current_col = alpha_array.index(char)
                if last_row < current_row:
                    direction_count = current_row - last_row
                    direction = "d" * direction_count
                    if direction:
                        result.append(direction)
                elif last_row > current_row:
                    direction_count = last_row - current_row
                    direction = "u" * direction_count
                    if direction:
                        result.append(direction)
                if last_col < current_col:
                    direction_count = current_col - last_col
                    direction = "r" * direction_count
                    if direction:
                        result.append(direction)
                elif last_col > current_col:
                    direction_count = last_col - current_col
                    direction = "l" * direction_count
                    if direction:
                        result.append(direction)

                last_row, last_col = current_row, current_col
                result.append("#")
                break

    answer += "".join(result)
    result.clear()
    return answer


def main():
    print(finder("UP YOU GO") == "dddd#u#ddddrrrr#uu#ddllll#dr#drrr#")
    print(finder("UP") == "dddd#u#")


main()
