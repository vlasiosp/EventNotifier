my_file = open("E:\GitHub\EventNotifier\categories.txt", "r")
content = my_file.read()
content_list = content.splitlines()
cat_file =open("E:\GitHub\EventNotifier\{}.txt".format(content_list[0]), "r")
category=cat_file.read()
cat_list = category.splitlines()
print(cat_list)
cat_file.close()
my_file.close()


