'''Python program should continuously monitor the CPU usage of the local machine and 
   If the CPU usage exceeds a predefined threshold (e.g., 80%), an alert message should be displayed'''
#importing time module for Pause Program from executing and psutil module system utalization 
import time
import psutil
# Limit has set to 1 so we can check the output because CPU uses never cross 10
limit = 1 
#Definining the function to monitor the CPU Usaes
def monitor_cpu_usage():
    print("Monitoring CPU usage...")
    #While loop to continously print the CPU Alert
    while True:
        try:
            cpu_status = psutil.cpu_percent(time.sleep(1))
            #This condition will check if CPU status is greater than limit defined print the Alert!
            if cpu_status > limit:
                print(f"\033[31mAlert! CPU usage exceeds threshold:{cpu_status}%\033[0m")
        except Exception as e:
            print(f"An error occurred: {e}")
#Calling the monitor_cpu_usage function 
monitor_cpu_usage()
