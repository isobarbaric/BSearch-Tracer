
import pandas as pd

class BinarySearch:

    def __init__(self) -> None:
        pass

    def __bsearch(nums: list, target: int, left: int, right: int, path: list) -> list:
        """Performs binary search given a list and target

        :param nums: a list of sorted numbers
        :type nums: list
        :param target: the value looked for in the nums
        :type target: int
        :param left: the value of the left pointer in bsearch
        :type left: int
        :param right: the value of the right pointer in bsearch
        :type right: int
        :param path: the values of the l, r pointers seen so far
        :type path: list
        :return: the entire path list, tracing the left and right pointers throughout the bsearch
        :rtype: list
        """
        path.append([left, right])

        if left > right:
            return path

        mid = (left + right) // 2

        if nums[mid] == target:
            return path
        elif nums[mid] < target:
            return BinarySearch.__bsearch(nums, target, mid+1, right, path)
        else:
            return BinarySearch.__bsearch(nums, target, left, mid-1, path)

    def trace(nums: list, target: int) -> list:
        '''Traces binary search to provide information on how binary search

        :param nums: a list of sorted numbers
        :type nums: list
        :param target: the value looked for in the nums
        :type target: int
        '''
        nums.sort()
        path = BinarySearch.__bsearch(nums, target, 0, len(nums)-1, [])

        logic_flow = []

        for step in path:
            mid = (step[0]+step[1]) // 2

            outcome = ''
            if nums[mid] > target:
                outcome = "> target"
            elif nums[mid] < target:
                outcome = "< target"
            else:
                outcome = "= target"

            logic_flow.append({
                'left': step[0],
                'right': step[1],
                'value': nums[mid],
                'outcome': outcome
            })

        df = pd.DataFrame.from_records(logic_flow)
        df.index += 1
        name = f"Binary Search, target = {target}"

        # use MultiIndex to add a header
        df.columns = pd.MultiIndex.from_product([[name], df.columns])

        return df