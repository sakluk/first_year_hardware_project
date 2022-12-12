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

### Peak detection

> The detection of peaks is based on the AMPD algorithm.
> It needs the input signal to be linearly detrended, but the use of the input filter of band-pass characteristic with the limiter described in the previous section satisfies this requirement.
> The AMPD algorithm performs well for the filtered PPG signal, but it is computationally expensive, which can be unacceptable for wearable devices.
> The need to calculate a large matrix with real-valued elements, where moving windows are used, can be avoided due to the modifications of the algorithm proposed in further parts of this paper.
> ...
> From practical observation, it has been inferred that the signal is too noisy, and it is of no use for peak detection and heart rate calculation, when we have the following:
> $ \lambda > \lambda_max $
> The value of λmax = 17 was found empirically to be a good choice.
> To simplify the processing, the authors propose replacing real-valued elements of matrix Mr with the matrix Mr’ containing 1-bit binary values, m’k,i, as follows:

```
if (x[i-1] > x[i-k-1]) & (x[i-1] > x[i+k-1]):
  m[k, i] = 0
else:
  m[k, i] = 1

s[i] = np.sum(m[k, i], axis = 0)
```

## References

Primary

- Wójcikowski and Pankiewicz. (2020). [Photoplethysmographic Time-Domain Heart Rate Measurement Algorithm for Resource-Constrained Wearable Devices and its Implementation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7146569/). Sensors (Basel).
- Scholkmann et al. (2012). [An Efficient Algorithm for Automatic Peak Detection in Noisy Periodic and Quasi-Periodic Signals](An Efficient Algorithm for Automatic Peak Detection in Noisy Periodic and Quasi-Periodic Signals). algorithms.
- Cerina, L. (2017). [Automatic Multiscale-based Peak Detection (AMPD)](https://github.com/LucaCerina/ampdLib) for Python. GitHub.
- Szabolcs and László. (2021). [The minimal sampling frequency of the photoplethysmogram for accurate pulse rate variability parameters in healthy volunteers](https://www.sciencedirect.com/science/article/pii/S1746809421001865). Biomedical Signal Processing and Control, Volume 68.
Secondary

Secondary

- MATLAB Central (2018). Discussion on [Remove trend and detect peaks in a photoplethysmogram (PPG) signal](https://se.mathworks.com/matlabcentral/answers/380879-remove-trend-and-detect-peaks-in-a-photoplethysmogram-ppg-signal)
- Liang et al. (2018). [An optimal filter for short photoplethysmogram signals](https://www.nature.com/articles/sdata201876). Nature.
- Ismail et al. (2021). [Heart rate tracking in photoplethysmography signals affected by motion artifacts: a review](https://asp-eurasipjournals.springeropen.com/articles/10.1186/s13634-020-00714-2). EURASIP Journal on Advances in Signal Processing.

- [qppg.m from PhysioNet Cardiovasculat Signal Toolbox, File](https://moodle.frankfurt-university.de/mod/resource/view.php?id=473220)
