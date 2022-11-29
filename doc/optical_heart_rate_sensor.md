# Optical heart rate sensor

We use Elecrow's [Crowtail - Pulse Sensor 2.0][1] which is very sensitive to proper positioning, body movements and external conditions. For example, if the skin contact is loose, it easily picks up the 50 Hz flickering from the ambient room lighting.

It is recommended first to test and try which body location gives the best signal. Based on our experiments the front head, cheek and the chest gave best results. The signal from the finger tip or the wrist might be more difficult to measure.

There are some blog writings related to this topic using similar optical heart rate sensors and obstacles they have found. For example, [T.K.Hareendran wrote][3] his experiences with similar [optical sensor][4]. It might be a good practice to prepare some plastic or glue sealing around the sensor, as there is a small leakage current, if the sensor is placed directly to the skin.

In the [Hareendran's article][3] the electrical schematic of the circuit is also given. The same circuit can be also found from the [Crowtail - Pulse Sensor wikipage][2] (scroll to the bottom and see the Resources part). It contains the eagle file (zip) having both the electrical schematic and printed board circuit (PCB) layout. In order to read them you need a [PCB design tool][5] or you can use [an online viewer][6]. In [Techatronics' pages][7]  is another hack of the same circuit. Notice that the component values are different. [Ted Burke][11] has also built a optical heart rate sensor using basic electronic components. 

[There is also a circuit simulation model][8] developed with NI's Multisim available. By reading [the datasheet for the optical sensor][9] it was assumed that a photo current about 40 uA is generated in the sensor. That was modeled with an AC Current Source having offcet current of 40 uA and current peak of 1 uA. However, the model couldn't be simulated with the given 3.3 Mohm feedback resistor for the operational amplifier, but it was needed to reduce it to 1 Mohm. Overall, you get an idea that the circuit might be too sensitive and would benefit of tuning some of the component values.

More reading:

- [New High Performance Optical Sensor for Heart Rate Monitoring Ideal for Wearables][10] by Rohm Semiconductors.
- Ngueyn, W & Horjus, R. (2011). [Heart-Rate Monitoring Control System Using Photoplethysmography (PPG)][12]
- Analog Engineer's Circuit: Amplifiers (2018). [Photodiode amplifier circuit][13]. Texas Instruments.

[1]: https://www.elecrow.com/crowtail-pulse-sensor-p-1673.html (Crowtail - Pulse Sensor 2.0)

[2]: https://www.elecrow.com/wiki/index.php?title=Crowtail-_Pulse_Sensor (Crowtail - Pulse Sensor wikipage)

[3]: https://www.electroschematics.com/heart-rate-sensor/ (T.K. Hareendran, Pulse Rate Sensor)

[4]: https://cdn.shopify.com/s/files/1/0672/9409/files/PulseSensorAmpedGettingStartedGuide.pdf (Pulse Sensor Getting Started Guide)

[5]: https://www.autodesk.com/products/eagle/free-download (Eagle PCB design software for everyone, free download)

[6]: https://www.altium.com/viewer/ (Altium 365 Viewer - Electronic Designs Online)

[7]: https://techatronic.com/pulse-sensor-heart-beat-sensor/ (What is pulse sensor and its working - Heart Beat Sensor)

[8]: https://github.com/sakluk/first_year_hardware_project/tree/main/circuit (NI's Multisim circuit simulation model for Crowtail's Pulse Sensor)

[9]: https://www.elecrow.com/wiki/images/d/dc/APDS-9008-020-Avago.pdf (APDS-9008, Miniature Surface-Mount Ambient Light Photo Sensor - datasheet)

[10]: https://www.rohm.com/news-detail?news-title=new-high-performance-optical-sensor-for-heart-rate-monitoring&defaultGroupId=false (New High Performance Optical Sensor for Heart Rate Monitoring Ideal for Wearables)

[11]: https://batchloaf.wordpress.com/2019/04/04/e5-ppg-photoplethysmogram-amplifier-arduino-circuit/ (Burke, T. 2019. €5 PPG – photoplethysmogram amplifier)

[12]: https://core.ac.uk/download/pdf/19143551.pdf

[13]: https://www.ti.com/lit/an/sboa220a/sboa220a.pdf
