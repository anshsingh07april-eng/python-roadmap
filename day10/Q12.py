#Q12. Tower of Hanoi. There are three rods A, B, C and n disks on A. Move all disks to C, one at a time, never putting a bigger disk on a smaller one. Write hanoi(n, source, target, helper) that prints each move, like Move disk 1 from A to C. Test with n = 3 (it should print 7 moves).
def hanoi(n, source, target, helper):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n - 1, source, helper, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n - 1, helper, target, source)

n = 3
hanoi(n, "A", "C", "B")
print(f"Total moves for {n} disks: {2**n - 1}")
prompt = int(input("Enter the number of disks for Tower of Hanoi: "))
hanoi(prompt, "A", "C", "B")
print(f"Total moves for {prompt} disks: {2**prompt - 1}")