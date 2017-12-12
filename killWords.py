import os

word_file = open("world_file",'r')
word_file_list = []

for line in world_file.readlines():
	word_file_list.append(line.splite(" "))

world_file.close()

ass_file = open("ass_file","r")
unknow_word_list = []

for line in ass_file.readlines():
	unknow_word_list.append(line.splite(" "))

ass_file.close()

new_word_list = []

for i in range(unknow_word_list.length):
	if unknow_word_list[i] not in word_file_list:
		new_word_list.append(unknow_word_list[i])

print(unknow_word_list)