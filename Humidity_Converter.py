import math

def rel_humid(RH_input, temperature_input, temperature_output):
    ''' (int, int, int) -> float
    Returns the relative humidity of air that would result from changing
    the temperature from temperature_input to temperature_output and holding
    the amount of water in the air constant.
    '''
    RH_output = RH_input * (temperature_output+273.15)/(temperature_input+273.15) * math.exp(17.62*temperature_input/(243.12+temperature_input))/math.exp(17.62*temperature_output/(243.12+temperature_output))
    return RH_output

### Get input from user on outdoor conditions

ambient_temperature = int(input('What is the current temperature outside? (C)\n'))
ambient_RH = int(input('What is the current relative humidity outside? (%)\n'))
indoor_temperature = int(input('And what is the current temperature inside? (C)\n'))

### Calculate and provide output on what outdoor humidity would yield at indoor temperatures

comparable_humidity = rel_humid(ambient_RH,ambient_temperature,indoor_temperature)

print('If you bring the air outside into the house at indoor temperatures, the indoor relative humidity would be {}.'.format(comparable_humidity))
