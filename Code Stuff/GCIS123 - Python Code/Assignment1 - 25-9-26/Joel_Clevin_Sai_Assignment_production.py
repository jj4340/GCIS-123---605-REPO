#GCIS Assignment 01 - 25-9-26 V2

"""
Your group must design this logic.
For example, you must decide how your program distinguishes between:
•	Normal
•	High
•	Critical
**when a reading is above the normal range.**

WORKING RULE:
Normal - in between minimum and maximum
High - higher than normal maximum value
Critical - higher than 2 times the maximum value.

Why use this: 
Usually if the device has 200% maximum energy i.e 2 times the maximum energy:
It is considered critical.
"""

cv = 2
#Task 1
#Task 1.1 - Getting the name of the device
#1
def getting_device_normal_range(name):
    """
    This function is used to return the normal energy range of every device connected to HomeSense.
    (We use the short name of the device here because it is a better input as it has less chance to be wrong.)
    When the function gets a device name; it will use If condition to find out what device is being mentioned.
    Then it will return the minimum normal value and maximum normal value.
    This value is returned by "return min, max".
    We will be using the maximum value for the second function.
    """
    while True:
        if (name=="LED Light"):
            #"For LED Light; normal range is 0.01-0.1 kWh")
            return 0.01, 0.1
        elif (name=="Television"):
            #"For Television; normal range is 0.05-0.5 kWh"
            return 0.05,0.5
        elif (name=="Refrigerator"):
            #"For Refrigerator; normal range is 0.1-1.5 kWh"
            return 0.1,1.5
        elif (name=="Washing Machine"):
            #"For Washing Machine; normal range is 0.3-2.5 kWh"
            return 0.3,2.5
        elif (name=="Air Conditioner"):
            #"For Television; normal range is 0.5-5.0 kWh"
            return 0.5,5.0
        else:
            """
            This is the Unknown device condition.
            If the device is not recognized and is an unknown, then it will print
            "Device mentioned is not identified."
            """
            print("Device mentioned is not identified.")
            break

#-------------------------------------------------------------------------------------------------------------------------------#

#Task 7 - Boundary Conditions
#2
def check_zero_or_negative(reading):
    """
    This function is used to handle zero or negative readings.
    We use it in the getting_device_status() and getting_energy_cost() function.
    If the reading is 0 or negative, it will r eturn "NIL".
    If the reading is postive and not equal to 0, the function returns the reading itself.
    """
    if (reading<0):
        return "NIL"
    elif (reading == 0):
        return "NIL"
    else:
        return reading

#-------------------------------------------------------------------------------------------------------------------------------#

#Task 1.2 - Getting the device status\
#3
def getting_device_status(max,reading):
    """
    This function will take the reading of the device and maximum value given by the first function.
    It does not take device name because it does not need it as the maximum value indicates what device is being used.
    Once it takes the reading of the device and maximum value; it will decide the status of the device.
    If reading is less than maximum = Normal
    If reading is higher than maximum but less that CV*max = High
    If reading is higher than CV*max = Critical
    (CV means the critical variable; what we multiply to the high value of the normal range to decide the limit for critical energy)
    """
    r = check_zero_or_negative(reading)
    if (r=="NIL"):
        return "INVALID READING"
    elif (r < max):
        return "NORMAL"
    elif((r >=max) and (r < cv*max)):
        return "HIGH"
    elif((r >= cv*max)):
        return "CRITICAL"

#Task 1.3 - Getting the alert. Whether device requires attention or not.
#4
def requires_alert(verdict):
    """
    This function answers whether a given device needs attention based on the energy readings.
    If the verdict from the device_energy_verdict is NORMAL:
    It will tell false. Meaning the device does not need attention.
    If the verdict from the device_energy_verdict is HIGH or CRITICAL:
    It will tell true. Meaning the device does need attention.
    """
    if (verdict=="NORMAL"):
        return False
    elif (verdict=="HIGH"):
        return True
    elif (verdict=="CRITICAL"):
        return True

