my_file = open("E:\GitHub\EventNotifier\categories.txt", "r")
content = my_file.read()
print(content)

content_list = content.splitlines()
for cat in content_list:
    cat_file =open("E:\GitHub\EventNotifier\{}.txt".format(cat))
    cat_list = cat_file.read()
    print(cat_list)
my_file.close()