import sys
import timeit
import requests
import matplotlib.pyplot as plt

sys.setrecursionlimit(200000)

def func1(arr, low, high):
    stack = [(low, high)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = func2(arr, low, high)
            stack.append((low, pi-1))
            stack.append((pi+1, high))

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"  # Replace with the URL of the API endpoint
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Error: API returned status code ", response.status_code)

# Initialize lists to hold data for scatter plot
x_data = []  # Length of subarray
y_data = []  # Execution time

# Measure execution time for each subarray
for i in range(len(data)):

    secs = timeit.timeit(stmt = "func1(data[i], 0, len(data[i])-1)",globals=globals(), number=1)
    x_data.append(len(data[i]))
    y_data.append(secs)
    
    
# Create scatter plot
plt.scatter(x_data, y_data)
plt.title("Execution Time vs. Subarray Length")
plt.xlabel("Subarray Length")
plt.ylabel("Execution Time (s)")
plt.show()
