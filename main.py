# a = 4235
# b = 8313

# def runningSum(a,b):
#   sum = 0;

#   for i in range(a,b+1):
#     if (i % 2 == 1 ):
#       # print(i)
#       sum +=i

#   return sum

# print("Sum is:", runningSum(a,b))

# Write and open a file #

file = open('test.txt', 'r')
newFile = open('output.txt', 'w')
# print(file.read())

# print(file.readlines()[1:2])
counter = 0
for line in file:
  if counter % 2 == 1:
    print(line)
    newFile.write(line)
  counter += 1

# print("Counter:", counter)
newFile.close()
