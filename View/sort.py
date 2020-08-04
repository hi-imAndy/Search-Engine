

def partition(nums, low, high):
    pivot = nums[(low + high) // 2].getKoeficijent_rangiranja()     #Sortira se na osnovu proizvoda koeficijenta i broja pronadjenih reci
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i].getKoeficijent_rangiranja()> pivot:
            i += 1

        j -= 1
        while nums[j].getKoeficijent_rangiranja() < pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(lista):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(lista, 0, len(lista) - 1)
