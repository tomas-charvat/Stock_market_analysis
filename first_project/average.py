def average(numbers) ->float:
    i=0
    total=0
    for number in numbers:
        total+=number
        i=i+1
    return total/i


print(average([1,2,3,4,13]))