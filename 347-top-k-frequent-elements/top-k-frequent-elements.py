class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)   
        
        top_k_keys = heapq.nlargest(k, count, key=count.get)

        return top_k_keys