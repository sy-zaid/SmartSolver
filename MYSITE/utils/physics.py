"""Velocity Section (PC-whole-div-2):
  Input:
    - Distance: input-distance
      Units (Dropdown): dropdown-units-distance
        - Meters (m)
        - Kilometers (km)
        - Feet (ft)

    - Time: input-time
      Units (Dropdown): dropdown-units-time
        - Seconds (s)
        - Hours (h)

  Buttons:
    - Clear Button: clearButton
    - Solve Button: solveButton

  Output:
    - Velocity: res-mean
"""

def convertDistanceToSI(distance, unit):
    # Define conversion factors
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'feet': 0.3048,  # 1 foot is approximately 0.3048 meters
    }

    # Check if the provided unit is valid
    if unit not in conversion_factors:
        print('Invalid unit provided.') 
        return None

    # Perform the conversion
    converted_distance = float(distance) * conversion_factors[unit]

    return converted_distance

# Example usage:
# distance_in_meters = convertDistanceToSI(100, 'kilometers')
# print(f'Converted distance: {distance_in_meters} meters')

def convertTimeToSI(time, unit):
    # Define conversion factors
    conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,  # 1 hour is 3600 seconds
    }

    # Check if the provided unit is valid
    if unit not in conversion_factors:
        print('Invalid unit provided.')
        return None

    # Perform the conversion
    converted_time = float(time) * conversion_factors[unit]

    return converted_time


def convertVelocityToSI(velocity, unit):
    # Define conversion factors
    conversion_factors = {
        'meter-per-second': 1,
        'kilometer-per-hour': 0.277778,  # 1 km/h is approximately 0.277778 m/s
        'feet-per-second': 0.3048,  # 1 ft/s is approximately 0.3048 m/s
    }

    # Check if the provided unit is valid
    if unit not in conversion_factors:
        print('Invalid unit provided.')
        return None

    # Perform the conversion
    converted_velocity = float(velocity) * conversion_factors[unit]

    return converted_velocity

# Example usage:
# velocity_in_meters_per_second = convertVelocityToSI(50, 'kilometers-per-hour')
# print(f'Converted velocity: {velocity_in_meters_per_second} m/s')

def convertAccelerationToSI(acceleration, unit):
    # Define conversion factors
    conversion_factors = {
        'meters-per-second-squared': 1,
        'kilometers-per-hour-squared': 2.77778e-7,  # 1 km/h² is approximately 2.77778e-7 m/s²
    }

    # Check if the provided unit is valid
    if unit not in conversion_factors:
        print('Invalid unit provided.')
        return None

    # Perform the conversion
    converted_acceleration = float(acceleration) * conversion_factors[unit]

    return converted_acceleration

def convertMassToSI(mass, unit):
    # Define conversion factors
    conversion_factors = {
        'kilograms': 1,
        'grams': 0.001,  # 1 gram is 0.001 kilograms
        'milligrams': 1e-6,  # 1 milligram is 1e-6 kilograms
    }

    if unit not in conversion_factors:
        print('Invalid unit provided.')
        return None

    
    converted_mass = float(mass) * conversion_factors[unit]
    return converted_mass
    


def calcVelocity(distance,time,dddistance,ddtime):
    siu_distance = float(convertDistanceToSI(distance,dddistance))
    siu_time = float(convertTimeToSI(time,ddtime))
    velocity = round(siu_distance / siu_time,4)
    return velocity

def calcAcceleration(final_velocity,initial_velocity,time,ddvelocity,ddtime):
    siu_initial_velocity = float(convertVelocityToSI(initial_velocity, ddvelocity))
    siu_final_velocity = float(convertVelocityToSI(final_velocity, ddvelocity))
    siu_time = float(convertTimeToSI(time, ddtime))
    acceleration = round((siu_final_velocity - siu_initial_velocity) / siu_time,4)
    return acceleration

def calcFrequency(time,ddtime):
    siu_time = float(convertTimeToSI(time,ddtime))
    freq = round(1/siu_time,4)
    return freq

# Example usage:
# inp_time = "10"  # Replace with your actual input
# ddtime = "seconds"  # Replace with your actual input
# calcFrequency(inp_time, ddtime)


def calcForce(acceleration,mass,ddacceleration,ddmass):
    # print(ddmass)
    siu_mass = float(convertMassToSI(mass,ddmass))
    siu_acceleration = float(convertAccelerationToSI(acceleration,ddacceleration))
    force = round((siu_acceleration * siu_mass),4)
    return force


