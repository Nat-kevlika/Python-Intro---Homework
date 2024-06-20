def middle_point(x1, y1, x2, y2):
    middle_x = (x1 + x2) / 2
    middle_y = (y1 + y2) / 2
    return middle_x, middle_y

def main():
    my_points = (
        ((0, 1), (2, 4)),
        ((-5, 3), (2, -1)),
        ((9, 5), (7, 5))
    )

    for point1, point2 in my_points:
        print(f"Middle point of {point1} and {point2} is: {middle_point(*point1, *point2)}")

if __name__ == "__main__":
    main()
