class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
      hmap1 = {}
      hmap2 = {}
      
      for i in range(0, len(nums1)):
        if nums1[i] in hmap1.keys():
          hmap1[nums1[i]] += 1
        else:
          hmap1[nums1[i]] = 1

      for i in range(0,len(nums2)):
        if nums2[i] in hmap2.keys():
          hmap2[nums2[i]] += 1
        else:
          hmap2[nums2[i]] = 1
       
      intersection = []
      for k in hmap1.keys():
        if k in hmap2.keys():
          element_count = min(hmap1[k], hmap2[k])
          intersection.extend([k]*element_count)
          
      return intersection
          
      
          
        
       
