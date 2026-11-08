#Q4. Scope. Before running, write in a comment what you think each snippet prints, then run it and compare:
#• x = 10, then def show(): x = 5; print(x), then call show() and print(x)
#• count = 0, then def add(): count += 1, then call add() (what error do you get, and why?)
#In a comment, explain the difference between a local variable and a global variable in your own words.

x = 10

def show():
    x = 5
    print(x)

show()
print(x)


count = 0

def add():
    global count
    count += 1

add()
print(count)


