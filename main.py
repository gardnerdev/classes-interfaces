from sre_constants import SRE_FLAG_IGNORECASE


class SimpleGradebook:
    def __init__(self):
        self._grades = {}
    def add_student(self, name: str) -> dict:
        self._grades[name] = []
    def report_grades(self, name: str, score: int) -> dict:
        self._grades[name].append(score)
    
    def average_grade(self,name: str) -> int:
        grades = self._grades[name]
        return sum(grades) / len(grades)


if __name__ == "__main__":
    book = SimpleGradebook()
    book.add_student('Issac Newton')
    book.report_grades('Issac Newton', 5)
    book.report_grades('Issac Newton', 6)
    
    print(book.average_grade('Issac Newton'))
    