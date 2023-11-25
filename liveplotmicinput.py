import pyaudio
import numpy as np

import matplotlib.pyplot as plt
import time

RATE = 44100
CHUNK = int(RATE/20) # RATE / number of updates per second
dataarray=[]
def soundplot(stream):
    maxValue = 2 ** 16
    bars = 35
    t1=time.time()
    data = np.frombuffer(stream.read(CHUNK),dtype=np.int16)
    #dataarray.append(data[i])
    plt.cla()
    plt.plot(data,"k-")
    plt.title(i)
    plt.grid()
    plt.ylim(-20000,20000)
    #plt.savefig("03.png",dpi=50)
    plt.pause(0.00001)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs ( np.max ( dataL ) - np.min ( dataL ) ) / maxValue
    peakR = np.abs ( np.max ( dataR ) - np.min ( dataR ) ) / maxValue
    lString = "#" * int ( peakL * bars ) + "-" * int ( bars - peakL * bars )
    rString = "#" * int ( peakR * bars ) + "-" * int ( bars - peakR * bars )
    print("\rtook %.02f ms      "%((time.time()-t1)*1000)+ "L=[%s]\tR=[%s]" % (lString, rString) ,end='')

if __name__=="__main__":
    p=pyaudio.PyAudio()
    for i in range ( p.get_device_count ( ) ):
        print ( p.get_device_info_by_index ( i ) )
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                  frames_per_buffer=CHUNK)
    while True: #do this for 10 seconds
        soundplot(stream)
    stream.stop_stream()
    stream.close()
    p.terminate()
