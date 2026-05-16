class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visitaattuale=set()
        preMap={i:[] for i in range(numCourses)}
        for corso,pre in prerequisites:
            preMap[corso].append(pre)

        def ricorsione(corso):
            if corso in visitaattuale:
                return False
            if preMap[corso] == []:
                return True
            visitaattuale.add(corso)
            for pre in preMap[corso]:
                if not ricorsione(pre):
                    return False
            visitaattuale.remove(corso)
            preMap[corso]=[]
            return True

        for corso in range(numCourses):
            if not ricorsione(corso):
                return False
        return True