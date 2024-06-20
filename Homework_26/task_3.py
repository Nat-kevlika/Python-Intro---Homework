class ExtendedList(list):
    def min(self):
        if not self:
            raise ValueError("List is empty")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("List is empty")
        return max(self)


if __name__ == "__main__":

    list_one = ExtendedList([11, 7, 8, 3, 120])
    list_two = ExtendedList([37, 22, 123, 17, 4])

    print(f"Min value in list_one: {list_one.min()}")
    print(f"Max value in list_one: {list_one.max()}")

    print(f"Min value in list_two: {list_two.min()}")
    print(f"Max value in list_two: {list_two.max()}")

    empty_list = ExtendedList([])
    try:
        print(f"Min value in empty_list: {empty_list.min()}")
    except ValueError as e:
        print(f"Error: {e}")