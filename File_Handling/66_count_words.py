with open("sample.txt","r") as file :
    content = file.read()

word_list = content.split()
word_count = len(word_list)

print(word_count)
