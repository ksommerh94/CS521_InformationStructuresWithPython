class FSComponent:

   def __init__(self, name):
       pass

   def changeOwner(self):
       pass

class MyFile(FSComponent):
   def __init__(self, name, size):
       self._name = name
       self._size = size

   def countfiles(self):
       return (self._size,1)

class MyFolder(FSComponent):
   def __init__(self, name):
       self._name = name
       self._children = []

   def add(self, ch):
       self._children.append(ch)

   def countfiles(self):
       #Go through all children
       final_size=0
       count_amount_files=0
       for f in self._children:
           temp_size,temp_amount=f.countfiles()
           final_size+=temp_size
           count_amount_files+=temp_amount
       return final_size,count_amount_files
