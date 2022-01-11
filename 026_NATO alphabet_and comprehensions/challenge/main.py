with open('file1.txt', 'r') as f1:
    data1 = [int(num.strip()) for num in f1.readlines()]

with open('file2.txt', 'r') as f2:
    data2 = [int(num.strip()) for num in f2.readlines()]

result = [num for num in data1 if num in data2]
print(result)