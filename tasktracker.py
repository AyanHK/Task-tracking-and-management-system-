import sqlite3
import os
os.system('attrib +h taskmanager.db')
def main():
    user= sqlite3.connect("taskmanager.db") 
    cur= user.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS user_info(task TEXT PRIMARY KEY,remark TEXT ,date TEXT )") 

    print("\n\nTo enter a new task press n:\nto view an old one press w:\n") 
    command= input("Enter command : ")
    if command =="n": 
        value=input("\nEnter the task : ")
        remark=input("Enter remark if any : ")
        date=input("Enter the date : ")   
        print("\ntask successfully saved")
        cur.execute("INSERT OR REPLACE INTO user_info  (task,remark,date) VALUES (?,?,?)" ,(value,remark,date),) 


        user.commit()
    elif command=="w":
        cur.execute(" SELECT * FROM user_info")
        output= cur.fetchall() 
        if output:
            for value,remark,date in output:
                print(f"\nSaved Tasks : {value}\nRemarks : {remark}\nDate : {date}")
                command2=input("\nTo delete a task press y ")
                if command2=="y":
                    taskd1 = input("\nenter the task name as saved to be deleted or press n to continue ")
                    cur.execute(" DELETE FROM user_info WHERE task=?",(taskd1,))
                    user.commit()
                    print("\nTask Successfully deleted : \n")
                elif command2=="n":
                    print("\nno tasks deleted : \n")
                else :  
                    print("Invalid Option")
        else:
            print("\nno tasks saved : \n")
    else:   
        print("\nInvalid Option")
    user.close() 
    
while True :
    main() 