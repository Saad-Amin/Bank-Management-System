import pymysql as connector
import numpy as np
import random

con = connector.connect(host="localhost", user="root", password="", db="pythontest")
cur = con.cursor()

# Queue Concept
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Stack Concept
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# Linear Search Concept
def linearsearch(arr, n, x):
    for i in range(0, n):
        if (arr[i][4] == x):
            return i
    return -1

# Binary Search Concept
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid][4] == x:
            return mid

        elif arr[mid][4] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

#Bubble Sort
def bubbleSort(data):
    n = len(data)
    for i in range(n-1):
        if data[i][4] > data[i + 1][4]:
            data[i][4], data[i + 1][4] = data[i + 1][4], data[i][4]

# Insertion Sort
def insertionSort(data):
    for i in range(1, len(data)):
        key = data[i][4]
        j = i - 1
        while j >= 0 and key < data[j][4]:
            data[j + 1][4] = data[j][4]
            j -= 1
        data[j + 1][4] = key

# Selection Sort
def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i][0] < array[min_idx][0]:
                min_idx = i

        (array[step][0], array[min_idx][0]) = (array[min_idx][0], array[step][0])

# Main Database Operations
def dboperations(que):
    con.ping()
    cur.execute(que)
    if(cur.rowcount>0):
        con.commit()
        con.close()
        return cur.rowcount
    else:
        con.commit()
        con.close()
        return cur.rowcount

# Random Account Number Generator
def acc_generator():
    acc_no = "DS"
    for num in range(0, 4):
        ran = random.randint(0, 9)
        acc_no += str(ran)
    return acc_no

# Bill Info
def billinfo(no,type):
    con.ping()
    query = "select * from bills where billno = '{}' and billtype = '{}'".format(no,type)
    cur.execute(query)
    if (cur.rowcount > 0):
        info = cur.fetchall()
        for x in info:
            print("\nBill No: ", x[0])
            print("Bill Type: ", x[1])
            print("Amount: ", x[2])
            print("Status: ", x[3])
            print("Family No: ", x[4])

        print("\n1.Pay Bill")
        print("2.Back")
        choice2 = int(input("Enter Your Choice: "))
        if (choice2 == 1):
            query1 = "update bills set status = 'Paid' where billno = '{}'".format(no)
            cur.execute(query1)
            if (cur.rowcount > 0):
                print("Bill Payed Sucessfully\n")
            else:
                print("Bill Not Paid\n")
        con.commit()

# After Manager login
def managerlogin():
    while(True):
        con.ping()
        print("\n1.Employee Functions")
        print("2.Users Functions")
        print("3.Employee Details")
        print("4.Back")
        choice = int(input("\nEnter Your Choice "))

        if (choice == 1):
            con.ping()
            employeelogin()

        elif(choice == 2):
            con.ping()
            userlogin()

        elif(choice == 3):
            data = np.array([["", "", "", "", ""]])
            con.ping()
            query = "select * from employee"
            q = Queue()
            cur.execute(query)
            result = cur.fetchall()
            if (cur.rowcount > 0):
                for rows in result:
                    q.enqueue(rows)
                while (True):
                    if (q.isEmpty() == False):
                        data = np.append(data, [q.dequeue()], axis=0)
                    else:
                        break
            else:
                print("Operation Unsucessfull")
            con.commit()

            data = np.delete(data, 0, axis=0)

            print("Sorting on the basis of Employee Id")
            insertionSort(data)

            for i in range(len(data)):
                for j in range(1):
                    print("\nEmployee Id: ", data[i][j+4])
                    print("Name: ", data[i][j])
                    print("Username: ", data[i][j + 1])
                    print("Email: ", data[i][j + 2])
                    print("Pass: ", data[i][j + 3])

            while True:
                print("\n1.Search Employee")
                print("2.Back")
                choice = int(input("Enter Your Choice: "))
                if(choice == 1):
                    search = input("Enter Employee Id to search: ")
                    result = binarySearch(data,0,len(data)-1,search)

                    if(result == -1):
                        print("\nEmployee Not Found")
                    else:
                        print("\nEmployee Found at index no",result)

                elif(choice == 2):
                    break

        elif(choice == 4):
            break

