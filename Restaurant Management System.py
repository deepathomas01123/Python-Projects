#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. STUDENT NAME : DEEPA ROSE THOMAS
#   STUDENT ID   : S3952532
#2. THE HIGHEST PART ATTEMPTED IS PART -3 SECTION 5.
#3. PROBLEMS AND REQUIREMENTS HAVE NOT MET 
        #In the Order an Item section, the customer is asked "Do you want to continue[Y/N]?"
        # I have not handled the case when an invalid choice is entered besides Y/N


#DOCUMENTATION
    #In this section we are initialing the lists amd dictionaries that are needed during the program
    #We have declared a copy list to capture the copy of the original items in order to capture the sold-out dishes information
    
#Importing libraries
# Initilalising the Lists
import sys
new_customer_list = ["Tom","Kate"]
items_list = {"Hamburger": 12.5, "Coke": 3.0, "Pizza": 14.0}
copy_list = items_list.copy() #contains a copy of items_list
customer_order={} #to store the customer name and the order count
rewards_customer_list = ["Kate"]


#FUNCTION TO WAIT FOR A KEY PRESS 
#This function is used to ask the user for a key press after each option in the Menu item is completed.
#After a key is entered by the user, the program prints the Menu again

def pressEnter():
    input("Press any key to continue")
    print_menu()

# FUCNTION TO TAKE ORDER FROM THE USER

#In this function the Customer makes the order from the menu items
# We ask for customer name as the first input and a while loop is run until the user enters 'N' meaning he doesnt wnat to order
#any more items from the menu
#Every time a dish is entered a check is made with the original items_list to see if the list is present.
#A validation is also done for the dish quantity entered to check is its a valid integer 
# We also check if the dish entered is SOLD -OUT and a message is displayed to the user if he has entered a SOLD-OUT dish
# An option is made available to the user to cancel the order in case of SOLD-OUT dish and the user can exit the Restaurant
#from the main Menu.

#For capturing the number of orders made by the user, the customer_order dictionary is used so that the username and the no.of
#orders can be stored as key:value pairs.

#The order_list is also initialised as a dictionary capturing the dish_name and the dish_qty ordered by the user.

def order():    
    choice = 'y'
    cust_name = input(" Enter the name of the customer : ")
    order_list={}
    #Loop to keep asking for dishes until user presses y
    while choice =='y' or choice =='Y':
        check = 0
        flag = 0
        dish_name = input("Enter the dish:")
        dish_name = dish_name.strip()
        dish_name = dish_name.title()
        while check == 0: 
            if dish_name not in items_list:
                print(" You have not entered a valid dish, please reenter ")
                dish_name = input("Enter the dish:")
                dish_name = dish_name.strip()
                dish_name = dish_name.title()
                check = 0
            else:
                 check = 1
        dish_qty = input("Enter the dish quantity (1,2,3..): ")
        #checking for invalid dish quantity entry
        while flag == 0:
            if dish_qty.isdigit()==False or int(dish_qty)<=0:
                print("You have entered an invalid quantity, please reenter")
                dish_qty = input("Enter the dish quantity (1,2,3..): ")
                flag = 0
            else:
                flag = 1
#Adding the dishes that are ordered to the order_list
        if dish_name not in order_list:
            order_list[dish_name] = [dish_qty]
        elif isinstance(order_list[dish_name], list):
            order_list[dish_name].append(dish_qty)
        else:
            order_list[dish_name] = [order_list[dish_name], dish_qty]
        choice =input("Do you wish to continue (y/n)?")
#Checking for sold-out dish in the order     
    for dish_name in list(order_list):
        if items_list[dish_name]=='SOLD OUT':
            print(dish_name," is SOLD OUT and will be removed from your order")
            del order_list[dish_name]
            choice = input("Do you want to cancel the order [y/n]?")
            if choice.title()=='Y':
                  print_menu()                 
    
    
 #adding new customers to the customer_list
    if len(order_list) !=0:
        if cust_name not in new_customer_list:
            new_customer_list.append(cust_name)
            customer_order[cust_name]=1
        else:
            #taking the count of orders made by customers
            order_number = customer_order[cust_name]
            customer_order[cust_name]= int(order_number)+1
        
#calling the function to print the invoice  
    generate_invoice(cust_name, order_list)
    
    
#FUNCTION TO PRINT MOST FREQUENT CUSTOMER

#In this function we sort the customer_order dictionary items in the reverse order to get them sorted according to the most
#number of orders made.
#In case if there are more than one customer with same number of orders, the program prints only 1 customer.

def display_frequent_customer():
    #check if any orders have been made or not
    if len(customer_order)==0:
        print("No Customer has ordered till now")
    else:
        sort_orders = sorted(customer_order.items(),key = lambda x:x[1], reverse = True)
        print("MOST FREQUENT CUSTOMER \t NUMBER OF ORDERS MADE")
        print(sort_orders[0][0],"\t\t\t", sort_orders[0][1])
    pressEnter()
    
#FUNCTION TO PRINT CUSTOMER INFORMATION

#This function loops through the customer_list and prints whether the customers are in the Rewards program/not
def display_customer_info():
    print("Customer Name \t Rewards Program(Y/N)")
    for name in new_customer_list:
        if name in rewards_customer_list:
            print(name,"\t\t In the Rewards Program")
        else:
            print(name,"\t\t Not in Rewards Program")
    pressEnter()
    
#FUNCTION TO PRINT DISHES INFORMATION

