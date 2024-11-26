class Student:
    def __init__(self, student_id, name, python_score, math_score, big_data_score):
        self.student_id = student_id
        self.name = name
        self._python_score = python_score
        self._math_score = math_score
        self._big_data_score = big_data_score

    @property
    def python_score(self):
        return self._python_score

    @python_score.setter
    def python_score(self, score):
        self._python_score = score

    @property
    def math_score(self):
        return self._math_score

    @math_score.setter
    def math_score(self, score):
        self._math_score = score

    @property
    def big_data_score(self):
        return self._big_data_score

    @big_data_score.setter
    def big_data_score(self, score):
        self._big_data_score = score

    def get_average_score(self):
        return (self._python_score + self._math_score + self._big_data_score) / 3
    
    ######### 542313460109 胡华吉  ###############
    
student = Student("001", "Alice", 85, 90, 88)
print("平均成绩:", student.get_average_score())

student.python_score = 95  # 修改Python成绩
print("修改后的平均成绩:", student.get_average_score())

