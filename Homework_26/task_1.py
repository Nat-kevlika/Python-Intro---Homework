class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, new_element):
        if new_element not in self.elements:
            self.elements.append(new_element)
            print(f"Added {new_element} to the list.")

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
            return f"Element {element} removed from the list"
        else:
            raise ValueError(f"Element {element} not found in the list")

    def __str__(self):
        sorted_elements = sorted(self.elements)
        return ', '.join(map(str, sorted_elements))


if __name__ == "__main__":
    inset = Inset()

    inset.insert(10)
    inset.insert(20)
    inset.insert(30)
    inset.insert(40)
    inset.insert(50)

    print("Checking members:")
    print(f"Is 20 in list? - {inset.member(20)}")
    print(f"Is 70 in list? - {inset.member(70)}")
    print(f"Is 80 in list? - {inset.member(80)}")
    print("")

    print("Removing element:")
    try:
        print(inset.remove(30))
    except ValueError as e:
        print(e)
    print("")

    print("Trying to remove element:")
    try:
        print(inset.remove(60))
    except ValueError as e:
        print(e)
    print("")

    print("Final list:")
    print(inset)
