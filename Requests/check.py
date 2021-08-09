def countingValleys(steps, path):
    # Write your code here
    counting_valleys = 0
    total_count = 0
    in_ground = 0
    for p in path:
        if p == "D":
            total_count -= 1
        if p == "U":
            total_count += 1
        if total_count == 0:
            in_ground += 1
            if in_ground % 2 == 0:
                counting_valleys += 1
    return counting_valleys


name = "swagata dutta"

names = name.split(" ")
print(names)
fullname = " ".join([n.capitalize() for n in names])
print(fullname)
