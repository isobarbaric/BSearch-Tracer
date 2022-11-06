
class BinarySearch:

    def __init__(self) -> None:
        pass

    # returns index of element using binary search
    def __binary_search(self, nums: list, target: int, low: int, high: int, path: list) -> list:
        # NOTE: whether or not the number was found successfully or not is basically just checking if the L and R are out of order in the last tuple

        path.append([low, high])

        if low > high:
            return path

        mid = (low + high) // 2

        if nums[mid] == target:
            return path
        elif nums[mid] < target:
            return self.__binary_search(nums, target, mid+1, high, path)
        else:
            return self.__binary_search(nums, target, low, mid-1, path)

    def find_path(self, nums: list, target: int) -> list:
        nums.sort()
        return self.__binary_search(nums, target, 0, len(nums)-1, [])