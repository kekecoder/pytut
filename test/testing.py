from user import get_formatted_name

print("Enter 'q' at anytime to quit.")

while True:
    first = input("\nPlease give me your firstname: ")
    if first == 'q':
        break
    last = input("Please give me your lastname: ")
    if last == 'q':
        break

    formatted_text = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_text + ".")
