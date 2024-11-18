from time import sleep
# Define GPIO pin numbers for devices
lamp_pin = 0  # D0 for Lamp
fan_pin = 1   # D1 for Fan
door_pin = 2  # D2 for Door
alarm_pin = 4  # D4 for Alarm

# Define GPIO pin numbers for sensors
motion_sensor_pin = 3  # D3 for Motion Sensor
temp_sensor_pin = 'A0'  # A0 for Temperature Sensor

# Historical data for learning (adaptive behavior)
temp_history = []

# Functions to simulate sensor input (replace with actual sensor reading in Packet Tracer)
def read_motion_sensor():
    # Simulate reading from motion sensor (1 = motion detected, 0 = no motion)
    return 0  # Change this value for testing

def read_temp_sensor():
    # Simulate reading from temperature sensor (returns temperature in °C)
    return 35  # Change this value for testing

# Functions to control devices
def control_lamp(status):
    if status == "ON":
        print("Lamp is ON")
    else:
        print("Lamp is OFF")

def control_fan(status):
    if status == "ON":
        print("Fan is ON (High Speed)")
    else:
        print("Fan is OFF")

def control_door(status):
    if status == "OPEN":
        print("Door is OPEN")
    else:
        print("Door is CLOSED")

def control_alarm(status):
    if status == "ON":
        print("Alarm is ON")
    else:
        print("Alarm is OFF")

# AI learning function to adjust behavior based on temperature history
def adjust_fan_based_on_temperature():
    if len(temp_history) >= 5:  # Check if we have enough temperature data points
        avg_temp = sum(temp_history[-5:]) / 5  # Calculate average of last 5 readings
        print("Average Temperature: " + str(avg_temp) + " degrees")
        
        if avg_temp > 30:
            control_fan("ON")
        else:
            control_fan("OFF")
    else:
        current_temp = read_temp_sensor()
        if current_temp > 30:
            control_fan("ON")
        else:
            control_fan("OFF")

# Main loop to control devices based on sensor input
while True:
    # Read sensors
    motion_detected = read_motion_sensor()
    current_temp = read_temp_sensor()

    # Store temperature readings for learning
    temp_history.append(current_temp)

    # Control door and lamp based on motion sensor input
    if motion_detected:
        control_door("OPEN")
        control_lamp("ON")
        control_alarm("ON")  # Turn on alarm if motion is detected
    else:
        control_door("CLOSE")
        control_lamp("OFF")
        control_alarm("OFF")  # Turn off alarm when there's no motion

    # Use AI learning to control the fan based on temperature history
    adjust_fan_based_on_temperature()

    # Activate alarm if temperature is too high
    if current_temp > 40:
        control_alarm("ON")
    else:
        control_alarm("OFF")
    sleep(5)  # Wait for 5 seconds before the next reading
