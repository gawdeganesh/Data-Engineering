def CountFrequency(my_list):
	dict = { ele : my_list.count(ele) for ele in my_list}
	return dict




# Driver function
if __name__ == "__main__":
	my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

	print(CountFrequency(my_list))
