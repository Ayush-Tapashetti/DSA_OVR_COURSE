

undo_stack = []
redo_stack = []
current_text = ""

def write_text(new_text):
    global current_text
    undo_stack.append(current_text)
    redo_stack.clear()          # new action invalidates redo history
    current_text = new_text
    print(f"Typed: '{current_text}'")

def undo():
    global current_text
    if not undo_stack:
        print("Cannot Undo! History is empty.")
        return
    redo_stack.append(current_text)
    current_text = undo_stack.pop()
    print(f"Undo performed -> Current: '{current_text}'")

def redo():
    global current_text
    if not redo_stack:
        print("Cannot Redo! No undone actions.")
        return
    undo_stack.append(current_text)
    current_text = redo_stack.pop()
    print(f"Redo performed -> Current: '{current_text}'")

print(" User Typing Actions ")
write_text("A")
write_text("AB")
write_text("ABC")

print("\n Undo Operations ")
undo()   # back to "AB"
undo()   # back to "A"

print("\n Redo Operations ")
redo()   # forward to "AB"

print("\n New Action (Deleted the Redo History)")
write_text("ABD")

print("\nAttempt Redo After New Action ")
redo()   # Cannot Redo! (redo_stack was cleared by write_text)

print("\n Undo to Previous")
undo()   # back to "AB"
