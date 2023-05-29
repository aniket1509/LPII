def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    numbers = input("Enter a list of numbers, separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    sorted_numbers = selection_sort(numbers)    
    print("Sorted list:", sorted_numbers)

if __name__ == "__main__":
    main()