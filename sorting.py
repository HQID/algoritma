# Hasby Ashidiq
# F55123010
# Kelas A

# Pseudocode merge sort:
# MERGE-SORT(B, left, right):
#     if left < right:
#         mid = (left + right) // 2
#         MERGE-SORT(B, left, mid) // memanggil dirinya sendiri secara rekursif
#         MERGE-SORT(B, mid + 1, right)
#         MERGE(B, left, mid, right)

# MERGE(B, left, mid, right):
#     Membagi array B menjadi dua bagian: kiri dan kanan
#     i = 0
#     j = 0
#     k = left
#     while i < panjang(kiri) dan j < panjang(kanan):
#         if kiri[i] <= kanan[j]:
#             B[k] = kiri[i]
#             i += 1
#         else:
#             B[k] = kanan[j]
#             j += 1
#         k += 1
#     Sisa elemen dari kiri atau kanan dipindahkan ke array B

# Pseudocode bubble sort:
# BUBBLE-SORT(B):
#     for i = 0 hingga panjang(B) - 1:
#         for j = 0 hingga panjang(B) - i - 2:
#             if B[j] > B[j+1]:
#                 Tukar elemen B[j] dengan B[j+1]

import random
import time

data = []
while len(data) < 100:
    data.append(random.randint(1, 100))

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

data_copy1 = data.copy()
data_copy2 = data.copy()

start_time = time.perf_counter()
merge_sort(data_copy1)
merge_time = (time.perf_counter() - start_time) * 1000  

start_time = time.perf_counter()
bubble_sort(data_copy2)
bubble_time = (time.perf_counter() - start_time) * 1000  

print("Daftar Asli:", data)
print("Hasil Pengurutan Merge Sort:", data_copy1)
print("Waktu Pengurutan Merge Sort:", merge_time, "milidetik")
print("Hasil Pengurutan Bubble Sort:", data_copy2)
print("Waktu Pengurutan Bubble Sort:", bubble_time, "milidetik")