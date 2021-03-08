# cases where they cannot overlap:
# E >= C or A >= G or F >= D or B >= H i.e. return 0 in those cases
# otherwise they do overlap
# could it be simpy
# (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))

# (3 - 0) *  

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: 
        int, H: int) -> int:
        rect1_area = (C-A) * (D-B)
        rect2_area = (G-E) * (H-F)
        if E >= C or A >= G or F >= D or B >= H:
            # no intersetion so just sum of two areas
            return rect1_area + rect2_area
        # otherwise it is the sum of intersection plus non intersecting areas
        intersection_area = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        return intersection_area + (rect1_area-intersection_area) + 
            (rect2_area-intersection_area)
