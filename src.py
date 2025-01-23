from time import sleep
from machine import ADC, Pin
import network
import urequests as requests

DELAY = 15
SSID = "wokwi-GUEST"
PASSWORD = ""
WLAN = network.WLAN(network.STA_IF)

pot = ADC(Pin(27))

def connectWifi():
  # WLAN aktivointi
  WLAN.active(True)
  # Yhdistäminen - SSOD - SALASANA
  WLAN.connect(SSID, PASSWORD)
  # Odotetaan yhteyden muodostumista
  while not WLAN.isconnected():
    print(".", end="")
    sleep(0.1)
  # Yhteysmuodostettu -> jatketaan operointia
  print(" Connected!")
  print(WLAN.ifconfig())
  return None

def sendData(value):
  try:
    # Sending data as query parameter
    DATA_ENDPOINT = "http://xxxxx/api/v1/update"
    response = requests.get(f"{DATA_ENDPOINT}?value={value}")
    print(response.json())
    response.close()
  except:
    print("could not send data...")
  return None

def operate():
  while True:
    print("\r          \r", end="")
    # unsigned 16-bit => 2^16 => 65536
    reading = pot.read_u16()
    print("Raw: {}".format(reading), end="")
    reading = reading * 100 / 65535
    print("Converted: {}".format(reading), end="\n")
    sendData(reading)
    sleep(DELAY)
  return None

def main():
  # 1. Initialize
  connectWifi()
  print("System started.")
  # 2. Operate
  operate()
  return None

main()