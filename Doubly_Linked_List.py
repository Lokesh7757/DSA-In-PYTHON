class Node:
    def __init__(self, data):
        self.data = data  # Store data in the node
        self.next = None  # Pointer to the next node in the list
        self.prev = None  # Pointer to the previous node in the list


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    # Insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning of the list")

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end of the list")
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        print(f"Inserted {data} at the end of the list")

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # If the head node holds the key to be deleted
        if temp is not None and temp.data == key:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            print(f"Deleted node with value {key}")
            return

        # Search for the key to be deleted
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next

        # If the key was not present in the list
        if temp is None:
            print(f"Node with value {key} not found")
            return

        # Unlink the node from the linked list
        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

        temp = None
        print(f"Deleted node with value {key}")

    # Search for a node by value
    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                print(f"Found node with value {key}")
                return True
            current = current.next

        print(f"Node with value {key} not found")
        return False

    # Display the linked list
    def display(self):
        if self.head is None:
            print("The list is empty")
            return

        current = self.head
        print("Linked list contents:", end=" ")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Main function to interact with the user
def main():
    dll = DoublyLinkedList()

    while True:
        print("\nChoose an operation:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete Node")
        print("4. Search for a Value")
        print("5. Display List")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            data = input("Enter the value to insert at the beginning: ")
            dll.insert_at_beginning(data)
        elif choice == '2':
            data = input("Enter the value to insert at the end: ")
            dll.insert_at_end(data)
        elif choice == '3':
            key = input("Enter the value of the node to delete: ")
            dll.delete_node(key)
        elif choice == '4':
            key = input("Enter the value to search for: ")
            dll.search(key)
        elif choice == '5':
            dll.display()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")


# Run the main function
if __name__ == "__main__":
    main()
