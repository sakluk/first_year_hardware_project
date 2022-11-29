# Optical heart rate sensor

We use Elecrow's [Crowtail - Pulse Sensor 2.0][1] which is very sensitive to proper positioning, body movements and external conditions. For example, if the skin contact is loose, it easily picks up the 50 Hz flickering from the ambient room lighting.

It is recommended first to test and try which sensing location gives the best signal. Based on our experiments the front head, check and chest have given best results. The pulse signal from the finger tip or wrist might be difficult to measure.

There are some blog writings related to this topic using similar optical heart rate sensors and obstacles they have found. For example T.K.Hareendran [wrote](https://www.electroschematics.com/heart-rate-sensor/) his experiences with similar [PulseSensor Guide](https://cdn.shopify.com/s/files/1/0672/9409/files/PulseSensorAmpedGettingStartedGuide.pdf). It might be a good practice to prepare some sealing around the sensor, as you can sense a small leakage current in your skin, when you contact the bare sensor on your forehead skin.

In the Hareendran's article the electrical schematic of the circuit is also given. The same circuit can be also found from the [Crowtail - Pulse Sensor wikipage](https://www.elecrow.com/wiki/index.php?title=Crowtail-_Pulse_Sensor) (scroll to the bottom and see the Resources part). It contains the eagle file (zip) having both the electrical schematic and printed board circuit (PCB) layout. In order to read them you need a [PCB design tool](https://www.autodesk.com/products/eagle/free-download) or you can use [an online viewer](https://www.altium.com/viewer/).

In [Techatronics' pages](https://techatronic.com/pulse-sensor-heart-beat-sensor/) is another hack of the same circuit. Notice that the component values here are different. I also [played with the Crowtail's Pulse Sensor circuit on NI's Multisim](https://github.com/sakluk/first_year_hardware_project/tree/main/circuit). By reading [the datasheet for the optical sensor](https://www.elecrow.com/wiki/images/d/dc/APDS-9008-020-Avago.pdf) it was assumed that a photo current about 40 uA is generated in the sensor. That was modeled with an AC Current Source having offcet current of 40 uA and current peak of 1 uA. I couldn't run the simulation with the given 3.3 Mohm feedback resistor for the operational amplifier, but needed to reduce it to 1 Mohm. Overall I got a hunch that the circuit might be too sensitive and would benefit of tuning some of the component values.

References:

[1]: https://www.elecrow.com/crowtail-pulse-sensor-p-1673.html (Crowtail - Pulse Sensor 2.0()

[2]: Crowtail - Pulse Sensor wikipage(https://www.elecrow.com/wiki/index.php?title=Crowtail-_Pulse_Sensor)

[3]: [T.K. Hareendran, Pulse Rate Sensor](https://www.electroschematics.com/heart-rate-sensor/)

[4]: [Pulse Sensor Getting Started Guide](https://cdn.shopify.com/s/files/1/0672/9409/files/PulseSensorAmpedGettingStartedGuide.pdf)
- [5]: [Eagle PCB design software for everyone, free download](https://www.autodesk.com/products/eagle/free-download)
- [6]: [Altium 365 Viewer - Electronic Designs Online](https://www.altium.com/viewer/)
- [7]: [What is pulse sensor and its working - Heart Beat Sensor](https://techatronic.com/pulse-sensor-heart-beat-sensor/)
- [APDS-9008, Miniature Surface-Mount Ambient Light Photo Sensor - datasheet](https://www.elecrow.com/wiki/images/d/dc/APDS-9008-020-Avago.pdf).
- [8]: [NI's Multisim circuit simulation model for Crowtail's Pulse Sensor](https://github.com/sakluk/first_year_hardware_project/tree/main/circuit)
- [9]: [New High Performance Optical Sensor for Heart Rate Monitoring Ideal for Wearables](https://www.rohm.com/news-detail?news-title=new-high-performance-optical-sensor-for-heart-rate-monitoring&defaultGroupId=false). Rohm Semiconductors.
- [10]: Burke, T. (2019). [€5 PPG – photoplethysmogram amplifier]
- [11]: Ngueyn, W & Horjus, R. (2011). [Heart-Rate Monitoring Control System Using Photoplethysmography (PPG)](https://core.ac.uk/download/pdf/19143551.pdf)
