def pair_sum(arr,sum):
    for i in range(len(arr)):
         for j in range(i + 1, len(arr)):
             if arr[i] + arr[j] == sum:
                 print("true")
           
pair_sum([1,2,3,3,5],8)
        

