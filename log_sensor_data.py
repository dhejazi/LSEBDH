import serial
import openpyxl
import time

# Initialize serial port
ser = serial.Serial('COM3', 115200)  # Replace 'COM3' with your Arduino's serial port

# Create a new Excel workbook and select the active worksheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Sensor Data"

# Add headers to the Excel sheet
ws.append(["Timestamp", "Temperature (C)", "UV Index"])

# Function to read data from Arduino and write to Excel
def log_sensor_data():
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        
        if line:
            # Split the line into components
            parts = line.split()
            if len(parts) == 5 and parts[0] == 'Temperature' and parts[2] == 'UV':
                temperature = float(parts[1])
                uv_index = float(parts[4])
                
                # Append data to the Excel sheet
                ws.append([time.strftime("%Y-%m-%d %H:%M:%S"), temperature, uv_index])
                
                # Save the workbook
                wb.save("sensor_data.xlsx")
                
                print(f"Logged data: Temperature = {temperature} C, UV Index = {uv_index}")

# Start logging data
log_sensor_data()
