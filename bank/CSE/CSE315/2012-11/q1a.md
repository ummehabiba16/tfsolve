---
marks: 16
topics: [adc-registers, external-interrupts, timer-normal]
kind: diagram
source: {page: 91}
note: "Printed as 'greater that 60 C'."
---
Suppose you are to design an automated fire control system for a highly sophisticated room. To detect the fire, a pair of sensors (a smoke (S) and a temperature (T) sensor) is used. The sensors work in this way: the S sensor provides 0 volt if there is no smoke in the room. When it detects smoke, it jumps to 5 volt. The T sensor provides analog voltage in the range of 0 to 5 volt in proportional to the temperature between 0 C to 100 C. To be sure that the smoke is indeed caused by the fire you have to check the temperature of the room. So, the system continuously listens to the S sensor and collects the temperature from T sensor only after detection of smoke in the room. If the temperature of the room is found greater that 60 C after detection of smoke, the system will initiate an alarm to buzz. There will be a switch to stop the alarm. If the alarm is not switched off within one minute of the initiation of buzz, the system will send a start signal to the automated fire fighting system which is connected to the fire control system.

Now,

(i) Draw the block diagram with appropriate connections of the system along with pin names. You cannot use polling approach to collect data from any of the sensors.

(ii) Show the working procedure of your designed system using a flow chart. (8+8=16)
