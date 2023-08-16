import functions
import connector as con
import otp_sender

def registration():
    print("Enter your name: ")
    name=input()
    print("Enter your email")
    email=input()
    query="insert into registration_details (name,email) values" +"('"+name+"','"+email+"');"
    print("Registered Successfully")
    con.cursor.execute(query)
    con.dbc.commit()

def login():
    print("Enter the User ID to login:")
    user_id = input()
    fetch_query="select * from registration_details;"
    con.cursor.execute(fetch_query)
    count=0
    for i in con.cursor:
        if user_id ==i[2]:
            count = count+1
            print("Sending OTP")
            otp_sender.otp_sender(user_id)
    if count==0:
        print("User not registered")


inp=0
print("                                --------------------------------------")
print("                                            DASHBOARD")
print("                                --------------------------------------")
print("Enter 1 to login ")
print("Enter 2 to register")
print("ENTER 3 TO PRINT THE MAXIMUM RAINFALL")
print("ENTER 4 TO PRINT THE MINIMUM RAINFALL")
print("ENTER 5 TO PRINT AVERAGE RAINFALL")
print("ENTER 6 TO PRINT THE NAME OF SUBDIVISION WITH MAXIMUM RAINFALL")
print("ENTER 7 TO PRINT THE NAME OF SUBDIVISION WITH MINIMUM RAINFALL")
print("ENTER 8 TO PRINT MINIMUM RAINFALL OF A PARTICULAR MONTH")
print("ENTER 9 TO PRINT MAXIMUM RAINFALL OF A PARTICULAR MONTH")
print("ENTER 10 TO PLOT A GRAPH SHOWING ANNUAL MEAN RAINFALL OF EVERY SUBDIVISION")
print("ENTER 11 T0 PLOT A GRAPH SHOWING THE RAINFALL TREND")
print("ENTER 12 TO EXIT")

inp=int(input("enter your choice:"))
if inp==1:
    login()
elif inp==2:
    registration()
elif inp == 3:
    functions.max_rainfall()
elif inp==4:
    functions.min_rainfall()
elif inp==5:
     functions.avg_rainfall()
elif inp==6:
     functions.name_max()
elif inp==7:
    functions.name_min()
elif inp==8:
    functions.month_min()
elif inp==9:
     functions.month_max()
elif inp==10:
     functions.graph_1()
elif inp==11:
    functions.graph_2()




