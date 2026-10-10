readings = [
    {"sensor": "greenhouse", "value": "23.5"},
    {"sensor": "freezer", "value": "not available"},
    {"value": "18.0"},
    {"sensor": "boiler", "value": "140"},
]

def parse_reading(reading):
    sensor = reading["sensor"]
    value = float(reading["value"])
    if value < -50 or value > 100:
        raise ValueError(f"{sensor} reported an unsupported value.")
    return sensor, value

valid_readings = []
for reading in readings:
    try:
        valid_readings.append(parse_reading(reading))
    except (KeyError, TypeError, ValueError) as error:
        print(error)

if valid_readings:
    average = sum(value for _, value in valid_readings) / len(valid_readings)
    print(average)
else:
    print("No readings are valid.")
        
