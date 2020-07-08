# import the pyplot and wavfile modules

import matplotlib.pyplot as plot

from scipy.io import wavfile

# Read the wav file (mono)

samplingFrequency, signalData = wavfile.read('../zero.wav')

# Plot the signal read from wav file

plot.subplot(411)

plot.title('Spectrogram of a wav zero')

plot.plot(signalData)

plot.xlabel('Sample')

plot.ylabel('Amplitude')

plot.subplot(412)

x = signalData[:, 0]

y = signalData[:, 1]

plot.specgram(y, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequenc')

plot.subplot(413)

plot.specgram(x, Fs=samplingFrequency)

plot.xlabel('Time')

plot.ylabel('Frequency')

samplingFrequency1, signalData1 = wavfile.read('../one.wav')

plot.subplot(414)

plot.plot(signalData1)

plot.xlabel('Sample')

plot.ylabel('Amplitude')


plot.show()