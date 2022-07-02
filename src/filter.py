'''
a script to clean the data as it might contain duplicate prject keys while scraping
'''
# open the file with potential duplicates
file = open("project_keys.txt", "r")
content_list = file.readlines()
original_length = len(content_list)

# convert the list to a set then to a list again, as sets don't keep duplicates
content_list = list(set(content_list))
new_length = len(content_list)

print("the number of duplicates which were handled: ", original_length - new_length)
print("the number of unique project keys: ", new_length)

# save the unique keys to a new file
with open(r'filtered_project_keys.txt', 'w') as fp:
    for key in content_list:
        fp.write("%s" % key)