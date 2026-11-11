# Semester 2 Year 10DGT 2026 - Ultimate Conversion Calculator
# Author: Xander Wolmarans
# Date: 11/11/2026
# Version: 1.2

# Create a function to check if the measurement is a number
def num_check(question):
    
    # creating an error message
    error = "Please enter a number that is more than zero\n"
    while True:
        
        try:
            # ask the user for a number
            response = float(input(question))
            
            # check that the response is more than 0
            if response > 0:
                return response
            
            # if it is not more than 0 then print error message
            else:
                print(error)
                
        # if it is not a number then print error message
        except ValueError:
            print(error)

# DISTANCE EXECUTIONS:
# Create a function to check if the unit of distance is not a number and is instead either mm,cm,m,km
def distance_check(question):
    # create an error message
    error = "\nYour input is invalid, please enter a valid unit of measurement\nexamples: mm,cm,m,km\n"
    while True:
    
        try: 
            # ask the user for a unit of measurement
            response = input(question)
            
            # check that the response is a elegible unit of measurement
            if response == "mm" or response == "cm" or response == "m" or response == "km" or response == "millimeters" or response == "centimeters" or response == "meters" or response == "kilometers" or response == "millimetres" or response == "centimetres" or response == "metres" or response == "kilometres" or response == "millimeter" or response == "centimeter" or response == "meters" or response == "kilometer" or response == "millimetre" or response == "centimetre" or response == "metre" or response == "kilometre":
                return response
                
            else:
                print(error)
                
        except ValueError:
            print(error)
# Create a function to start the distance conversion
def distance_input():
        
        # Get the amount of units (assuming they are valid)
        from_unit = distance_check("\nWhat unit of distance would you like to convert? ")
        amount = float(num_check("How many units? "))
        to_unit = distance_check("To unit? ")

        # Multiply to get to our standard value...
        multiply_by = distance_dict[to_unit]
        standard = amount * multiply_by

        # Divide to get our desired value
        divide_by = distance_dict[from_unit]
        answer = standard / divide_by

        # Display results
        print(f"\nThere are {answer} {to_unit} in {amount} {from_unit }")
# Create a dictionary
distance_dict = {
    "mm" : 1000,
    "cm" : 100,
    "m" : 1, 
    "km" : 0.001,
    "millimeters" : 1000,
    "centimeters" : 100,
    "meters" : 1, 
    "kilometers" : 0.001,
    "millimetres" : 1000,
    "centimetres" : 100,
    "metres" : 1, 
    "kilometres" : 0.001,
    "millimeter" : 1000,
    "centimeter" : 100,
    "meter" : 1, 
    "kilometer" : 0.001,
    "millimetre" : 1000,
    "centimetre" : 100,
    "metre" : 1, 
    "kilometre" : 0.001,
}


# TIME EXECUTIONS:
# Created a time dictionary
time_dict = {
"ms" : 0.001,
    "s" : 1,
    "min" : 60,
    "m" : 60, 
    "h" : 3600,
    "d" : 86400,
    "milliseconds" : 0.001,
    "seconds" : 1,
    "minutes" : 60, 
    "hours" : 3600,
    "days" : 86400,
    "millisecond" : 0.001,
    "second" : 1,
    "minute" : 60, 
    "hour" : 3600,
    "day" : 86400,
}
# Create a function to check if the unit of time is either ms,s,m,h,d
def time_check(question):
    # create an error message
    error = "\nYour input is invalid, please enter a valid unit of time.\nexamples: milliseconds (ms), seconds (s), minutes (min), hours (h), days (d)"
    while True:
    
        # ask the user for a unit of measurement
        response = input(question)
        
        # check that the response is a elegible unit of measurement
        if response == "ms" or response == "s" or response == "min" or response == "h"or response == "m" or response == "d" or response == "milliseconds" or response == "seconds" or response == "minutes" or response == "hours"or response == "m" or response == "days" or response == "millisecond" or response == "second" or response == "minute" or response == "hour" or response == "day":
            return response
            
        else:
            print(error)
# Create a function to start the time conversion
def time_input():
        
        # Get the amount of units (assuming they are valid)
        from_unit = time_check("\nWhat unit of time would you like to convert? ")
        amount = float(num_check("How many units? "))
        to_unit = time_check("To unit? ")

        # divide to get to our standard value...
        divide_by = time_dict[to_unit]
        standard = amount / divide_by

        # multiply to get our desired value
        multiply_by = time_dict[from_unit]
        answer = standard *multiply_by

        # Display results
        print(f"\nThere are {answer} {to_unit} in {amount} {from_unit }")


# MASS EXECUTIONS:
# Created a mass dictionary
mass_dict = {
    "mg" : 0.001,
    "g" : 1,
    "kg" : 1000,
    "t" : 1000000, 
    "Mg" : 0.001,
    "G" : 1,
    "Kg" : 1000,
    "T" : 1000000,   
    "milligrams" : 0.001,
    "grams" : 1,
    "kilograms" : 1000,
    "tonnes" : 1000000,
    "Milligrams" : 0.001,
    "Grams" : 1,
    "Kilograms" : 1000,
    "Tonnes" : 1000000,
}
# Create a function to check if the unit of mass is correct
def mass_check(question):
    # create an error message
    error = "\nYour input is invalid, please enter a valid unit of mass.\nexamples: milligrams (mg), grams (g), kilograms (kg), tonnes (t)"
    while True:
    
        # ask the user for a unit of measurement
        response = input(question)
        
        # check that the response is a elegible unit of measurement
        if response == "mg" or response == "g" or response == "kg" or response == "t"or response == "Mg" or response == "G" or response == "Kg" or response == "T" or response == "milligrams" or response == "grams"or response == "kilograms" or response == "tonnes" or response == "tons" or response == "Milligrams" or response == "Grams"or response == "Kilograms" or response == "Tonnes" or response == "Tons":
            return response
            
        else:
            print(error)
