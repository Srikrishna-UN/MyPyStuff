"""
Andaman Prisoner Problem - There are 100 prison cells in a row. All cells are locked. Jailer is given permission by the Prime Minister of India to release any number of prisoners.
In Round 1, Jailer opens all the doors.
In Round 2, he closes every alternate door (2, 4, 6...).
In Round 3, every third door (3, 6, 9,....) if Door is Open,, he closes it. If Door is Closed, he opens it.
In Round 4, every fourth door (4, 8, 12..), if Door is open,, he closes it. If Door is Closed, he opens it.
He does this for 100 Rounds. At the end, who are the lucky prisoners ?
b) Prepare 2 letters. Letter1 to PM giving list of lucky prisoners and release date as today. Letter2 to Jailer giving list of unlucky prisoners who will be released after 4 weeks.
"""
# Initialization
prison_doors = []
open_doors = []
for _ in range(100):
    prison_doors.append(0)


def prison_iters(num):
    if num == 0:
        for i in range(num, 100):
            if prison_doors[i] == 1:
                prison_doors[i] = 0
            elif prison_doors[i] == 0:
                prison_doors[i] = 1
    else:
        for i in range(num, 100, num):
            if prison_doors[i] == 1:
                prison_doors[i] = 0
            elif prison_doors[i] == 0:
                prison_doors[i] = 1
    # for _ in prison_doors:
    #     if _ == 1:
    #         open_doors.append(prison_doors.index(_))


for z in range(100):
    prison_iters(z)

print(prison_doors)

for _ in prison_doors:
    if _ == 1:
        open_doors.append(prison_doors.index(_))

# print(open_doors)

