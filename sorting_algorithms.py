from abc import ABC, abstractmethod

class SortingAlgorithm(ABC):
    @abstractmethod
    def sort(self, data, key, reverse=False):
        pass

class BubbleSort(SortingAlgorithm):
    def sort(self, data, key, reverse=False):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (data[j][key] > data[j + 1][key]) != reverse:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

class MergeSort(SortingAlgorithm):
    def sort(self, data, key, reverse=False):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.sort(left_half, key, reverse)
            self.sort(right_half, key, reverse)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if (left_half[i][key] < right_half[j][key]) != reverse:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
        return data
