# Project-2nd
Project-2nd with Sang

#Nối trở cho DS18B20: (Github:d3noob)
Connecting the DS18B20 to the Ethernet port would either not work or the effort to make it work (even if it was possible) would be excessive for someone starting out with a Raspberry Pi.

As you state, cut off the RJ45 and connect the sensor with the black wire to ground, the red wire to the 3V3 pin and the blue or yellow (some are blue and some are yellow) wire to the GPIO4 pin. A resistor between the value of 4.7k Ohms to 10k Ohms needs to be connected between the 3V3 and GPIO4 pins to act as a ‘pull-up’ resistor.
![pull-up resistor](https://i.stack.imgur.com/5EKzW.png)
