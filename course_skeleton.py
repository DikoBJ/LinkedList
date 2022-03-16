import sys
ADD = 'A'
DELETE = 'D'
FIND = 'F'

class Student:
  def __init__(self, id, name, p=None):
    self.id=id
    self.name=name
    self.p=p
    self.next=None
    

class Course:
  def __init__(self, listStudent=[]):
    self.head = None
    self.listSutent=listStudent


  def __len__(self):
    return self.size


  def isEmpty(self):
    return self.size == 0


  def addStudent(self, newID, newName):
    if self.head == None:
      self.head=Student(newID, newName)
    else:
      newStudent=Student(newID, newName)
      newStudent.next= self.head
      self.head=newStudent


  def deleteStudent(self, queryID):
        temp = self.head
 
        if temp != None:
            if temp.id == queryID:
                self.head = temp.next
                temp = None
                return

        while temp != None:
            if temp.id == queryID:
                break
            prev = temp
            temp = temp.next
 
        # if queryID was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None
    


  def find(self, queryID):
    current = self.head
    while current != None:
      if current.id == queryID:
        return current.id 
      current = current.next
    return None  



  def write(self):
    while self.head:
      print (self.head)
      self.head = self.head.next


if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  course = Course()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == ADD:
        if len(words) != 3:
          raise Exception("ADD: invalid input")
        i, n = int(words[1]), words[2]
        if course.addStudent(i, n):
          course.write(outFile)
        else:
          outFile.write("Addition failed\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        if course.deleteStudent(i):
          course.write(outFile)
        else:
          outFile.write("Deletion failed\n")
      elif op == FIND:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        found = course.find(i)
        if not found:
          outFile.write("Search failed\n")
        else:
          outFile.write(str(found.id) + " " + found.name + "\n")
      else:
        raise Exception("Undefined operator")
