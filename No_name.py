#Get all index of a value in a list
l = [1,2,3,1,1]
[index for index, value in enumerate(l) if value == 1] #find all index of 1 in list l

#Get all index of a value in a list use numpy
values = np.array([1,2,3,1,2,4,5,6,3,2,1])
searchval = 3
ii = np.where(values == searchval)[0] # [0] because ii = (arr[],...)