# After employee login
def employeelogin():
    while(True):
        con.ping()
        print("\n1.Approve Loan Requests")
        print("2.Users Info")
        print("3.Last 5 login")
        print("4.Billing")
        print("5.Back")
        choice = int(input("\nEnter Your Choice "))

        # Loan Request Approval or Disapproval
        if (choice == 1):
            data = np.array([["","",""]])
            con.ping()
            query = "select * from loan"
            cur.execute(query)
            result = cur.fetchall()
            if (cur.rowcount > 0):
                for rows in result:
                    data = np.append(data,[rows],axis = 0)

            data = np.delete(data, 0, axis=0)
            print("Sorting on the basis of Account Number")
            selectionSort(data,len(data))

            for i in range(len(data)):
                for j in range(1):
                    print("\nAcc No: ",data[i][j])
                    print("Loan Amount: ",data[i][j+1])
                    print("Status: ",data[i][j+2])

            # Checking Account Number is in database or not
            acc = input("\nEnter Account Number u want to select ")
            query1 = "select accno from loan where accno = '{}'".format(acc)
            con.ping()
            if(dboperations(query1)>0):
                print("\n1.Approve Loan")
                print("2.Reject Loan")
                status = int(input("\nEnter Your Choice "))

                if (status == 1):
                    query = "update loan set status = 'Approved' where accno = '{}'".format(acc)
                    con.ping()
                    cur.execute(query)
                    if (cur.rowcount > 0):
                        print("Loan Approved")
                    else:
                        print("Invalid Data")

                elif (status == 2):
                    query = "update loan set status = 'Rejected' where accno = '{}'".format(acc)
                    con.ping()
                    cur.execute(query)
                    if (cur.rowcount > 0):
                        print("Loan Rejected")
                    else:
                        print("Invalid Data")
                else:
                    print("Invalid Account Number")
            else:
                print("Operation Unsucessfull")
            con.commit()

        # User Details
        elif (choice == 2):
            data = np.array([["","","","",""]])
            con.ping()
            query = "select * from useraccount"
            q = Queue()
            cur.execute(query)
            result = cur.fetchall()
            if (cur.rowcount > 0):
                for rows in result:
                    q.enqueue(rows)
                while (True):
                    if (q.isEmpty() == False):
                        data = np.append(data,[q.dequeue()],axis = 0)
                    else:
                        break
            else:
                print("Operation Unsucessfull")
            con.commit()

            data = np.delete(data,0,axis = 0)
            print("Sorting on the basis of Account Number")
            bubbleSort(data)

            for i in range(len(data)):
                for j in range(1):
                    print("\nAccno: ", data[i][j + 4])
                    print("Name: ",data[i][j])
                    print("Email: ",data[i][j+1])
                    print("Pass: ",data[i][j+2])
                    print("Gender: ",data[i][j+3])

            while True:
                print("\n1.Search user")
                print("2.Back")
                choice = int(input("Enter Your Choice: "))
                if(choice == 1):
                    search = input("Enter Account Number u want to search: ")
                    result = linearsearch(data,len(data),search)
                    if(result == -1):
                        print("\nAccount Number Not Found")
                    else:
                        print("\nAccount Number Found at index no",result)
                elif(choice == 2):
                    break

        # Last 5 login
        elif (choice == 3):
            con.ping()
            s = Stack()
            email = []
            query = "select accno from last_login"
            cur.execute(query)
            result = cur.fetchall()
            if (cur.rowcount > 0):
                for rows in result:
                    s.push(rows[0])
                for i in range(0,5):
                    if (s.size() > 0 and s.isEmpty() == False):
                        query1 = "select email from useraccount where accno = '{}'".format(s.pop())
                        cur.execute(query1)
                        result1 = cur.fetchone()
                        if (cur.rowcount > 0):
                            email.append(result1[0])
                    else:
                        break
                for i in email:
                    print(i)
            else:
                print("Operation Unsucessfull")
            con.commit()

        # Billing
        elif (choice == 4):
            con.ping()
            while(True):
                print("1.Electricity Bill Payment")
                print("2.Gas Bill Payment")
                print("3.Back")
                choice1 = int(input("Enter Your Choice: "))
                bill_no = input("Enter Bill No: ")
                if(choice1 == 1):
                    billinfo(bill_no,"Electricity")

                elif(choice1 == 2):
                    billinfo(bill_no, "Gas")

                elif (choice1 == 3):
                    break

        # Back
        elif(choice == 5):
            con.ping()
            break
    con.close()

