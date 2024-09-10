def bubble_sort(products, sort_by = "rating"):
    n = len(products)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater in rating
            if products[j][sort_by] > products[j+1][sort_by]:
                products[j], products[j+1] = products[j+1], products[j]
    return products

def merge_sort(products, sort_by = "pricing"):
    n= len(products)
    if n > 1:
        # Finding the mid of the array
        mid = n//2
        # Dividing the array elements into 2 halves
        left = products[:mid]
        right = products[mid:]
        # Sorting the first half
        merge_sort(left, sort_by)
        # Sorting the second half
        merge_sort(right, sort_by)
        # Merging the two halves
        i = j = 0
        result = []
        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            # Sorting by pricing
            if left[i][sort_by] < right[j][sort_by]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Checking if any element was left
        result.extend(left[i:])
        result.extend(right[j:])
        # Copy the sorted elements back into original array
        for i in range(len(products)):
            products[i] = result[i]        
    return products

def quick_sort(products, sort_by = "popularity"):
    n = len(products)
    if n <= 1:
        return products
    else:
        pivot = products[0]
        less = []
        greater = []
        for product in products[1:]:
            if product[sort_by] <= pivot[sort_by]:
                less.append(product)
            else:
                greater.append(product)
        return quick_sort(less, sort_by) + [pivot] + quick_sort(greater, sort_by)
    

    