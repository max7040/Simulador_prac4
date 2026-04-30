def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i+=1
        else:
            result.append(right[j]); j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def counting_sort(arr):
    arr = list(map(int, arr))
    max_val = max(arr)
    count = [0]*(max_val+1)
    for num in arr:
        count[num]+=1
    result=[]
    for i,c in enumerate(count):
        result.extend([i]*c)
    return result

def radix_sort(arr):
    arr = list(map(str, arr))
    max_len = max(len(x) for x in arr)
    for i in range(max_len-1, -1, -1):
        buckets = [[] for _ in range(256)]
        for item in arr:
            char = ord(item[i]) if i < len(item) else 0
            buckets[char].append(item)
        arr = [item for bucket in buckets for item in bucket]
    return arr
