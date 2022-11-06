
# from visualizer import Pathfinder

# rn = Pathfinder()
# rn.run()

from binary_search import BinarySearch

import pandas as pd

bsearch = BinarySearch()

nums = [1, 10, 26, 83, 125, 639, 2432]

logic_flow = []

for step in bsearch.find_path(nums, 35):
    logic_flow.append({'l': step[0],
        'r': step[1],
        'value': nums[(step[0]+step[1])//2]
    })

print(pd.DataFrame.from_records(logic_flow))