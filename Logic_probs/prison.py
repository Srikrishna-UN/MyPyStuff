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
prison_doors = [False]*100

for round_num in range(1, 101):
    for i in range(round_num, 100, round_num):
        prison_doors[i - 1] = not prison_doors[i - 1]

open_doors = []
closed_doors = []

for i in range(1, 101):
    if prison_doors[i-1]:
        open_doors.append(i)
    else:
        closed_doors.append(i)

print(open_doors)
