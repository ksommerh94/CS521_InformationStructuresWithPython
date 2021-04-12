import unittest
from myFileSystem import MyFolder
from myFileSystem import MyFile
from myFileSystem import FSComponent


class TestFileSystem(unittest.TestCase):

   def testChangeOwner(self):
       file1 = MyFile("file1", 1000)
       file2 = MyFile("file2", 20000)
       file3 = MyFile("file2", 300)
       root_folder = MyFolder("root")
       folder1 = MyFolder("folder1")

       root_folder.add(file3)
       root_folder.add(folder1)
       folder1.add(file1)
       folder1.add(file2)

       final_size,count_amount_files=root_folder.countfiles()
       assert final_size == 21300 and count_amount_files == 3
       print("The total number of files in the root folder will be " +str(count_amount_files) + ", and the total size will be "+str(final_size)+"B.")

       final_size,count_amount_files=folder1.countfiles()
       assert final_size == 21000 and count_amount_files == 2
       print("The total number of files in the folder1 folder will be " +str(count_amount_files) + ", and the total size will be "+str(final_size)+"B.")



if __name__ == '__main__':
   unittest.main()
