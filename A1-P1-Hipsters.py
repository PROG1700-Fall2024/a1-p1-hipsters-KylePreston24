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
    kilometer = float(0)
    deliveryCharge = int(15)
    recordCost = float(0)


    #Input

    #Customer name input

    customerName = input("Enter the customer's name: ")

    #Kilometer distance input for order

    kilometer = input("Enter the distance in kilometers for delivery: ")

    #record cost input for order

    recordCost = input("Enter the cost of records purchased: ")

    #OutPut

    # Delivery Cost equation

    totalDeliveryCost = deliveryCharge * float(kilometer)



    #Record Cost equation

    totalRecordCost = float(recordCost) * 1.14  #1.14 for 14% taxes


    #Total cost equation

    totalCost = totalDeliveryCost + totalRecordCost


    #print customers names
    print("Puchase summary for {0}".format(customerName))

    #Print for total delivery cost
    print("Delivery Cost: ${0:.2f}".format(totalDeliveryCost))
    
    #Print for record cost including taxes
    print("Purchase Cost: ${0:.2f}".format(totalRecordCost))

    #Print total cost 
    print("Total cost   : ${0:.2f}".format(totalCost))






    # YOUR CODE ENDS HERE

main()