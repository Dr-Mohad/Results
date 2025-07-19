def substring(arr,n):
    new_arr = []
    for word in arr:
        if n in word:
           new_arr.append(word)
    return new_arr
print(substring(['Mahad','Cabdullahi','yaxye'],'aha'))

