#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.
"""
Student Name:    Kyle Preston
Program Title:  Hipster's Local Vinyl Records
Description:   Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers
"""
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)


  #Variables


    customerName= ""
    kilometer = int(0)
    deliveryCharge = int(15)
    recordCost = int(0)


    #Input
    
    #Customer name input

    customerName = input("Please enter Customer's name: ")

    #Kilometer distance input for order

    kilometer = input("Please enter in distance using kilometers: ")

    #record cost input for order

    recordCost = input("Enter in cost of records: ")

    #OutPut

    # Delivery Cost equation

    totalDeliveryCost = deliveryCharge * int(kilometer)



    #Record Cost equation

    totalRecordCost = int(recordCost) * 1.14  #1.14 for 14% taxes


    #Total cost equation

    totalCost = totalDeliveryCost + totalRecordCost


    #print customers names
    print("Customers name: {0}".format(customerName))

    #Print for total delivery cost
    print("Total delivery cost: ${0:.2f}".format(totalDeliveryCost))
    
    #Print for record cost including taxes
    print("Total cost for records: ${0:.2f}".format(totalRecordCost))

    #Print total cost 
    print("Total cost: ${0:.2f}".format(totalCost))






    # YOUR CODE ENDS HERE

main()