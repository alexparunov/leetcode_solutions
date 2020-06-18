"""
https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/

"""
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:

        data = []
        for _id, rating, vegan, price, distance in restaurants:
            if price <= maxPrice and distance <= maxDistance:
                if veganFriendly:
                    if vegan:
                        data.append((rating, _id))
                else:
                    data.append((rating, _id))

        data.sort(reverse=True)
        return [_id for rating, _id in data]
