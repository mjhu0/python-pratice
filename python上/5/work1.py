import json
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        try:
            with open('students.json', 'r') as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = []

    def save_data(self):
        with open('students.json', 'w') as f:
            json.dump(self.students, f)

    def add_student(self):
        name = input("请输入学生姓名: ")
        score = float(input("请输入学生成绩: "))
        self.students.append({'name': name, 'score': score})
        self.save_data()
        print("学生信息添加成功。")

    def find_student(self):
        name = input("请输入要查找的学生姓名: ")
        for student in self.students:
            if student['name'] == name:
                print(f"姓名: {student['name']}, 成绩: {student['score']}")
                return
        print("未找到该学生。")

    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")
        for student in self.students:
            if student['name'] == name:
                self.students.remove(student)
                self.save_data()
                print("学生信息删除成功。")
                return
        print("未找到该学生。")

    def modify_student(self):
        name = input("请输入要修改的学生姓名: ")
        for student in self.students:
            if student['name'] == name:
                new_score = float(input("请输入新的成绩: "))
                student['score'] = new_score
                self.save_data()
                print("学生信息修改成功。")
                return
        print("未找到该学生。")

    def sort_students(self):
        self.students.sort(key=lambda x: x['score'])
        print("学生信息已按成绩排序。")

    def count_students(self):
        print(f"总学生人数: {len(self.students)}")

    def display_all_students(self):
        if not self.students:
            print("没有学生信息。")
        else:
            for student in self.students:
                print(f"姓名: {student['name']}, 成绩: {student['score']}")

    def run(self):
        while True:
            print("*************学生信息管理系统*************")
            print("1: 录入学生信息")
            print("2: 查找学生信息")
            print("3: 删除学生信息")
            print("4: 修改学生信息")
            print("5: 对学生进行排序")
            print("6: 统计学生总人数")
            print("7: 显示所有学生信息")
            print("8: 退出系统")
            print("**************************************")
            choice = input("请选择功能: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.find_student()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.modify_student()
            elif choice == '5':
                self.sort_students()
            elif choice == '6':
                self.count_students()
            elif choice == '7':
                self.display_all_students()
            elif choice == '8':
                print("退出系统。")
                break
            else:
                print("无效的选择，请重新输入。")

if __name__ == '__main__':
    sms = StudentManagementSystem()
    sms.run()


############   542313460109 胡华吉 ############