# After User Login
def userlogin(accno):
    while(True):
        con.ping()
        print("\n1.Loan Request")
        print("2.Balance Inquiry")
        print("3.Deposit Amount")
        print("4.Withdraw Amount")
        print("5.Money Transfer")
        print("6.Close Account")
        print("7.Back")
        choice = int(input("\nEnter Your Choice "))

        # Loan Request
        if(choice == 1):
            loanamount = int(input("Enter Loan Amount u want to request "))
            query = "insert into loan(accno,loanamount,status) values('{}','{}','Pending')".format(accno,loanamount)
            con.ping()
            if (dboperations(query) > 0):
                con.ping()
                print("Loan Request Successfully Submitted")
            con.commit()

        # Balance Inquiry
        elif (choice == 2):
            query = "select name from useraccount where accno = '{}'".format(accno)
            con.ping()
            cur.execute(query)
            result = cur.fetchone()
            for x in result:
                result = x
            query1 = "select balance from balanceinfo where accno = '{}'".format(accno)
            con.ping()
            cur.execute((query1))
            if(cur.rowcount>0):
                con.ping()
                bal = cur.fetchone()
                for x in bal:
                    bal = x
                    print("Mr/Miss",result,"your account balance is",bal,"Rs")
            con.commit()

        # Deposit Amount
        elif(choice == 3):
            query = "select balance from balanceinfo where accno = '{}'".format(accno)
            con.ping()
            cur.execute(query)
            con.ping()
            result = cur.fetchone()
            for x in result:
                result = x
            depamount = int(input("Enter Amount u want to Deposit "))
            bal = result + depamount
            query1 = "update balanceinfo set balance = '{}' where accno = '{}'".format(bal,accno)
            con.ping()
            if(dboperations(query1)>0):
                print("Sucessfully Deposit",depamount,"Rs in Account Number",accno)
            else:
                print("Invalid Amount")
            con.ping()
            con.commit()

        # Withdraw Amount
        elif (choice == 4):
            con.ping()
            query = "select balance from balanceinfo where accno = '{}'".format(accno)
            cur.execute(query)
            result = cur.fetchone()
            for x in result:
                result = x
            withamount = int(input("Enter Amount u want to Withdraw "))
            if(result>withamount or result == withamount ):
                remain = result - withamount
                query1 = "Update balanceinfo set balance = '{}' where accno = '{}'".format(remain, accno)
                if (dboperations(query1) > 0):
                    print("Sucessfully Withdraw", withamount, "Rs from Account Number", accno)
                else:
                    print("Invalid Amount")
            else:
                print("You Dont Have Enough Balance to Withdraw")
            con.ping()
            con.commit()

        # Transfer Money
        elif (choice == 5):
            bal = int(input("Enter Balance u want to Transfer "))
            query = "select balance from balanceinfo where accno = '{}'".format(accno)
            con.ping()
            cur.execute(query)
            result = cur.fetchone()
            for x in result:
                result = x
            if(result>bal):
                transferacc = input("Enter Account Number in which u want to Transfer Amount ")
                query1 = "select accno from useraccount where accno = '{}'".format(transferacc)
                con.ping()
                cur.execute(query1)
                if(cur.rowcount>0):
                    result1 = cur.fetchone()
                    for y in result1:
                        result1 = y
                    query2 = "select balance from balanceinfo where accno = '{}'".format(result1)
                    con.ping()
                    cur.execute(query2)
                    if (cur.rowcount > 0):
                        result2 = cur.fetchone()
                        for z in result2:
                            result2 = z
                        result2 = result2 + bal
                        query3 = "update balanceinfo set balance = '{}' where accno = '{}'".format(result2,result1)
                        con.ping()
                        cur.execute(query3)
                        if(cur.rowcount>0):
                            print("Sucessfully Tranfer")
                    else:
                        print("Error in Transfer")
                else:
                    print("Account Number Not Found")

                remain = result - bal
                query4 = "update balanceinfo set balance = '{}' where accno = '{}'".format(remain, accno)
                con.ping()
                cur.execute(query4)
                if(cur.rowcount>0):
                    print(bal,"Rs sucessfully deducted from Account No:",accno)
            else:
                print("You Don't Have Enough Balance to Transfer")
            con.ping()
            con.commit()

        # Close Account
        elif(choice == 6):
            con.ping()
            print("Are u sure u want to Close your Account")
            print("1.Yes")
            print("2.Cancel")
            confirm = int(input())

            if(confirm == 1):
                password = input("\nEnter Password of Account Number ")
                query = "select pass from useraccount where pass = '{}'".format(password)
                con.ping()
                cur.execute(query)
                if (cur.rowcount > 0):
                    query1 = "select balance from balanceinfo where accno = '{}'".format(accno)
                    con.ping()
                    cur.execute(query1)
                    if(cur.rowcount>0):
                        bal = cur.fetchone()
                        for x in bal:
                            bal = x
                        if(bal>0):
                            print("Please withdraw all money from your account in order to close it ")
                        else:
                            count = 0
                            query2 = "delete from useraccount where accno = '{}'".format(accno)
                            con.ping()
                            cur.execute(query2)
                            if (cur.rowcount > 0):
                                count += 1
                            query3 = "delete from balanceinfo where accno = '{}'".format(accno)
                            con.ping()
                            cur.execute(query3)
                            if (cur.rowcount > 0):
                                count += 1
                            query4 = "delete from loan where accno = '{}'".format(accno)
                            con.ping()
                            cur.execute(query4)
                            if (cur.rowcount > 0):
                                count += 1
                            con.ping()
                            con.commit()
                            if (count == 3):
                                print("Successfully Close Account Number", accno,"\n")
                                break
                    else:
                        print("Invalid Password")

        # Back
        elif(choice == 7):
            con.ping()
            break
        con.ping()
    con.close()

