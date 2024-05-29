class Queue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, new_element):
        self.elements.append(new_element)
        print(f"Added {new_element} to the queue.")

    def pop(self):
        if self.is_empty():
            raise ValueError("Cannot remove from an empty queue")

        removed_element = self.elements.pop(0)
        print(f"Element {removed_element} removed from the queue")
        return removed_element


if __name__ == "__main__":
    q = Queue()

    q.insert(1)
    q.insert(2)
    q.insert(3)

    print("\nRemoving elements:")
    print(q.pop())
    print(q.pop())
    print(q.pop())

    print("\nTrying to remove element:")
    try:
        print(q.pop())
    except ValueError as e:
        print("Error:", e)
