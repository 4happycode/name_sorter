import os
path = str(os.getcwd()+'/')


def getData(filename):
	read = open(path+filename, 'r+').readlines()
	data = [row.replace('\n','') for row in read]

	return data

def sortData(list_data):
	list_data.sort(key=lambda s: s.split()[-1])

	return list_data

def saveValue(sort_value):
	if sort_value :
		with open('sorted-names-list.txt', 'w') as f:
			for item in sort_value:
				f.write("%s\n" % item)
		message = 'List Of Data Has Been Saved'
	else:
		message = 'List Of Data Could Not Be Saved'

	return message

# Get List Data
list_data = getData('unsorted-names-list.txt')
print('Unsorted Data : ', list_data, '\n')

# Sorting Values
sort_value = sortData(list_data)
print('Sorted Data : ', sort_value, '\n')

# Saving List Data
save_data = saveValue(sort_value)
print(save_data)