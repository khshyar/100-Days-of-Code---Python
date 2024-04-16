with open("starting_letter.txt") as file_letter:

    data_letter = file_letter.read()


with open("invited_names.txt") as file_name:
    data_name = file_name.readlines()

    for name in data_name:
        stripped_name = name.strip()
        new_letter = data_letter.replace("[name]", stripped_name)
        with open(f"{stripped_name}.txt", mode="w") as final_version:
            final_version.write(new_letter)
