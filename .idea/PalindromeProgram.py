# stack1=[]
# stack1.append(3)
# stack1.append(4)
# stack1.append(50)
# print(stack1)
def is_palindrome_stack(s):
    # Preprocess: remove spaces and make lowercase
    s = s.replace(" ", "").lower()
    s=s.replace(",","")
    s=s.replace(".","")
    s=s.replace("!","")
    s=s.replace("-","")
    s=s.replace(" "" ","")
    s=s.replace("?","")
    stack = []

    # Push all characters to the stack
    for char in s:
        stack.append(char)

    # Pop characters and compare with the original
    for char in s:
        if char != stack.pop():
            return False

    return True

# Example usage
text = input("Enter any word or phrase: ")
if is_palindrome_stack(text):
    print("Yes, that's a  palindrome!")
else:
    print("The word you have entered is not a palindrome!")



