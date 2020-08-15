"""
https://leetcode.com/problems/angle-between-hands-of-a-clock/

"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_in_hour_minute = 360 / (12 * 60)
        angle_in_minute = 360 // 60

        angle_of_hour = (hour * angle_in_hour_minute * 60 + minutes * angle_in_hour_minute) % 360
        angle_of_minutes = minutes * angle_in_minute

        diff_angle = abs(angle_of_hour - angle_of_minutes)

        return min(diff_angle, 360 - diff_angle)
