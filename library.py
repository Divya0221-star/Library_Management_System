import datetime as dt

def get_date():
    a = dt.datetime.today()
    s = str(a.day) + "/" + str(a.month) + "/" + str(a.year)
    return s

def issue_book():
    enr = input("Enter Enrollment Number : ")
    bnum = input("Enter Book Number : ")
    idate = get_date()
    rdate = "NA"

    fobj = open("all_issued.txt", "a")
    fobj. write(enr + "," +bnum + "," + idate + "," + rdate  + "\n")
    fobj.close()
    print("Book Issued...")
    input()

def return_book():
    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    rdate = get_date()
    bnum = input("Enter Book Number : ")
    ind = 0
    while ind<len(all_lines):
        ls = all_lines[ind].split(",")
        if ls[1]==bnum and ls[3]=="NA\n":
            ls[3] = rdate + "\n"
            new_line = ",".join(ls)
            all_lines[ind] = new_line
            break
        ind = ind + 1

    fobj = open("all_issued.txt", "w")
    fobj.writelines(all_lines)
    fobj.close()
    print("Book Returned..")
    input()

def view_not_ret_books():
    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[3] == "NA\n":
            print(ls[0], ls[1], ls[2], sep="\t")
    input()

def add_new_book():
    bnum = input("Enter Book Number : ")
    btitle = input("Enter Book Title : ")
    bauth = input("Enter Book Author : ")
    bpub = input("Enter Publication Name : ")

    fobj = open("all_books.txt", "a")
    fobj.write(bnum + "," + btitle + "," + bauth + "," + bpub + "\n")
    fobj.close()
    print("New Book Added...")
    input()

def add_new_student():
    enum = input("Enter Enrollment Number : ")
    sname = input("Enter Student Name : ")
    sclass = input("Enter Class : ")
    semail = input("Enter Email : ")

    fobj = open("all_students.txt", "a")
    fobj.write(enum + "," + sname + "," + sclass + "," + semail + "\n")
    fobj.close()
    print("New Student Added...")
    input()

def book_history():
    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    bnum = input("Enter Book Number : ")
    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[1] == bnum:
            print(ls[0], ls[2], ls[3], sep="\t", end="")
    input()

def student_history():
    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    senr = input("Enter Enrollment Number : ")
    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[0] == senr:
            print(ls[1], ls[2], ls[3], sep="\t", end="")
    input()

def search_book():
    book_found = False
    bnum = input("Enter Book Number to Search : ")
    fobj = open("all_books.txt", "r")
    all_lines = fobj.readlines()
    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[0] == bnum:
            print("Book Title :", ls[1] )
            print("Author :", ls[2])
            print("Publication :", ls[3])
            book_found = True
            break
    if book_found == False:
        print("Invalid Book Number")
    input()

def search_student():
    stud_found = False
    senr = input("Enter Enrollment Number : ")

    fobj = open("all_students.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[0] == senr:
            print("Student Name :", ls[1])
            print("Class :", ls[2])
            print("Email :", ls[3])
            stud_found = True
            break
    if stud_found == False:
        print("Invalid Enrollment Number")
    input()

while True:
    print("Select Operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - View Not Returned Books")
    print("4 - Add new Book")
    print("5 - Add new Student")
    print("6 - Book History")
    print("7 - Student History")
    print("8 - Search Book")
    print("9 - Search Student")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1: issue_book()
    elif ch==2: return_book()
    elif ch==3: view_not_ret_books()
    elif ch==4: add_new_book()
    elif ch==5: add_new_student()
    elif ch==6: book_history()
    elif ch==7: student_history()
    elif ch==8: search_book()
    elif ch==9: search_student()
    elif ch==0: exit(0)