#-------------------------------------------------------------------------------------------------------------------------------#

#Task 2 -Getting the cost for running the device
cost = 0.23
#5
def getting_energy_cost(reading, cost):
    """
    This function will take a reading and the cost of energy consumption.
    It will find the total energy cost which is reading * cost and return it as energy_c
    It uses check_zero_or_negative() to check if the reading is 0 or negative.
    If it is zero of negative, that function returns "NIL".
    If it returns "NIL", the getting_energy_cost() function will return "INVALID READING" as reading is incorrect.
    """
    r = check_zero_or_negative(reading)
    if (r == "NIL"):
        return "INVALID READING"
    else:
        energy_c = r*cost
        return energy_c

#-------------------------------------------------------------------------------------------------------------------------------#

#Task 3 - Give feedback to the device's functioning
#6
def rec(device,energy,max):
    """
    This device is used to provide feedback based on the functioning of the device.
    If the device has normal energy, it means it is functioning normally.
    If the device has slightly high energy (above the maximum normal value and below 1.5 times the maximum):
    It will say "The device might overheat, so be cautious!"
    If the device has very high energy (above 1.5 times the maximum and below CV times maximum):
    It will say "The device is overheating, it may cause immediate failure."
    If the device has extremely high energy (above CV times the maximum limit):
    It will say "The decie will stop working, fix the problem as soon as possible!"
    """
    d = device
    if energy<max:
        return "The "+d+" is functioning normally so no need to worry!"
    elif energy>=max and energy<(1.5*max):
        return "The "+d+" functioning might overheat, so be cautious!"
    elif energy>=(1.5*max) and energy<(cv*max):
        return "The "+d+" is overheating, it may cause immediate failure."
    elif energy>=(cv*max):
        return "WARNING! The "+d+" functioning will stop working, fix the problem as soon as possible !"

#-------------------------------------------------------------------------------------------------------------------------------#

#Task 4 - Doing the analysis for multiple devices.
#7
devices = "LED Light,LED Light,Television,Television,Refrigerator,Refrigerator,Washing Machine,Washing Machine,Air Conditioner,Air Conditioner"
list_device = devices.split(",")
reading = "0.06 0.18 0.32 1.20 0.80 2.20 1.40 4.50 2.80 7.50"
list_reading = reading.split()

def compile_function(l_d, l_r,t):
    """
    This function uses all the functions we created prior.
    It uses getting_device_normal_range() to give the normal range of the device.
    It uses getting_device_status() to get the status of the device.
    It uses requires_alert() to get the verdict on whether the device needs attention or not.
    It uses rec() to get the feedback of the devices functioning.
    It uses getting_energy_cost() to find the energy consumption cost of the device.
    It displays all the values.
    At the end, it returns the energy cost and status of the device for use in other functions.
    """
    device_name = l_d[t]
    min_v, max_v = getting_device_normal_range(device_name)
    status = getting_device_status(max_v,float(l_r[t]))
    verdict = requires_alert(status)
    feedback = rec(device_name,float(l_r[t]),max_v)
    e_cost = getting_energy_cost(float(l_r[t]), cost)
    print("Device =",device_name,"\nEnergy level =",l_r[t],"\nStatus =", status,"\nRequires Attention =", verdict,"\nFeedback =",feedback,"\nEnergy cost =", e_cost,"\n")
    return e_cost, status

#-------------------------------------------------------------------------------------------------------------------------------#

#Task 5 - Doing analysis from multiple analysis
#8
def count_readings(status):
    """
    This function takes the status of the device from getting_device_status().
    It creates 3 variables: 
    n - number of normal readings
    h - number of high readings
    cr - number of critical readings
    If the status is "NORMAL", n is added 1. If it is "HIGH", h is added 1. If it is "CRITICAL", cr is added 1.
    The function returns the values of n, h and cr.
    """
    n = 0
    h = 0
    cr = 0  
    if (status == "NORMAL"):
        n += 1
    elif (status == "HIGH"):
        h += 1
    elif (status == "CRITICAL"):
        cr += 1
    return n,h,cr

