Wójcikowski and Pankiewicz (2020) wrote:
> The proposed solution of time-domain heart rate measurement algorithm (TDHR) consists of three main blocks: signal conditioning, peak detection, and heart-rate-measuring blocks. In this work, the modified Automatic Multiscale-based Peak Detection (AMPD) algorithm from [19], together with a bandpass filter/limiter, was used for finding the HR from a wrist-based PPG signal. All of the signal processing was done while taking into account the need for low power, low resources, and computing power utilization, necessary for a self-sufficient mobile sensor.

![Block diagram of PPG signal acquisition, preprocessing, and final HR estimation by TDHR algorithm.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7146569/bin/sensors-20-01783-g003.jpg)
<br>*Block diagram of PPG signal acquisition, preprocessing, and final HR estimation by TDHR algorithm.*

### 1st stage - Band-pass biquad with limiter
The raw signal is fed to the band-pass biquad section, with an internal limiter.
Can be implemented as:

```
y[i] = 1/a[0]*(b[0]*x[i] + b[1]*x[i-1] + b[2]*x[i-2] - a[1]*y[i-1] - a[2]*y[i-2])
y[i] = np.max(y[i], L_low)
y[i] = np.min[y[i], L_high)
```
It would be nice to use sosfilt, but there can be some overhead as the sosfilt doesn't have any internal limiters. 
The signal should be then processed sample-by-sample, like

```
from ulab import scipy
from ulab import numpy as np

y[i], zi = scipy.signal.sosfilt(sos, x[i], zi = zi)

y[i] = np.max(np.max(y[i], L_low), L_high)
```

### 2nd stage - Band-pass filter
A typical fourth-order band-bass filter built from two biquads was employed. The band-pass of both stages was set to 0.5 - 2.5 Hz.
This can be implemented using sosfilt:

```
from ulab import scipy

y, zi = scipy.signal.sosfilt(sos, x, zi = zi)
```



## References

- MATLAB Central (2018). Discussion on [Remove trend and detect peaks in a photoplethysmogram (PPG) signal](https://se.mathworks.com/matlabcentral/answers/380879-remove-trend-and-detect-peaks-in-a-photoplethysmogram-ppg-signal)
- Liang et al. (2018). [An optimal filter for short photoplethysmogram signals](https://www.nature.com/articles/sdata201876). Nature.
- Ismail et al. (2021). [Heart rate tracking in photoplethysmography signals affected by motion artifacts: a review](https://asp-eurasipjournals.springeropen.com/articles/10.1186/s13634-020-00714-2). EURASIP Journal on Advances in Signal Processing.
- Wójcikowski and Pankiewicz. (2020). [Photoplethysmographic Time-Domain Heart Rate Measurement Algorithm for Resource-Constrained Wearable Devices and its Implementation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7146569/). Sensors (Basel).
- [qppg.m from PhysioNet Cardiovasculat Signal Toolbox, File](https://moodle.frankfurt-university.de/mod/resource/view.php?id=473220)
