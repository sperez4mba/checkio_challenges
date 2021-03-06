#Your optional code here
#You can import some modules or create additional functions
class NonUnique:
    def checkio(self,data):
        #Your code here
        #It's main function. Don't remove this function
        #It's using for auto-testing and must return a result for check.
        
        d = []
        for n in range(len(data)):
            c = data.count(data[n])
            if c > 1:
                d.append(data[n])
        #replace this for solution
        return d

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#or remove elements from original list (but it's bad practice for many real cases)
#Loop over original list


#These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == "__main__":
#     assert isinstance(checkio([1]), list), "The result must be a list"
#     assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
#     assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
#     assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
#     assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
