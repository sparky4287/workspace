def median(test_list):
    sorted_list = sorted(test_list)
    list_length = len(sorted_list)
    print sorted_list
    if list_length % 2 == 0:
	answer = (sorted_list[list_length/2-1] + sorted_list[list_length/2])/2
	print answer
    else:
	answer = sorted_list[int(list_length/2)]
	print answer
median([1,2,3,4,9,8,6])
