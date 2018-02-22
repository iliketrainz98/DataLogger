#Import Time for Delay functions etc
import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc0 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)
adc1 = Adafruit_ADS1x15.ADS1115(address=0x49, busnum=1)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1
#Max Raw Data Value (15 bit)/Max voltage. Finds how many mV 1 bit represents. Note if gain is adjusted this will also need to be changed.
voltageConvert = 4096.0/32767.0;

#Chooses which A/D convertor is selected by default
currentAdc = adc0
currentAdcText = "1st A/D Convertor";
time.sleep(2);
("Beginning Test...");
while(True):
    print("Reading Begin | Currently Selected:",currentAdcText);
    print("-" *37,"\n");
    time.sleep(0.5);
    for currentPin in range(4):
        print("Current Pin: Pin A" + str(currentPin));
        #Prints raw data from the A/D convertion , straight from the I2C Bus
        raw = currentAdc.read_adc(currentPin, gain=GAIN, data_rate=860);
        print("Raw Data:", raw);
        #Converted to voltage using above conversion variable (voltageConvert)
        voltage = (raw * voltageConvert);
        print("Voltage:", round(voltage,2), "mV");
        #Convert and print to temperature and line break
        temp = (voltage-500)/10;
        print("Temperature:", round(temp,2), "°C\n");
        #split data to make easier to read and pause 2 seconds
        time.sleep(1);
    #Select next A/D Convertor
    if currentAdc == adc0:
        currentAdc = adc1;
        currentAdcText = "2nd A/D Convertor";
    else:
        currentAdc = adc0;
        currentAdcText = "1st A/D Convertor";

