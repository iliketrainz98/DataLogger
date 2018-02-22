#Import Time for Delay functions .etc
import time
# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1015(address=0x48, busnum=1)

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

print("Beginning Test...");
while(True):
    print("1st A/D Convertor");
    value = adc.read_adc(3, gain=GAIN);
    print("Value:", value);
    voltage = (value * (0.125));
    print("Voltage:", voltage);
    temp = (voltage-500)/10;
    print("Temperature:", temp, "\n");
    time.sleep(2);
