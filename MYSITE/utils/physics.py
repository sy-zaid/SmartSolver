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
        'grams': 0.001,        # 1 gram is 0.001 kilograms
        'milligrams': 1e-6,    # 1 milligram is 1e-6 kilograms
        'pounds': 0.453592,     # 1 pound is approximately 0.453592 kilograms
        'ounces': 0.0283495,    # 1 ounce is approximately 0.0283495 kilograms
    }

    if unit not in conversion_factors:
        print('Invalid unit provided.')
        return None

    converted_mass = float(mass) * conversion_factors[unit]
    return converted_mass

def convertSIToMass(si_mass, target_unit):
    # Define conversion factors for the inverse conversion
    inverse_conversion_factors = {
        'kilograms': 1,
        'grams': 1000,        # 1 kilogram is 1000 grams
        'milligrams': 1e6,    # 1 kilogram is 1e6 milligrams
        'pounds': 2.20462,    # 1 pound is approximately 2.20462 kilograms
        'ounces': 35.274,     # 1 ounce is approximately 35.274 grams
    }

    if target_unit not in inverse_conversion_factors:
        print('Invalid target unit provided.')
        return None

    converted_mass = float(si_mass) * inverse_conversion_factors[target_unit]
    return converted_mass

def convLengthToSI(length, unit):
    length_conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 0.0254,  # Corrected factor for inches
        'feet': 0.3048,
    }
    if unit not in length_conversion_factors:
        print('Invalid length unit provided.')
        return None
    converted_length = float(length) * length_conversion_factors[unit]
    return converted_length

def convSIToLength(si_length, target_unit):
    inverse_length_conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 39.3701,  # Corrected factor for inches
        'feet': 3.28084,
    }
    if target_unit not in inverse_length_conversion_factors:
        print('Invalid target length unit provided.')
        return None
    converted_length = float(si_length) * inverse_length_conversion_factors[target_unit]
    return converted_length

# a = convertMassToSI(10,'grams')
# b = convertSIToMass(a,'ounces')
# print(b)

def convTimeToSI(time, unit):
    time_conversion_factors = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400,  # 1 day is 86400 seconds
        # Add more time units as needed
    }
    if unit not in time_conversion_factors:
        print('Invalid time unit provided.')
        return None
    converted_time = float(time) * time_conversion_factors[unit]
    return converted_time

def convSIToTime(si_time, target_unit):
    inverse_time_conversion_factors = {
        'seconds': 1,
        'minutes': 1 / 60,
        'hours': 1 / 3600,
        'days': 1 / 86400,  # 1 second is 1/86400 days
        # Add more time units as needed
    }
    if target_unit not in inverse_time_conversion_factors:
        print('Invalid target time unit provided.')
        return None
    converted_time = float(si_time) * inverse_time_conversion_factors[target_unit]
    return converted_time

def convTemperatureToSI(temperature, unit):
    if unit == 'celsius':
        converted_temperature = float(temperature) + 273.15
    elif unit == 'fahrenheit':
        converted_temperature = float(float(temperature) - 32) * 5/9 + 273.15
    elif unit == 'kelvin':
        converted_temperature = float(temperature)

    return round(converted_temperature,4)

def convSIToTemperature(temperature, target_unit):
    if target_unit == 'celsius':
        converted_temperature = float(temperature) - 273.15
    elif target_unit == 'fahrenheit':
        converted_temperature = float(float((temperature) - 273.15) * 9/5 + 32)
    elif target_unit == 'kelvin':
        converted_temperature = float(temperature)
    else:
        raise ValueError("Invalid desired temperature unit. Supported units are Celsius, Fahrenheit, and Kelvin.")

    return round(converted_temperature,4)



def convPowerToSI(power, unit):
    power_conversion_factors = {
        'watts': 1,
        'kilowatts': 1000,
        'megawatts': 1e6,  # 1 megawatt is 1e6 watts
        'horsepower': 745.7,  # 1 horsepower is approximately 745.7 watts
        # Add more power units as needed
    }
    if unit not in power_conversion_factors:
        print('Invalid power unit provided.')
        return None
    converted_power = float(power) * power_conversion_factors[unit]
    return converted_power

def convSIToPower(si_power, target_unit):
    inverse_power_conversion_factors = {
        'watts': 1,
        'kilowatts': 0.001,
        'megawatts': 1e-6,  # 1 watt is 1e-6 megawatts
        'horsepower': 1 / 745.7,  # 1 watt is approximately 1/745.7 horsepower
        # Add more power units as needed
    }
    if target_unit not in inverse_power_conversion_factors:
        print('Invalid target power unit provided.')
        return None


# -----------------------------------------------------------------#
# ------------------------- CALCULATIONS ------------------------- #
# ----------------------------------------------------------------- #
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




# ------------------------- FOR CONVERTERS ------------------------- #
def convMass(input_mass,dd_mass_from,dd_mass_to):
    temp = convertMassToSI(input_mass,dd_mass_from)
    res = convertSIToMass(temp,dd_mass_to)
    return res

def convLength(input_length,dd_length_from,dd_length_to):
    temp = convLengthToSI(input_length,dd_length_from)
    res = convSIToLength(temp,dd_length_to)
    return res

def convTime(input_time,dd_time_from,dd_time_to):
    temp = convTimeToSI(input_time,dd_time_from)
    res = convSIToTime(temp,dd_time_to)
    return res

def convTemperature(input_temperature,dd_temperature_from,dd_temperature_to):
    temp = convTemperatureToSI(input_temperature,dd_temperature_from)
    res = convSIToTemperature(temp,dd_temperature_to)
    return res

def convPower(input_power,dd_power_from,dd_power_to):
    temp = convPowerToSI(input_power,dd_power_from)
    res = convSIToPower(temp,dd_power_to)
    return res