# Create a function to start the time conversion
def mass_input():
        
        # Get the amount of units (assuming they are valid)
        from_unit = mass_check("\nWhat unit of mass would you like to convert? ")
        amount = float(num_check("How many units? "))
        to_unit = mass_check("To unit? ")

        # divide to get to our standard value...
        divide_by = mass_dict[to_unit]
        standard = amount / divide_by

        # multiply to get our desired value
        multiply_by = mass_dict[from_unit]
        answer = standard *multiply_by

        # Display results
        print(f"\nThere are {answer} {to_unit} in {amount} {from_unit }")


# VOLUME EXECUTIONS:
# Created a volume dictionary
vol_dict = {
    "ml" : 0.001,
    "l" : 1,
    "kl" : 1000,
    "ML" : 1000000, 
    "mL" : 0.001,
    "L" : 1,
    "kL" : 1000,
    "MegaLitre" : 1000000,
    "millilitre" : 0.001,
    "litre" : 1,
    "Kilolitre" : 1000,
    "Litre" : 1,
    "kilolitre" : 1000,
    "megalitre" : 1000000, 
    "Millilitre" : 0.001,
}
# Create a function to check if the unit of volume is correct
def vol_check(question):
    # create an error message
    error = "\nYour input is invalid, please enter a valid unit of volume.\nexamples: millilitres (mL), litres (L), kilolitres (kL), megalitres (ML)"
    while True:
    
        # ask the user for a unit of measurement
        response = input(question)
        
        # check that the response is a elegible unit of measurement
        if response == "mL" or response == "L" or response == "kL" or response == "ML"or response == "ml" or response == "l" or response == "kl" or response == "millilitres" or response == "litres" or response == "kilolitres"or response == "megalitres" or response == "Millilitres" or response == "Litres" or response == "Kilolitres" or response == "Megalitres":
            return response
            
        else:
            print(error)
# Create a function to start the time conversion
def vol_input():
        
        # Get the amount of units (assuming they are valid)
        from_unit = vol_check("\nWhat unit of volume would you like to convert? ")
        amount = float(num_check("How many units? "))
        to_unit = vol_check("To unit? ")

        # divide to get to our standard value...
        divide_by = vol_dict[to_unit]
        standard = amount / divide_by

        # multiply to get our desired value
        multiply_by = vol_dict[from_unit]
        answer = standard *multiply_by

        # Display results
        print(f"\nThere are {answer} {to_unit} in {amount} {from_unit }")

    
    
    
# Create a function to make sure the input for the desired conversion is correct
def conversion_check(question):
    
    # creating an error message
    error = "Please enter one of the elegible conversions\n\n------------------------\navailable conversions:\nTIME\nDISTANCE\nMASS\nVOLUME\n------------------------"
    while True:
         
        # ask the user for a type of conversion
        response = input(question)
        
        
        # check that the response is a elegible unit of measurement
        if response == "time" or response == "TIME" or response == "distance" or response == "DISTANCE"or response == "mass" or response == "MASS" or response == "volume" or response == "VOLUME"or response == "Time" or response == "Distance" or response == "Mass" or response == "Volume":
            return response
            
        else:
            print(error)
            
# Create a function to check if the user wants instructions
def instruction_ask(question):
    # creating an error message
    error = "Please enter either 'Yes' or 'No'"
        
    # ask the user for a type of conversion
    response = input(question)
    
    
    # check that the response is a elegible unit of measurement
    if response == "Yes" or response == "yes" or response == "No" or response == "no" or response == "NO" or response == "YES":
        return response
        
    else:
        print(error)







# Welcome the user
print("Welcome to ULTIMATE CONVERSION CALCULATOR\n")

# Create a loop
keep_going = ""
while keep_going == "":
    
# Ask if the user would like instructions
    instructions = instruction_ask("Would you like instructions?\nYes/No\n")
    if instructions == "Yes" or instructions == "yes" or instructions == "YES":
        print("\nChose from an available unit of conversion \n\n------------------------\navailable conversions:\nTIME\nDISTANCE\nMASS\nVOLUME\n------------------------")
        # Ask which conversion the user would like to preform
        selected_conversion = conversion_check("\nWhat conversion would you like to execute? ")
            
    elif instructions == "NO" or instructions == "No" or instructions == "no":
        # Ask which conversion the user would like to preform
        selected_conversion = conversion_check("\nWhat conversion would you like to execute? ")
    
    
        # Check if the user would like to convert distance
        if selected_conversion == "DISTANCE" or selected_conversion == "Distance" or selected_conversion == "distance":
            distance_input()
            
        # Check if the user would like to convert time
        elif selected_conversion == "Time" or selected_conversion == "TIME" or selected_conversion == "time":
            time_input()
        
        # Check if the user would like to convert mass
        elif selected_conversion == "Mass" or selected_conversion == "mass" or selected_conversion == "MASS":
            mass_input()
            
        # Check if the user would like to convert volume
        elif selected_conversion == "Volume" or selected_conversion == "volume" or selected_conversion == "VOLUME":
            vol_input()
    
    
   
    

    
# Ask user if they want to keep going
keep_going = input("Press enter to keep going or any key to quit. \n")


print("Thank you for using the area / perimeter calculator")