#This function prints the Dish_name and the dish_price corresponding to an item
#If the item is SOLD-OUT, the SOLD-OUT information is also displayed.
def display_dish_info():
    print("Item  Price(AUD)")
    print("**" * 15)
    for dish,price in items_list.items():
        print(dish, " ",price)
    pressEnter()
    
#FUNCTION TO ADD/UPDATE DISH

#This funstion reads the Items:Price update/addition that needs to be made by the user
#The input string is split into a list and each item is checked if the prices entered for the dish are valid integer values.
# If an invalid price is entered the program skips the item and proceeds to the next item in the list
#An error message is displayed to the user in this instance.
def add_update():
    temp_list = input('Enter the dish and prices in the format dish1:price1, dish2:price2 :')
    item= (temp_list.split(","))
    for i in range(0, len(item)):
        dish, price = str(item[i]).split(":")
        dish= dish.strip()
        dish = dish.title()
        price = price.strip()
        if price.isdigit()== False or int(price)<=0:
            print("Price entered is not valid,", dish, " wont be added")
        else:
            items_list[dish]= price
    print("Menu has been updated successfully")
    copy_list = items_list.copy()
    #The display_dish_info() function is called so that the user can see the items added/updated to the system
    display_dish_info()
    pressEnter()
    
#FUNCTION TO PRINT THE INVOICE OF THE CUSTOMER

#This function takes the customer name and the orders list as inputs
#A check is made to see if the customer belongs to the Rewards Program and an option is provided to the customer to get added 
#to the program as well
# The service fee is calculated based on the Rewards Program and the Total price
#An invoice is generated to the customer as per their order

def generate_invoice(cust_name, order_list):    
    check = 1 
    cost = 0
    if cust_name in rewards_customer_list:
        service_fee = 0
    else:
        choice = input(" The customer is not in the Rewards Program. Do you want to join the Rewards Program[y/n]? :")        
        while check ==1:            
            if choice == 'y' or choice == "Y":
                rewards_customer_list.append(cust_name)
                service_fee = 0
                print("Customer successfully added to the Rewards program")
                check = 0
            elif choice =='n' or choice == 'N':
                service_fee = 0.1
                check = 0
            else:
                print("invalid choice, please reenter")
                choice = input(" Plese enter y/n")   
#Printing Invoice  
    
    print("*"* 20)
    print("RECEIPT OF ", cust_name)
    print("*"* 20)
    for dish_name, dish_qty in order_list.items(): 
        price = float(items_list[dish_name])
        for i in range (0, len(dish_qty)):
            print(dish_name, "\t", price, "(AUD)","\t *", dish_qty[i])
            cost += (price*int(dish_qty[i]))
    service_fee *= cost
    print("Service fee \t", service_fee, "(AUD)" )
    total_cost = cost+service_fee
    print("Total cost \t", total_cost, "(AUD)")
    pressEnter()
    
#FUNCTION TO ADD SOLD-OUT DISHES

#Here we ask the user to enter the sold-out dishes
# A check is made if they are valid and if not, an error message is printed to the user and the program proceeds to the next item 
#in the list
#The value of key - dish_name is updated as 'SOLD-OUT' in the items_list to denote them as Sold-out
def add_sold_out_dish():
    sold_out_list=[]
    choice = 1
    check = 0
    temp_list = input("Enter the dishes that are sold-out in the format dish1, dish2 :")
    item= (temp_list.split(","))
    for i in range(0, len(item)):
        dish_name = item[i].strip()
        dish_name = dish_name.title()
        if dish_name in items_list:
            sold_out_list.append(dish_name)
        else:
            print("You have entered an invalid dish", dish_name," wont be added to the sold-out option")
                       
    for dish, price in items_list.items():
        if dish in sold_out_list:
            items_list[dish]= "SOLD OUT"
        else:
            items_list[dish]= copy_list[dish]
    pressEnter()
    
#FUNCTION TO PRINT MENU

#This function prints the MENU as required.
#It accepts the choices from the user and if an invalid choice is made, the user is asked again until he enters a valid choice.
#When the user enters the choice 0, the program exits.
def print_menu():
    print(" Welcome to RMIT Restaurant ordering system!\n")
    print("**"* 30)
    print("You can choose from the following options")
    print("1. Order a Meal\n2. Add/update dishes and prices\n3. Display existing customers information\n4. Display existing dishes information\n5. Add sold out dishes\n6. Display most frequent customer\n0. Exit the program \n")
    print("**"* 30)
    choice = input(" Choose one option :")
    if choice == '1':
        order()
    elif choice == '2':
        add_update()
    elif choice == '3':
        display_customer_info()
    elif choice == '4':
        display_dish_info()
    elif choice == '5':
        add_sold_out_dish()
    elif choice == '6':
        display_frequent_customer()
    elif choice == '0':
        print("Thank you for ordering from RMIT Restaurant \nHave a nice day :)")
        sys.exit(0)
    else: 
        print("Invalid choice, please re enter")
        print_menu()

print_menu()

#PROBLEMS NOT MET BY THE CODE
#Handling invalid choice other than Y/N when the user is asked Do you want to continue? while ordering an item.
#Try - except is not implemented for KeyError or invalid choice error
# Storing user order history is not answered in the code.

#ANALYSIS
#Over all the program was challenging requiring to use all the concepts covered in the Lecture and Practical sessions
#This week had all the assignment submissions and hence it was a bit difficult to do everything together
#I found Part 3 to be challenging especially the sold-out dishes part and the customer order history part.


