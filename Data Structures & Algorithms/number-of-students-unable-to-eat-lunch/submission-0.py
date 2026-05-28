class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        giro=len(students)
        rifiuti=0

        while sandwiches and rifiuti!=len(students):
            studente=students.pop(0)
            if studente==sandwiches[0]:
                sandwiches.pop(0)
                rifiuti=0
            else:
                students.append(studente)
                rifiuti+=1
        
        return len(students)