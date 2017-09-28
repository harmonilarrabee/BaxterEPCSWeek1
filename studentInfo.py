import random

def main():
  firstNames = [
    "James",
    "John",
    "Robert",
    "Michael",
    "William",
    "David",
    "Richard",
    "Joseph",
    "Thomas",
    "Charles",
    "Christopher",
    "Daniel",
    "Matthew",
    "Anthony",
    "Donald",
    "Mark",
    "Paul",
    "Steven",
    "Andrew",
    "Kenneth",
    "George",
    "Joshua",
    "Kevin",
    "Brian",
    "Edward",
    "Ronald",
    "Timothy",
    "Jason",
    "Jeffrey",
    "Ryan",
    "Gary",
    "Jacob",
    "Nicholas",
    "Eric",
    "Stephen",
    "Jonathan",
    "Larry",
    "Justin",
    "Scott",
    "Frank",
    "Brandon",
    "Raymond",
    "Gregory",
    "Benjamin",
    "Samuel",
    "Patrick",
    "Alexander",
    "Jack",
    "Dennis",
    "Jerry",
    "Mary",
    "Patricia",
    "Jennifer",
    "Elizabeth",
    "Linda",
    "Barbara",
    "Susan",
    "Jessica",
    "Margaret",
    "Sarah",
    "Karen",
    "Nancy",
    "Betty",
    "Lisa",
    "Dorothy",
    "Sandra",
    "Ashley",
    "Kimberly",
    "Donna",
    "Carol",
    "Michelle",
    "Emily",
    "Amanda",
    "Helen",
    "Melissa",
    "Deborah",
    "Stephanie",
    "Laura",
    "Rebecca",
    "Sharon",
    "Cynthia",
    "Kathleen",
    "Amy",
    "Shirley",
    "Anna",
    "Angela",
    "Ruth",
    "Brenda",
    "Pamela",
    "Nicole",
    "Katherine",
    "Virginia",
    "Catherine",
    "Christine",
    "Samantha",
    "Debra",
    "Janet",
    "Rachel",
    "Carolyn",
    "Emma",
    ]

  lastNames = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
    "Anderson",
    "Thomas",
    "Jackson",
    "White",
    "Harris",
    "Martin",
    "Thompson",
    "Garcia",
    "Martinez",
    "Robinson",
    "Clark",
    "Rodriguez",
    "Lewis",
    "Lee",
    "Walker",
    "Hall",
    "Allen",
    "Young",
    "Hernandez",
    "King",
    "Wright",
    "Lopez",
    "Hill",
    "Scott",
    "Green",
    "Adams",
    "Baker",
    "Gonzalez",
    "Nelson",
    "Carter",
    "Mitchell",
    "Perez",
    "Roberts",
    "Turner",
    "Phillips",
    "Campbell",
    "Parker",
    "Evans",
    "Edwards",
    "Collins",
    "Stewart",
    "Sanchez",
    "Morris",
    "Rogers",
    "Reed",
    "Cook",
    "Morgan",
    "Bell",
    "Murphy",
    "Bailey",
    "Rivera",
    "Cooper",
    "Richardson",
    "Cox",
    "Howard",
    "Ward",
    "Torres",
    "Peterson",
    "Gray",
    "Ramirez",
    "James",
    "Watson",
    "Brooks",
    "Kelly",
    "Sanders",
    "Price",
    "Bennett",
    "Wood",
    "Barnes",
    "Ross",
    "Henderson",
    "Coleman",
    "Jenkins",
    "Perry",
    "Powell",
    "Long",
    "Patterson",
    "Hughes",
    "Flores",
    "Washington",
    "Butler",
    "Simmons",
    "Foster",
    "Gonzales",
    "Bryant",
    "Alexander",
    "Russell",
    "Griffin",
    "Diaz",
    "Hayes",
    ]

  students = [
  ]
  
  for i in range(0,100):
    students.append(Student(random.choice(lastNames), random.choice(firstNames), random.randint(1,100), random.randint(45,136), random.randint(152,198)))

  printHeader()
  selection = int(getUserSelection())
  if selection == 0:
    printStudentsByAge(students)
  elif selection == 1:
    printStudentsByLName(students)
  elif selection == 2:
    printStudentsByFName(students)
  elif selection == 3:
    printStudentsByHeight(students)
  elif selection == 4:
    printStudentsByWeight(students)
  elif selection == 5:
    printSumAge(students)
  elif selection == 6:
    printAvgAge(students)
  elif selection == 7:
    printSumHeight(students)
  elif selection == 8:
    printAvgHeight(students)
  elif selection == 9:
    printSumWeight(students)
  elif selection == 10:
    printAvgWeight(students)
  else:
    print ("SELECTION NOT RECOGNIZED")

