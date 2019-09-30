import math

### Calculate the relative humidity for one temperature based on the
### relative humidity at another temperature

def rel_humid(RH_input, temperature_input, temperature_output):
    RH_output = RH_input * (temperature_output+273.15)/(temperature_input+273.15) * math.exp(17.62*temperature_input/(243.12+temperature_input))/math.exp(17.62*temperature_output/(243.12+temperature_output))
    return RH_output

### Get input from user on outdoor conditions

ambient_temperature = int(input('What is the current temperature outside? (C)\n'))
ambient_RH = int(input('What is the current relative humidity outside? (%)\n'))
indoor_temperature = int(input('And what is the current temperature inside? (C)\n'))

comparable_humidity = rel_humid(ambient_RH,ambient_temperature,indoor_temperature)

print('If you bring the air outside into the house at indoor temperatures, the indoor relative humidity would be {}.'.format(comparable_humidity))
