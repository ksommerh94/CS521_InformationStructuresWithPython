import unittest
from c_hotel import Hotel


class TestProject(unittest.TestCase):

   def test_myProject(self):
       hotel1 = Hotel('Test1',4.3,3.3,4.4,5,True,240)
       print(hotel1)

       average_rank=hotel1.avg_ranks()
       self.assertEqual(average_rank, 4.25)
       print("The average ranking score is " +str(average_rank))

       price_with_discount,flag=hotel1._Hotel__price_discount('TRAVEL50')
       assert price_with_discount == 120 and flag == True
       print("The price with discount is " +str(price_with_discount))

       price_with_discount,flag=hotel1._Hotel__price_discount('TRAVEL20')
       assert flag == False
       print("There is no discount code")




if __name__ == '__main__':
   unittest.main()
