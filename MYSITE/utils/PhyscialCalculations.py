def calculating_velocity():
    # be careful of units
    D = float(input("Enter Distance: "))
    T = float(input("Enter Time: "))
    velocity = D/T
    print("Velocity = {} m/s".format(velocity))
    
calculating_velocity()


     # be careful of units
def calculating_acceleration():
    intial_velocity = float(input("Enter Initial Velocity: "))
    final_velocity = float(input("Enter Final Velocity: "))
    time = float(input("Enter Time Taken: "))
    acceleration = (final_velocity - intial_velocity)/time
    print("Acceleration = {} m/s^2".format(acceleration))

calculating_acceleration()
    
     # be careful of units
def calculating_frequency():	
    T = float(input("Enter Time-Period: "))
    f = 1/T
    print("Frequency = {} Hz".format(f))
    
calculating_frequency()
    
def calculating_pressure():
    F = float(input("Enter Force: "))
    A = float(input("Enter Area: "))
    P = F/A
    print("Pressure = {} Pa".format(P))

calculating_pressure()

def calculating_force():
    m = float(input("Mass = "))
    a = float(input("Acceleration = "))
    F = m*a 
    print("Force = {} N".format(F))
    
calculating_force()
    
        
        