#9
def highest_reading_index(l_r):
    """
    This function is used to get the device with the highest energy reading.
    It takes input as a list of readings.
    It sets 3 variables:
    Highest_reading = Initialized at first to the first reading in the list (l_r[0]).
    Highest_index = This is the index of the chosen reading.
    Current_index = This value is used in the loop statement.
    For every reading in the list, if the reading (n) is greater than highest_reading:
    It will set the highest_reading variable to the reading of n. 
    Then the highest_index variable is set to the current_index variable. This gives the index of that reading.
    At the end of the loop, current_index is added 1. This basically counts and tells which reading, the variable n is set to.
    In the end, the function returns the highest_index which is used to find the name of the device with the highest reading. 
    """
    highest_reading = l_r[0]
    highest_index = 0
    current_index = 0
    for n in l_r:
        if (n > highest_reading):
            highest_reading = n
            highest_index = current_index
        current_index += 1
    return highest_index

#10
def mul_analysis(l_d,l_r):
    """
    This function uses a loop to analyze several functions.
    It creates  6 variables:
    t - total number of devices in the list of devices.
    total_e - the sum of energy consumption from all devices.
    t_cost - the sum of energy cost from all devices.
    no_normal, no_high, no_critical - the total number of normal, high and critical readings respectively.
    The loop iterates for every device in the list of devices. 
    The compile function returns the status and energy cost of the chosen device.
    The reading from the list of readings (index is given by the value of t) is added to total_e
    count_readings(status) uses the status to set the value of n, h, cr to one. 
    Then that value gets added to no_normal, no_high, no_critical for the final count. \
    t is added one so that during the next iteration, the loop would continue to the next device in the list and repeat the process.
    It also uses the highest_reading_index() to find the index of the device with the highest energy reading.
    In the end, it returns all the variables created as well as the device with the highest energy.\
    """
    t = 0
    total_e = 0
    t_cost = 0
    no_normal = 0
    no_high = 0
    no_critical = 0

    for x in l_d:
        e_cost, status = compile_function(l_d,l_r,t)
        total_e += float(l_r[t])
        t_cost += e_cost
        n, h, cr = count_readings(status)
        no_normal += n
        no_high += h
        no_critical += cr
        t += 1
        
    index_of_device_with_high = highest_reading_index(l_r)
    h_device = l_d[index_of_device_with_high]

    return t, total_e, t_cost, no_normal, no_high, no_critical, h_device


#-------------------------------------------------------------------------------------------------------------------------------#

#Task 6 - Getting the home-sense report.
#11
def report(t, total_e, t_cost, no_normal, no_high, no_critical, h_device):
    """
    This is the last function of the code.
    It takes 7 parameters from the mul_analysis function:

    t - total number of devices
    total_e - total energy consumption
    t_cost - total energy cost
    no_normal, no_high, no_critical - total number of high, critical and normal readings
    h_device - device with the highest energy consumption

    It will take these 7 parameters and present them in a report.
    """
    print("========== HomeSense Report ==========\n")
    print("Readings analyzed:",t)
    print("No of Normal readings:", no_normal)
    print("No of High readings:", no_high)
    print("No of Critical readings:", no_critical)
    print("Readings requiring attention:", no_high + no_critical)
    print("Total energy:",total_e,"kWh")
    print("Estimated cost: AED",t_cost)
    print("Highest consumption:",h_device)
    print("\n========== HomeSense Report ==========\n")

#-------------------------------------------------------------------------------------------------------------------------------#

t, total_e, t_cost, no_normal, no_high, no_critical, h_device = mul_analysis(list_device, list_reading)
report(t, total_e, t_cost, no_normal, no_high, no_critical, h_device)