while(True):
    con.ping()
    print("1.Manager Login")
    print("2.Employee Login")
    print("3.Create User Account")
    print("4.User Login")
    print("5.FAQ")
    print("6.Close Application")

    choice = int(input("\nEnter Your Choice "))
    if (choice == 1):
        con.ping()
        email = str.strip(input("Enter Manager Email "))
        password = str.strip(input("Enter Password "))
        query = "select email, pass from manager where email = '{}' and pass = '{}'".format(email, password)
        if (dboperations(query) > 0):
            managerlogin()
        else:
            print("Invalid Email or Password")

    elif(choice == 2):
        con.ping()
        email = str.strip(input("Enter Employee Email "))
        password = str.strip(input("Enter Password "))
        query = "select email, pass from employee where email = '{}' and pass = '{}'".format(email,password)
        if(dboperations(query)>0):
            employeelogin()
        else:
            print("Invalid Email or Password")

    elif(choice == 3):
        con.ping()
        count = 0
        name = input("Enter Name ")
        email = str.strip(input("Enter User Email "))
        password = str.strip(input("Enter Password "))
        gender = str.strip(input("Enter Gender "))
        bal = int(str.strip(input("Enter Balance u want to deposit in your account ")))
        accno = acc_generator()
        print("Your Account Number is",accno)
        con.ping()
        query = "insert into useraccount(name,email,pass,gender,accno) values('{}','{}','{}','{}','{}')".format(name,email,password,gender,accno)
        if(dboperations(query)>0):
            count += 1
        query1 = "insert into balanceinfo(accno,balance,accholdername) values('{}','{}','{}')".format(accno,bal,name)
        if(dboperations(query1)>0):
            count += 1
        if(count == 2):
            print("\nAccount Successfully Created\n")

    elif (choice == 4):
        con.ping()
        acc = str.strip(input("Enter Your Account Number "))
        password = str.strip(input("Enter Password "))
        query = "select accno, pass from useraccount where accno = '{}' and pass = '{}'".format(acc, password)
        if(dboperations(query)>0):
            query1 = "insert into last_login(accno) values('{}')".format(acc)
            con.ping()
            dboperations(query1)
            con.ping()
            userlogin(acc)

    elif(choice == 5):
        # Dictionary Concept
        faq = [
            {
                "Question": "Is it necessary to create account in bank for bill payment?",
                "Answer": "No u can pay bill with your billno without creating any account"
            },
            {
                "Question": "Am I need to deposit some amount in my account when i create account?",
                "Answer": "Yes u need to depsoit some amount at the time of account creation"
            },
            {
                "Question": "What is the minimum age to create account in bank?",
                "Answer": "Your age is need to be 18 years or above to create account in bank"
            }
        ]
        while True:
            print("0 . Back")
            for i in range(len(faq)):
                print(i+1,".",faq[i]["Question"])
            question = int(input("\nSelect Your desired Question: "))
            print(faq[question-1]["Answer"])
            if(question == 0):
                break

    elif(choice == 6):
        con.ping()
        break

    else:
        print("Invalid Choice")
        break