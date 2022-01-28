class Node {
  node;
  next;
  constructor(node) {
    this.node = node;
    this.next = null
  }

  toString() {
    let head = this
    let output = ''

    while (head) {
      output += `${head.node} `
      head = head.next
    }
    console.log(output.trim())
  }
}

class LinkedList {
  head
  length
  constructor() {
    this.head = null;
    this.length = 0;
  }

  append(element) {
    let node = new Node(element), current;
    if (!this.head) {
      this.head = node
    } else {
      current = this.head;
      while (current.next) {
        current = current.next
      }
      current.next = node
    }
    this.length++;
  }
  insertAt(position, element) {
    if (position >= 0 && position <= this.length) {
      let node = new Node(element), current = this.head, previous, index = 0;
      if (position === 0) {
        node.next = current;
        this.head = node;
      } else {
        while (index++ < position) {
          previous = current;
          current = current.next
        }
        node.next = current;
        previous.next = node
      }
      this.length++;
      return true;
    } else {
      return false;
    }
  }

  removeAt(position) {
    if (position > -1 && position < this.length) {
      let current = this.head, previous, index = 0;
      if (position === 0) {
        this.head = current.next;
      } else {
        while (index++ < position) {
          previous = current
          current = current.next
        }
        previous.next = current.next;
      }
      this.length--;
    }
  }

}

const linkedList = new LinkedList()
linkedList.append(5)
linkedList.append(4)
linkedList.insertAt(1, 2)
linkedList.head.toString()
linkedList.removeAt(1)
linkedList.head.toString()