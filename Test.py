def removeDuplicate(self):
    # Current will point to head
    current = self.head;
    if (self.head == None):
        print("List is empty");
    else:
        while (True):
            # Temp will point to previous node of index.
            temp = current;
            # Index will point to node next to current
            index = current.next;
            while (index != self.head):
                # If current node is equal to index data
                if (current.data == index.data):
                    # Here, index node is pointing to the node which is duplicate of current node
                    # Skips the duplicate node by pointing to next node
                    temp.next = index.next;
                else:
                    # Temp will point to previous node of index.
                    temp = index;
                index = index.next;
            current = current.next;
            if (current.next == self.head):
                break;
