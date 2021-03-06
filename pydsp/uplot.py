from pylab import *

SAVE_DIR = './pydsp/static/media/plots/test.png'

def gp(res,num,c):
    t = arange(0,num,1)
    s = res
    xlabel('Time ')
    ylabel('Magnitude')
    if c=='l':
        title('Linear Convolution')
    elif c== 'c':
        title('Circular Convolution')
    elif c== 'if':
        title('Impulse Responce [First Order]')
    elif c== 'is':
        title('Impulse Responce [Second Order]')
    elif c== 'ac':
        n=int(num/2)
        t=arange(-n,n+1,1)
        xlabel('Amplitude')
        title('Autocorrelation')
    elif c== 'cc':
        n=int(num/2)
        t=arange(-n,n+1,1)
        xlabel('Amplitude')
        title('Crosscorrelation')
    elif c== 'nd':
        title('N Point DFT')
    stem(t, s)
    grid(True)
    savefig(SAVE_DIR)
    close()

def nyq_plot(fd,fs):
    fdr=fd
    fsr=fs
    tfinal=0.05
    nycrt='The Sampling frequency should be '+ str(2*fd)
    xlabel('Time (s)  ' + nycrt+'hz')
    ylabel('Amplitude (V)')
    title('Nyquist Plot')
    if fd >= 1000 and fd < 10000:
        fd=fd/10
        fs=fs/10
    if fd >= 10000 and fd < 100000:
        fd=fd/100
        fs=fs/100
    if fd >= 100000:
        fd=fd/1000
        fs=fs/1000
    if fd*2 in frange(fs-10,fs+10):
        title('Nyquist Plot')
    if fs < 2*fd:
        title('Under Sampling')
    if fs > 2.2*fd:
        title('Over Sampling')
    text(0.04, 0.75, 'Input Signal:'+str(int(fdr))+'hz')
    text(0.04, 0.65, 'Sampling Signal:'+str(int(fsr))+'hz')
    t1=arange(0,tfinal,1/fs)
    yn=cos(2*pi*fd*t1)
    t=arange(0,tfinal,0.00005)
    xn=cos(2*pi*fd*t)
    plot(t,xn,t1,yn,'r*-')
    grid(True)
    savefig(SAVE_DIR)
    close()



def twoplot(numr,numi,a,b,ch):
    if ch==0:
        suptitle('Inverse Discrete Fourier Transform', fontsize=14, fontweight='bold')
    else:
        suptitle('Discrete Fourier Transform', fontsize=14, fontweight='bold')
    tr = arange(0,numr,1)
    ti = arange(0,numi,1)
    subplots_adjust(hspace=.5)
    subplot(2,1,1)
    title('Real Values')
    grid(True)
    xlabel('Time ')
    ylabel('Magnitude')
    stem(tr,a)
    subplot(2,1,2)
    title('Imaginary Values')
    grid(True)
    xlabel('Time ')
    ylabel('Magnitude')
    stem(ti,b)
    savefig(SAVE_DIR)
    close()

def oneplot(res,num,ch):
    if ch==0:
        suptitle('Inverse Discrete Fourier Transform', fontsize=14, fontweight='bold')
    else:
        suptitle('Discrete Fourier Transform', fontsize=14, fontweight='bold')
    t=arange(0,num,1)
    stem(t,res)
    grid(True)
    xlabel('Time ')
    ylabel('Magnitude')
    savefig(SAVE_DIR)
    close()

