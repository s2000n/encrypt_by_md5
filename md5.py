import hashlib
with open("input.txt", 'r',encoding="latin-1") as file_input:
    lines = file_input.readlines()
    with open('output.txt', 'w',encoding="latin-1") as file_output:
        count=0
        for line in lines:
            count=count + 1
            snapping = line.replace("\n", "")
            md5hash = hashlib.md5(snapping.encode()).hexdigest()
            print(count)
            file_output.write(md5hash + "\n")
input("done...")