

def merge(arr):
    if len(arr) > 1:
        m = len(arr)//2
        arr1 = arr[:m]
        arr2 = arr[m:]

        merge(arr1)
        merge(arr2)

        i = j = k = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1

            else:
                arr[k] = arr2[j]
                j += 1
            k += 1

        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1

        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1


arr = [int(x) for x in input("Input Array: ").split()]
merge(arr)
print(arr)
