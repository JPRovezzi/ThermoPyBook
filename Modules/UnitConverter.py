
#Temperature

##Fahrenheit to Celcius
def convert_Temperature(T,Unit1,Unit2):
    if (Unit1 == "F" and Unit2 == "C"):
        result = (5/9)*(T-32)
    elif (Unit1 == "C" and Unit2 == "F"):
        result  = (9/5)*T + 32
    
    elif (Unit1 == "C" and Unit2 == "K"):
        result = T + 273.15
    elif (Unit1 == "K" and Unit2 == "C"):
        result = T - 273.15   

    elif (Unit1 == "F" and Unit2 == "R"):
        result = T + 459.67
    elif (Unit1 == "R" and Unit2 == "F"):
        result = T - 459.67
    
    elif (Unit1 == "K" and Unit2 == "R"):
        result = T * (18/10)
    elif (Unit1 == "R" and Unit2 == "K"):
        result = T * (10/18)

    elif (Unit1 == "F" and Unit2 == "K"):
        result = (5/9)*(T-32) + 273.15
    elif (Unit1 == "K" and Unit2 == "F"):
        result = (T - 273.15) * (9/5) + 32

    elif (Unit1 == "R" and Unit2 == "C"):
        result = T * (10/18) - 273.15 
    elif (Unit1 == "C" and Unit2 == "R"):   
        result = (T + 273.15) * (18/10)
    elif (Unit1 == Unit2):
        result = T
    else:
        raise Exception("Something went wrong")
    
    return result

##Celcius to Fahrenheit
def convert_TF_to_TC(T):
    return (5/9)*(T-32)
