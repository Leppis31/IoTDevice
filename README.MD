This is code for an IoT device. The IoT device is a temperature sensor that utilizes two sensors.

This Python script is designed to be used with an IoT temperature sensor device that reads data from a potentiometer (connected to pin 27 of the microcontroller) and sends the data to a remote server via HTTP. The script connects the device to a Wi-Fi network, continuously reads sensor values, processes the data, and then sends it as a query parameter to a specified API endpoint. The data is sent every 15 seconds.

Overview:
This program allows an IoT device to read temperature or sensor values from a potentiometer, convert the raw data to a percentage, and then send it to a server. It handles Wi-Fi connectivity and data transmission over HTTP.

Requirements:
Microcontroller (e.g., ESP32 or ESP8266) with support for MicroPython
Wi-Fi network credentials (SSID and password)
Remote server with an API endpoint capable of handling query parameters for data input
Script Components:
Wi-Fi Connection (connectWifi() function):

Activates the WLAN interface on the device.
Connects to the specified Wi-Fi network using the provided SSID and password.
Waits until the device is connected to the network and displays the network configuration.
Sensor Data Collection (operate() function):

Reads raw data from a potentiometer sensor connected to GPIO pin 27.
Converts the raw reading from a 16-bit ADC value to a percentage (scaled from 0 to 100).
Sends the processed data to the specified server endpoint.
Data Sending (sendData(value) function):

Sends the sensor data to a remote server as a query parameter in a GET request.
The server URL (DATA_ENDPOINT) is specified in the script.
The function prints the server's response (if successful) or a failure message in case of an error.
Main Flow (main() function):

Calls the connectWifi() function to establish a network connection.
Starts the sensor operation in the operate() function to continuously monitor and send sensor data.
Configuration:
SSID: Wi-Fi network name (set to "wokwi-GUEST" in the script).
PASSWORD: Wi-Fi password (empty in the script, can be set if needed).
DELAY: Time delay (in seconds) between sensor readings (set to 15 seconds).
Usage:
Replace the DATA_ENDPOINT variable with the actual URL of your API that will receive the sensor data.
Ensure that the device is correctly connected to the specified Wi-Fi network.
Run the script on a compatible microcontroller (e.g., ESP32 or ESP8266 with MicroPython).
Monitor the console for connection status, sensor readings, and any responses from the server.
Notes:
The script assumes the presence of a potentiometer connected to pin 27.
The urequests module is used to handle HTTP requests (make sure it is available on the device).