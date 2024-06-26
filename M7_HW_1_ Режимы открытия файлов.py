file_name = "my_text_file.txt"

with open(file_name, "r", encoding="utf-8") as file:
    file_content = file.read()
    print(file_content)


