#ProcessData.py
#Name:Cameron Sailors
#Date:4/6/2025
#Assignment:Lab 8

import random

def makeID(first, last, num):
  while len(last) < 5:
    last = last + "x"
  last = last[0:5]

  last3 = num[-3:]

  id = first[0] + last + last3
  return id

def makeMajorYear(major, year):
  major3 = major[0:3]
  year = year.upper()
  yearAbbr = ""
  if year == "FRESHMAN":
    yearAbbr = "FR"
  elif year == "SOPHOMORE":
    yearAbbr = "SO"
  elif year == "JUNIOR":
    yearAbbr = "JR"
  elif year == "SENIOR":
    yearAbbr = "SR"
  else:
    yearAbbr = "GRAD"
  
  majorYear = major3 + yearAbbr
  return majorYear

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  for student in inFile:
    studentData = student.split()
    firstName = studentData[0]
    lastName = studentData[1]
    studentID = studentData[3]
    year = studentData[5]
    major = studentData[6]
    userID = makeID(firstName, lastName, studentID)
    majorYear = makeMajorYear(major, year)

    studentOutput = lastName + "," + firstName + "," + userID + "," + majorYear + "\n"
    outFile.write(studentOutput)


  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
