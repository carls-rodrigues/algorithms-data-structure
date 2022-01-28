class Node:
    def __init__(self, node) -> None:
        self.node = node
        self.next = None

    def __str__(self) -> str:
        data = self
        output = ""

        while data:
            output += str(data.node) + " "
            data = data.next
        return output


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def append(self, element):
        node = Node(element)
        current = None
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.length += 1

    def removeAt(self, position):
        if position > -1 and position < self.length:
            current = self.head
            previous = current
            index = 1
            if position == 0:
                self.head = current.next

            else:
                while index <= position:
                    previous = current
                    current = current.next
                    index += 1
                previous.next = current.next

            self.length -= 1


linkedList = LinkedList()
linkedList.append(5)
linkedList.append(2)
print(linkedList.head)
linkedList.removeAt(1)
print(linkedList.head)
