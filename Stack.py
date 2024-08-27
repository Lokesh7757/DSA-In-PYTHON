class Stack:
    def __init__(self):
        self.stack = []

    # Push operation: Add an element to the top of the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack")

    # Pop operation: Remove and return the top element of the stack
    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped {item} from the stack")
            return item
        else:
            print("Stack is empty! Cannot pop.")
            return None

    # Peek operation: Return the top element of the stack without removing it
    def peek(self):
        if not self.is_empty():
            print(f"Top of the stack is {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty! Cannot peek.")
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Get the size of the stack
    def size(self):
        return len(self.stack)

    # Display the elements of the stack
    def display(self):
        print("Stack contents:", self.stack)


# Main function to interact with the user
def main():
    stack = Stack()

    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Size")
        print("6. Check if Empty")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            item = input("Enter the item to push onto the stack: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            print(f"Stack size: {stack.size()}")
        elif choice == '6':
            print(f"Is stack empty? {'Yes' if stack.is_empty() else 'No'}")
        elif choice == '7':
            print("Exiting the program.")

            
            break
        else:
            print("Invalid choice! Please select a valid option.")


# Run the main function
if __name__ == "__main__":
    main()
