'''
Program Name: Mobile Install Log Parser
Script Name: main.py
Version: 0.1
Python Version: 3.6
github: midwestcoder2020
Author: Darian Lopez
website www.midwestcoder.com
email: midwestcder2019@gmail.com
Date: 8 Dec 20

purpose:
    allows user to select the log file for exact parsing. the user can specify between one application or all applications for:
        -install records
        -uninstall records
'''
from datetime import datetime
running = True
import os


# nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
# sys.stdout = nonbuffered_stdout

# write to log file
def writeEntry(out,data):
    with open(out, "a+") as f1:
        f1.write(str(data) +"\n")
    f1.close()

#Find all Installation records for an app DONE
def parseInstallOneApp(f,appName,out):
    count =0
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Started \n"))
    with open(f, 'r') as f:
        data = f.readlines()
        for l in data:
            print("checking {}".format(l))
            if appName in l:
                if "Install" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out,l)
        print("{} records found\n ".format(count))
        writeEntry(out,"{} records found\n ".format(count))
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Finished"))

#find all installation records DONE
def parseLogFileAllApps(f,out):
    count = 0
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Started \n"))
    with open(f, 'r') as f:
        data = f.readlines()
        for l in data:
            print("checking {}".format(l))
            if "Install" in l:
                print(l[0:l.find("[")])
                print(l[l.find("[")::])
                count = count + 1
                writeEntry(out, l)
        print("{} records found\n ".format(count))
        writeEntry(out, "{} records found\n ".format(count))
    writeEntry(out, "{} {}".format(str(datetime.now())," Parsing Finished"))

#Find Deletion/Uninstall Records for an app DONE
def parseLogFileAllOneApp(f,appName,out):
    count =0
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Started \n"))
    with open(f, 'r') as f:
        data = f.readlines()
        for l in data:
            # print("checking {}".format(str(l)))
            if appName in l:
                if "Uninstall Identifier" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out, l)

                if "Destroying" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out,l)


                if "Install" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out,l)

        print("{} records found\n ".format(count))
        writeEntry(out,"{} records found\n ".format(count))
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Finished"))

#Find all records for an app DONE
def parseAllDelOneApp(f,appName,out):
    count = 0
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Started \n"))
    with open(f, 'r') as f:
        data = f.readlines()
        for l in data:
            # print("checking {}".format(l))
            if appName in l:
                if "Uninstall Identifier" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out, l)

                if "Destroying" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out,l)

        print("{} records found\n ".format(count))
        writeEntry(out,"{} records found\n ".format(count))
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Finished"))

#find all Deletion/Uninstall Records DONE
def parseAllDelete(f,out):
    count = 0
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Started \n"))
    with open(f, 'r') as f:
        data = f.readlines()
        for l in data:
            print("checking {}".format(l))
            if "Uninstall Identifier" in l:
                print(l[0:l.find("[")])
                print(l[l.find("[")::])
                count = count + 1
                writeEntry(out, l)

            if "Destroying" in l:
                print(l[0:l.find("[")])
                print(l[l.find("[")::])
                count = count + 1
                writeEntry(out,l)

        print("{} records found\n ".format(count))
        writeEntry(out,"{} records found\n ".format(count))
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Finished"))



#install and delete for all apps
def parseUnAndInAllApps(f,out):
    count = 0
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Started \n"))
    with open(f, 'r') as f:
        data = f.readlines()
        for l in data:
                print("checking {}".format(l))
                if "Uninstall Identifier" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out, l)

                if "Destroying" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out, l)

                if "Install" in l:
                    print(l[0:l.find("[")])
                    print(l[l.find("[")::])
                    count = count + 1
                    writeEntry(out,l)
        print("{} records found\n ".format(count))
        writeEntry(out,"{} records found\n ".format(count))
    writeEntry(out, "{} {}".format(str(datetime.now()), " Parsing Finished"))

def main():
		print("***4n6***"*10)
		print("\nPrecise iOS mobile installation log parsing and reported\n")
		print("How it works: \n")
		print("1 - Enter the path of the ios mobile installation logfile to parse\n")
		print("2 - Select the type of parsing method you need\n")
		print("3 - The program will generate a text file report with th results\n")
		print("***4n6***" * 10)

		file = input("\nEnter the path of the log file to parse \n")

		print("**1337**"*10)
		print("\n Select the parsing mode below: \n")
		parseMethod = input("1 - Find all Installation references for one Application\n\n2 - Find all Deletion|Uninstallation references for one Application\n\n"
							"3 - Find Both Install and Uninstall refences for one Application\n\n4 - Find all Installation references for all applications\n\n"
							"5 - Find Deletion|Uninstallation Dele references for all applications\n\n6 - Find Both Install and Uninstall refernces for all applications\n\n").lstrip().strip()

		out = os.getcwd()+"/out.txt"

		if int(parseMethod) <=3:
			app = input("enter the main part of the applicatino bundle (ie dropbox,  tiktok = musically)")

		if parseMethod == '1':
			try:
				parseInstallOneApp(file,app,out)
			except Exception as e:
				print(str(e) + "An Error Occured. Check your data sources")

		elif parseMethod =='2':
			try:
				parseAllDelOneApp(file,app,out)
			except Exception as e:
				print(str(e) + "An Error Occured. Check your data sources")

		elif parseMethod == '3':
			try:
				parseLogFileAllOneApp(file,app,out)
			except Exception as e:
				print(str(e)+"An Error Occured. Check your data sources")

		elif parseMethod =='4':
			try:
				parseLogFileAllApps(file,out)
			except Exception as e:
				print(str(e) + "An Error Occured. Check your data sources")

		elif parseMethod =='5':
			try:
				parseAllDelete(file,out)
			except Exception as e:
				print(str(e) + "An Error Occured. Check your data sources")

		elif parseMethod == '6':
			try:
				parseUnAndInAllApps(file,out)
			except Exception as e:
				print(str(e) + "An Error Occured. Check your data sources")
				
		print("Output saved to {}".format(out))


if __name__ == '__main__':
    main()