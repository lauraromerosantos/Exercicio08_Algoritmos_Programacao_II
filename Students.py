class Student:
  def __init__(self, code, name, subscription):
    self.code = code
    self.name = name
    self.subscription = subscription

  def printStudent(self):
    print('Código: {} - Nome: {} - Matrícula: {}'.format(str(self.code), self.name, self.subscription))

############################

class HighSchool(Student):
  def __init__(self, code, name, subscription, year):
    Student.__init__(self, code, name, subscription)
    self.year = year

  def printHighSchool(self):
    print('Código: {} - Nome: {} - Matrícula: {} - Ano: {}'.format(str(self.code), self.name, self.subscription, str(self.year)))

############################

class Graduation(Student):
  def __init__(self, code, name, subscription, halfyear):
    Student.__init__(self, code, name, subscription)
    self.halfyear = halfyear
  
  def printGraduation(self):
        print('Código: {} - Nome: {} - Matrícula: {} - Semestre: {}'.format(str(self.code), self.name, self.subscription, str(self.halfyear)))