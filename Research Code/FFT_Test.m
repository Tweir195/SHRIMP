filename = 'FFT_Test_2.wav'; % Replace with the file you want to analyze
[data, sample_rate] = audioread(filename); % Read the file into a matrix of amplitudes and a sample_rate
data_sample = data(12.12*sample_rate:12.17*sample_rate,1); % Section the data from 12.12 seconds to 12.17 seconds
% Left audio channel only
spec = fft(data_sample); % Take FFT
L = length(data_sample); % I copied and pasted this code from the MatLab documentation 
% But this graphs the single-sided spectrum
freq_dis = sample_rate*(0:(L/2))/L;
P2 = abs(spec/L);
P1 = P2(1:L/2+1);
plot(freq_dis, P1);
% The higher frequencies are technically there but not useful
% so we limit it
xlim([0, 2*10^3])

figure()
% s = spectrogram(data_sample); I don't know what the difference between
% this and the next line of code is, so its commented out
spectrogram(data_sample, 1000, [],[], sample_rate, 'yaxis'); % Plot the spectrogram
% The parameters are in order: the data samples, how wide each block on the
% spectrogram should be, some parameters I'm not sure of, and the sample
% rate