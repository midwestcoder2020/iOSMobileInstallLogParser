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
from gooey import Gooey, GooeyParser
running = True
import os
import sys

# nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
# sys.stdout = nonbuffered_stdout

# write to log file
def writeEntry(out,data):
    with open(out+"\\"+"output.txt", "a+") as f1:
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

@Gooey(program_name="IOS Mobile Install Log Parser")
def main():
    settings_msg = 'IOS Mobile Install Log Parser'
    parser = GooeyParser(description=settings_msg)
    parser.add_argument('--verbose', help='be verbose', dest='verbose',
                        action='store_true', default=False)
    subs = parser.add_subparsers(help='commands', dest='command')

    # ########################################################
    # Find all Installation records for an app DONE
    allRecOneApp = subs.add_parser('Install_Entries_One_App', help='Find all Installation records for an app')
    allRecOneApp.add_argument('Log_File',
                             help='Find all Installation records for an app',
                             type=str, widget='FileChooser')

    allRecOneApp.add_argument('App_Name',
                             help='Enter the application name you are looking for (ie :kik)')

    allRecOneApp.add_argument('Output_Dir',
                             help='Find all Installation records for an app',
                             type=str, widget='DirChooser')

    # ########################################################

    # find all installation records DONE
    # ########################################################
    allInstall = subs.add_parser(
        'Install_Entries', help='find all installation records')
    allInstall.add_argument('Log_File',
                             help='Find all Installation records for an app',
                             type=str, widget='FileChooser')

    allInstall.add_argument('Output_Dir',
                             help='Find all Installation records for an app',
                             type=str, widget='DirChooser')


    # Find Deletion/Uninstall Records for an app DONE
    # ########################################################
    delRecOne = subs.add_parser(
        'Uninstall_Entries_One_App', help='Find Deletion/Uninstall Records for an app')
    delRecOne.add_argument('Log_File',
                             help='Find all Installation records for an app',
                             type=str, widget='FileChooser')

    delRecOne.add_argument('App_Name',
                             help='Enter the application name you are looking for (ie :kik)')

    delRecOne.add_argument('Output_Dir',
                             help='Find all Installation records for an app',
                             type=str, widget='DirChooser')


    # ########################################################
    # Find all records for an app DONE
    allRecOneApp = subs.add_parser('All_Entries_One_App', help='Find all records for an app')
    allRecOneApp.add_argument('Log_File',
                             help='Find all Installation records for an app',
                             type=str, widget='FileChooser')

    allRecOneApp.add_argument('App_Name',
                             help='Enter the application name you are looking for (ie :kik)')

    allRecOneApp.add_argument('Output_Dir',
                             help='Find all Installation records for an app',
                             type=str, widget='DirChooser')


    # ########################################################
    # find all Deletion/Uninstall Records DONE
    allDelRecs = subs.add_parser('All_Deletion_Entries', help='Find all Deletion/Uninstall Records')
    allDelRecs.add_argument('Log_File',
                             help='Find all Installation records for an app',
                             type=str, widget='FileChooser')

    allDelRecs.add_argument('Output_Dir',
                             help='Find all Installation records for an app',
                             type=str, widget='DirChooser')


    # ########################################################
    # install and delete for all apps
    allInAndDel = subs.add_parser('All_Install+Delete_Records', help='Find install and delete for all apps')
    allInAndDel.add_argument('Log_File',
                             help='Find all Installation records for an app',
                             type=str, widget='FileChooser')

    allInAndDel.add_argument('Output_Dir',
                             help='Find all Installation records for an app',
                             type=str, widget='DirChooser')


    # parser.parse_args()

    args = parser.parse_args()

    command = args.command

    if command == 'Install_Entries_One_App':
        file = args.Log_File
        out = args.Output_Dir
        app = args.App_Name

        try:
            parseInstallOneApp(file,app,out)
        except Exception as e:
            print(str(e) + "An Error Occured. Check your data sources")

    elif command =='Install_Entries':
        file = args.Log_File
        out = args.Output_Dir

        try:
            parseLogFileAllApps(file,out)
        except Exception as e:
            print(str(e) + "An Error Occured. Check your data sources")

    elif command =='Uninstall_Entries_One_App':
        file = args.Log_File
        out = args.Output_Dir
        app = args.App_Name
        try:
            parseAllDelOneApp(file,app,out)
        except Exception as e:
            print(str(e) + "An Error Occured. Check your data sources")

    elif command == 'All_Entries_One_App':
        file = args.Log_File
        out = args.Output_Dir
        app = args.App_Name
        try:
            parseLogFileAllOneApp(file,app,out)
        except Exception as e:
            print(str(e)+"An Error Occured. Check your data sources")

    elif command =='All_Deletion_Entries':
        file = args.Log_File
        out = args.Output_Dir
        try:
            parseAllDelete(file,out)
        except Exception as e:
            print(str(e) + "An Error Occured. Check your data sources")

    elif command == 'All_Install+Delete_Records':
        file = args.Log_File
        out = args.Output_Dir
        try:
            parseUnAndInAllApps(file,out)
        except Exception as e:
            print(str(e) + "An Error Occured. Check your data sources")


if __name__ == '__main__':
    main()