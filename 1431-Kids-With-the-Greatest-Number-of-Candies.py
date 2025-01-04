from typing import List

def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    biggest_candy = max(candies)
    final_list = []
    i = 0
    while i < len(candies):
        if candies[i] + extraCandies >= biggest_candy:
            final_list.append(True)
        else:
            final_list.append(False)
        i += 1

    return final_list


def kidsWithCandies2(self, candies: List[int], extraCandies: int) -> List[bool]:
    final_list = []
    max_candies = max(candies)

    for candy in candies:
        final_list.append(candy + extraCandies >= max_candies)
    return final_list

    
