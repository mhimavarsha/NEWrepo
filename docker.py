import os

os.system("tput setaf 2")
print("\t\t\twelcome to my menu")
os.system("tput setaf 7")

os.system("zenity --info --text= 'welcome to lw ' ")

print("\t\t\t------------------------"   )
print()

print("where you want to run ur program (local/remote):", end = '')
#myhost = input()
#print(myhost)

#if myhost == "local":



while True:
    print("""
press 1: To manage Docker
press 2: To control HTTPD
press 3: To manage AWS
press 4: To manage Hadoop
press 5: to exit
    """)
    choice = int(input("Enter proper choice from menu: "))
    if choice == 1:
        while True:
                print("""
                Press 1: TO start Docker (Docker must be installed)
                Press 2: To see Docker Info
                Press 3: To see Docker Images
                Press 4: To Run Docker
                Press 5: To see All Running OS
                Press 6: To Pull an Image
                Press 7: To stop container
                Press 8: To delete container
                Press 9: To stop Docker
                Press 10: To Exit
                         """)
        print("enter ur choice:", end='')
        ch = input()
        print(ch)


        if int(ch) == 1:
                        os.system("systemctl start docker")
        elif int(ch) == 2:
                        os.system("docker info")
        elif int(ch) == 3:
                        os.system("docker images")
        elif int(ch) == 4:
                            image = input("\nGive the Image Name: ")
                            verion = input("\nEnter Requied Version: ")
                            os_name = input("\nEnter the Name you want to Give")
                            print("docker run -it --name {} {}:{}".format(image, version , os_name))
                            os.system("docker run -it --name {} {}:{}".format(os_name, iamge, version))
        elif int(ch) == 5:
                            os.system("docker ps - a")
        elif int(ch) == 6:
                            image = input("\nGive the Image Name: ")
                            version = input("\nEnter Version: ")
                               
                            os.system("docker pull {}:{}".format(image,version))                    
        elif int(ch) == 7:
                            os_name = input("Enter the OS name which you want to Delete: ")
                            os.system("docker stop {}".format(os_name))
        elif int(ch) == 8:
                            os_name = input("Enter the OS Name which you want to Delete: ")
                            os.system("docker rm {}".format(os_name))
        elif int(ch) == 9:
                            os.system("systemctl stop docker")
                            print("----------Docker has been stopped---------")
        elif int(ch) == 9:
                            break
        else:
                        print("you have enter wrong choice")
    elif choice == 2:
        
