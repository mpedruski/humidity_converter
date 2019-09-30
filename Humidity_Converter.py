import math

molar_mass_water = 18.01528
ideal_gas_constant = 8313.6 ### Assumes mass reported in kg, while molar mass in g

### Calculate saturation vapour pressure of moist air for given conditions

def saturation(pressure, temperature):
    sat = (1.0016 + 3.15*pressure*10**-6 - 0.074/pressure) * 6.112 * math.exp(17.62*temperature/(243.12+temperature))
    return sat

### Calculate mass of water in a given volume of air

def mass(RH, pressure, temperature):
    mw = RH*saturation(pressure,temperature)*molar_mass_water/(ideal_gas_constant*(temperature+273.15))
    return mw

### Calculate the relative humidity based on a given mass of water
def rel_humid(mass, pressure, temperature):
    RH = mass*ideal_gas_constant*(temperature+273.15)/(saturation(pressure, temperature)*molar_mass_water)
    return RH

### Get input from user on outdoor conditions

pressure = float(input('What is the current air pressure outside? (kPa) \n'))
ambient_temperature = int(input('What is the current temperature outside? (C)\n'))
ambient_RH = int(input('What is the current relative humidity outside? (%)\n'))
indoor_temperature = int(input('And what is the current temperature inside? (C)\n'))

mass_of_water = mass(ambient_RH,pressure*10,ambient_temperature)
comparable_humidity = rel_humid(mass_of_water,pressure*10,indoor_temperature)

print('If you bring the air outside into the house at indoor temperatures, the indoor relative humidity would be {}.'.format(comparable_humidity))
