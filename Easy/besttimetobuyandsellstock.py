class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        start=prices[0]
        if len(prices)==0:
            return None
        for i in range(1,len(prices)):
            if ((prices[i])-start)<0:
                start=prices[i]
            elif ((prices[i]-start))>profit:
                profit=(prices[i]-start)
        return profit
            
            