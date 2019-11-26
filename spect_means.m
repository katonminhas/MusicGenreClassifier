% This file compresses the spectrograms to 25x22 and saves the mean values
% for each genre of spectrograms


genres = ["blues" "classical" "country" "disco" "hiphop" "jazz" "metal" "pop" "reggae" "rock"];


% Get means for each genre
blues_mean = zeros(128,216);
classical_mean = zeros(128,216);
country_mean = zeros(128,216);
disco_mean = zeros(128,216);
hiphop_mean = zeros(128,216);
jazz_mean = zeros(128,216);
metal_mean = zeros(128,216);
pop_mean = zeros(128,216);
reggae_mean = zeros(128,216);
rock_mean = zeros(128,216);


% Get spectrogram data
for i=1:length(genres)
    for j=0:99
        if j < 10
            name = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genres(i) + "/" + genres(i) + "0" + num2str(j) + ".csv";
        else
            name = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genres(i) + "/" + genres(i) + num2str(j) + ".csv";
        end
        
        curr_song = readtable(name);
        curr_song = table2array(curr_song);
        
        switch i
            case 1
                blues_mean = blues_mean + curr_song;
            case 2
                classical_mean = classical_mean + curr_song;
            case 3
                country_mean = country_mean + curr_song;
            case 4
                disco_mean = disco_mean + curr_song;
            case 5
                hiphop_mean = hiphop_mean + curr_song;
            case 6 
                jazz_mean = jazz_mean + curr_song;
            case 7
                metal_mean = metal_mean + curr_song;
            case 8
                pop_mean = pop_mean + curr_song;
            case 9
                reggae_mean = reggae_mean + curr_song;
            case 10
                rock_mean = rock_mean + curr_song;
        end
    end
      
end
    

blues_mean = blues_mean / 100;
classical_mean = classical_mean / 100;
country_mean = country_mean / 100;
disco_mean = disco_mean / 100;
hiphop_mean = hiphop_mean / 100;
jazz_mean = jazz_mean / 100;
metal_mean = metal_mean / 100;
pop_mean = pop_mean / 100;
reggae_mean = reggae_mean / 100;
rock_mean = rock_mean / 100;


% subplot(5,2,1), image(blues_mean), title("Blues")
% subplot(5,2,2), image(classical_mean), title("Classical")
% subplot(5,2,3), image(country_mean), title("Country")
% subplot(5,2,4), image(disco_mean), title("Disco")
% subplot(5,2,5), image(hiphop_mean), title("Hip-Hop")
% subplot(5,2,6), image(jazz_mean), title("Jazz")
% subplot(5,2,7), image(metal_mean), title("Metal")
% subplot(5,2,8), image(pop_mean), title("Pop")
% subplot(5,2,9), image(reggae_mean), title("Reggae")
% subplot(5,2,10), image(rock_mean), title("Rock")
% 
% writematrix(blues_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/blues_mean.csv');
% writematrix(classical_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/classical_mean.csv');
% writematrix(country_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/country_mean.csv');
% writematrix(disco_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/disco_mean.csv');
% writematrix(hiphop_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/hiphop_mean.csv');
% writematrix(jazz_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/jazz_mean.csv');
% writematrix(metal_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/metal_mean.csv');
% writematrix(pop_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/pop_mean.csv');
% writematrix(reggae_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/reggae_mean.csv');
% writematrix(rock_mean, 'C:/Users/Katon/Documents/finalproject/spectrograms/rock_mean.csv');

