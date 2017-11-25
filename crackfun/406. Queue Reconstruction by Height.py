class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) < 2:
            return people
        people.sort(key=lambda x: (x[1], x[0]))
        for i in range(len(people)):
            j = 0
            count = 0
            while j < i:
                if people[j][0] >= people[i][0]:
                    count += 1
                if count > people[i][1]:
                    break
                j += 1
            if j < i:
                temp = people[i]
                people = people[:i] + people[i + 1:]
                people = people[:j] + [temp] + people[j:]
        return people

#-----------
class Solution(object):
    def reconstructQueue(self, people):
        if not people:
            return []
        ordered_line = []
        insertion_order = sorted(people, key = lambda (h,k): (-h,k))
        for person in insertion_order: ordered_line.insert(person[1], person)
        return ordered_line