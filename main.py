PLACE = "name"


with open("projects/turtle/mailmerge/names.txt") as file:
    names = file.readlines()
    print( names)


with open("projects/turtle/mailmerge/letter.docx", mode="r") as file1:
    letter = file1.read()
    for i in names:
        name = i.strip()
        new_letter = letter.replace(PLACE, name)
        with open(f"projects/turtle/mailmerge/{name}.docx", mode="w") as file:
            file.write(new_letter)
