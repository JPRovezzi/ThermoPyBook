
#Kinetic Energy
def get_kinetic_energy(mass,velocity,condition,R=0):
    
    gas_constant = R
    #SimpleCondition
    if (condition == "Simple"):
        result = (1/2.) * mass * velocity * velocity
        
    elif (condition == "2D monoatomic fluid"):
        result = (1/2) * mass * velocity * velocity * (1/(gas_constant))
    elif (condition == "3D monoatomic fluid"):
        result = (1/3) * mass * velocity * velocity * (1/(gas_constant))
    else: 
        raise Exception("Error")
    return result

