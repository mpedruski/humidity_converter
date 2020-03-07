import math

def saturation(pressure, temperature):
    ''' (float, int) -> float
    Calculates the staturation vapour pressure of moist air for given conditions
    '''
    sat = (1.0016 + 3.15*pressure*10**-6 - 0.074/pressure) * 6.112 * math.exp(17.62*temperature/(243.12+temperature))
    return sat

def mass(RH, pressure, temperature):
    ''' (int, float, int) -> float
    Returns the mass of water in a given volume of air under parameters supplied'''
    mw = RH*saturation(pressure,temperature)*molar_mass_water/(ideal_gas_constant*(temperature+273.15))
    return mw

def rel_humid(mass, pressure, temperature):
    '''(float, float, int) -> float
    Returns the relative humidity of air based on mass of water in the air, the air pressure
    and the air temperature'''
    RH = mass*ideal_gas_constant*(temperature+273.15)/(saturation(pressure, temperature)*molar_mass_water)
    return RH

molar_mass_water = 18.01528
ideal_gas_constant = 8.3136

### Get input from user on outdoor conditions

pressure = float(input('What is the current air pressure outside? (kPa) \n'))
ambient_temperature = int(input('What is the current temperature outside? (C)\n'))
ambient_RH = int(input('What is the current relative humidity outside? (%)\n'))
indoor_temperature = int(input('And what is the current temperature inside? (C)\n'))

mass_of_water = mass(ambient_RH,pressure*10,ambient_temperature)
comparable_humidity = rel_humid(mass_of_water,pressure*10,indoor_temperature)

print('If you bring the air outside into the house at indoor temperatures, the indoor relative humidity would be {}.'.format(comparable_humidity))
