class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {}
        repeats = []
        for i in range(len(list1)):
            dict[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in dict:
                dict[list2[i]] += i
                repeats.append(list2[i])
        
        rest = []
        index = len(list1) + len(list2)
        for place in repeats:
            if dict[place] < index:
                rest = []
                rest.append(place)
                index = dict[place]
            elif dict[place] == index:
                rest.append(place)
        return rest