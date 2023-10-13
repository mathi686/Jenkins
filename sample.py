# a=int(input("Enter the a value : "))
# b=int(input("Enter the b value : "))
# c=int(input("Enter the c value : "))
# d=int(input("Enter the d value : "))
# e=int(input("Enter the e value : "))
# total=(a+b+c+d+e/5)
# print("avarage" , total)
# if(total>20):
#     print("pass")
# else:
#     print("faill")
# score = int(input("enter the mark : "))
#
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "Fail"
#
# print(f"Your grade is {grade}")

# print(e_count)
# print(o_count)
#
# # for i in "apple"
# e_count=0
# o_count=0
# for i in range (1,101):
#     if(i%3==0 and i%5==0):
#         e_count=e_count+1
#         o_count=o_count+1
#     else:
#         p



import subprocess

# Define the Nginx installation command for Debian/Ubuntu
install_command = "sudo apt-get update && sudo apt-get install -y nginx"

# Execute the installation command
try:
    subprocess.check_call(install_command, shell=True)
    print("Nginx has been successfully installed.")
except subprocess.CalledProcessError as e:
    print(f"Error installing Nginx: {e}")
