def max_num(head, sequence):
    for i in sequence:
        if i > head:
            return i


def min_num(head, sequence):
    for i in range(len(sequence) - 1, -1, -1):
        if sequence[i] < head:
            return sequence[i]


def C_LOOK(N, head, sequence):
    seek_sequence = []
    stop_condition = min_num(head, sequence)
    seek_operations = 0
    seek_sequence.append(head)
    near_num = max_num(head, sequence)
    for i in range(len(sequence)):
        if near_num > head:
            difference = near_num - head
            seek_operations += difference
            head = near_num
            seek_sequence.append(head)
            near_num = max_num(head, sequence)
            if head == stop_condition:
                break
        if head == max(sequence):
            difference = head - min(sequence)
            head = min(sequence)
            near_num = max_num(head, sequence)
            seek_operations += difference
            seek_sequence.append(head)
    print("Seek Sequence : 	", end=" ")
    for i in seek_sequence:
        if i == stop_condition:
            print(i)
        else:
            print(i, " ==> ", end=" ")
    return seek_operations


if __name__ == "__main__":
    Number_disk = int(input("Enter the number of disks:	"))
    if Number_disk > 0:
        head = int(input("Enter initial header position : 	"))
        while not head in range(Number_disk + 1):
            head = int(input("Please enter valid initial head position :"))
        sequence = []
        sequence = list(map(int, input("Enter the sequence : 	").split()))
        sequence.sort()
        if min(sequence) < 0 or max(sequence) > Number_disk:
            print("Sequence out of range")
            exit(0)

        seek_operations = C_LOOK(Number_disk, head, sequence)
        print("Total number of seek operations : ", seek_operations)