class Student:
  def __init__(self, lastName, firstName, age, height, weight):
    self.lastName = lastName
    self.age = age
    self.firstName = firstName
    self.height = height
    self.weight = weight

inputQuestions = [ 
  "For STUDENTS BY AGE, type 0",
  "For STUDENTS BY LAST NAME, type 1",
  "For STUDENTS BY FIRST NAME, type 2",
  "For STUDENTS BY HEIGHT, type 3",
  "For STUDENTS BY WEIGHT, type 4",
  "For SUM of STUDENT AGES type 5",
  "For AVERAGE of STUDENT AGES type 6",
  "For SUM of STUDENT HEIGHTS type 7",
  "For AVERAGE of STUDENT HEIGHTS type 8",
  "For SUM of STUDENT WEIGHTS type 9",
  "For AVERAGE of STUDENT WEIGHTS type 10",
]

def getUserSelection():
  print (inputQuestions[0])
  print (inputQuestions[1])
  print (inputQuestions[2])
  print (inputQuestions[3])
  print (inputQuestions[4])
  print (inputQuestions[5])
  print (inputQuestions[6])
  print (inputQuestions[7])
  print (inputQuestions[8])
  print (inputQuestions[9])
  print (inputQuestions[10])
  return input("Type selection and press enter: ")

def printHeader():
    print("Student Information")

def printStudentsByAge(students):
  print ("-----Students By Age-----")
  sortStudents = sorted(students, key=lambda student: student.age)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + ", " + str(student.height) + ", " + str(student.weight))

def printStudentsByLName(students):
  print ("-----Students By First Name-----")
  sortStudents = sorted(students, key=lambda student: student.lastName)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + ", " + str(student.height) + ", " + str(student.weight))

def printStudentsByFName(students):
  print ("-----Students By Last Name-----")
  sortStudents = sorted(students, key=lambda student: student.firstName)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + ", " + str(student.height) + ", " + str(student.weight))

def printStudentsByHeight(students):
  print ("-----Students By Height-----")
  sortStudents = sorted(students, key=lambda student: student.height)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + ", " + str(student.height) + ", " + str(student.weight))

def printStudentsByWeight(students):
  print ("-----Students By Weight-----")
  sortStudents = sorted(students, key=lambda student: student.weight)
  for student in sortStudents:
    print (student.lastName + ", " + student.firstName + ", " + str(student.age) + ", " + str(student.height) + ", " + str(student.weight))

def printSumAge(students):
  print ("Answer:")
  x = 0
  for student in students:
    x = x + student.age
  print (x)

def printAvgAge(students):
  print ("Answer:")
  x = 0
  for student in students:
    x = x + student.age
  print (x/len(students))

def printSumHeight(students):
  print ("Answer:")
  x = 0
  for student in students:
    x = x + student.height
  print (x)

def printAvgHeight(students):
  print ("Answer:")
  x = 0
  for student in students:
    x = x + student.height
  print (x/len(students))

def printSumWeight(students):
  print ("Answer:")
  x = 0
  for student in students:
    x = x + student.weight
  print (x)

def printAvgWeight(students):
  print ("Answer:")
  x = 0
  for student in students:
    x = x + student.weight
  print (x/len(students))

def ageRange(studentA, studentB):
  return math.abs(studentA.age - studentB.age)


main()