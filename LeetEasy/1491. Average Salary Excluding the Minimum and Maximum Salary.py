class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        # Find the sum and subtract it by minimum and maximum element than divite by 
        # length-2(because minimum anf maximum salary are excruded/not included)
        # return float((sum(salary)-max(salary)-min(salary))/(len(salary)-2))

        
        #      Another approach is sorting
        # Sort the given array
        salary.sort()
        # Calculate the total salary from first last-1 index and divide by length-2
        return sum(salary[1:-1])/float(len(salary)-2)