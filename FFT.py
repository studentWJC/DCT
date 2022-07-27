import numpy as np
from scipy.io import wavfile

samplerate, data = wavfile.read("Output.wav")   #读取音频文件
time = np.arange(len(data))/samplerate
ft = np.fft.fft(data)
avg = np.max(abs(ft[1:]))*49/50   #具体数值可设置
ft[np.where(abs(ft) >= avg)] = 0 #将小于最大频率二十分之一的设置为0
data = np.fft.ifft(ft)
data = (data.real).astype('i2') # 格式转换
wavfile.write('Output_F.wav', samplerate, data) # 保存为过滤后的文件