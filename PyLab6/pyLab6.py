# Lab 6 exercise 10

# Copy from file F1 to file F2 all lines that do not contain words
# that match the first word.Determine the number of consonants
# in the first line of file F2.
import regex


try:
    file1 = open("MySQL_fertilizer_manager.sql", "r")
    print("The first file:\n" + file1.read().strip() + "\n")
    file1.seek(0)
    first = file1.readline()
    first = first[:first.index(" ")]
    print("The first word of the first file: " + first + "\n")
    lines = []
    while line := file1.readline():
        if line.find(first) < 0:
            lines.append(line)
    file2 = open("Copy_file.txt", "w+")
    file2.writelines(lines)
    file2.seek(0)
    first = file2.readline()
    print("The first line of the second file: \n" + first.strip() + "\n")
    regs = r'(?:[b-df-hj-np-tv-xz])'
    print("Number of consonants in it: " + str(len(regex.findall(regs, first.lower()))))
    file1.close()
    file2.close()

except Exception as e:
    print(e)
