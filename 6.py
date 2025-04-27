list_num = []
x, y, z = input().split()
list_num.append(int(x))
list_num.append(int(y))
list_num.append(int(z))
nums = input().list()
count = 0
diff = set(list_num) - set(nums)
print(len(diff))