def getGradePoint(GPA):
  if (GPA == "A" ):
    return 4.0
  elif (GPA == "B"):
    return 3.67
  elif (GPA == "B+"):
    return 3.33
  elif (GPA == "B"):
    return 3.0
  elif (GPA == "B-"):
    return 2.67
  elif (GPA == "C+"):
    return 2.33
  elif (GPA == "C"):
    return 2.0
  elif (GPA == "D"):
    return 1.0
  else: 
    return 0.0

def run():
  GPA = input("Enter your course 1 letter grade: ")
  CourseOne = getGradePoint(GPA)
  OneCredit = float(input("Enter your course 1 credit: "))
  print(f"Grade point for course 1 is: {(getGradePoint(GPA))}")

  GPA = input("Enter your course 2 letter grade: ")
  CourseTwo = getGradePoint(GPA)
  TwoCredit = float(input("Enter your course 2 credit: "))
  print(f"Grade point for course 2 is: {(getGradePoint(GPA))}")

  GPA = input("Enter your course 3 letter grade: ")
  ThreeCredit = float(input("Enter your course 3 credit: "))
  CourseThree = getGradePoint(GPA)
  print(f"Grade point for course 3 is: {(getGradePoint(GPA))}")

  GPATotal = ((CourseOne * OneCredit) + (CourseTwo *TwoCredit) + (CourseThree *ThreeCredit) ) / (OneCredit + TwoCredit + ThreeCredit)

  print(f"Your GPA is: {GPATotal}")

if __name__ == "__main__":
  run()