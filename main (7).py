implement a functioncalled sort_students that takes a list of students object as input and sortd the list based on therir CGPA(cumulative grade point average) in descending order each students object has the following attributes:test the function,roll_number(string), and cgpa(float).test the function with different input lists of students
class students:

  def__init__(self.name.roll_number,cgpa):
  self.name-name.
 self.roll_number=roll_number
self.cgpa=cgpa

def sort_students (students_list) :
  #sort the list of students in descending order of cgpa
sorted_students=sorted(students_list,key=lamda students:students.cgpa reverse=true)
return sorted_students
#example usage:
students=[
     students("hari","A123",7,8),
students("Nadhini","A124",8,9),
students("selvi","A125",9,0),
]
sorted_students=sort_students(students)
for students in sorted_students:
  print("name:{},roll_number:{},cgpa:{}",format(student.name,student.roll_number,student.cgpa))
  
  