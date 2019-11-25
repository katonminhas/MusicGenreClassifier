% This file compresses the spectrograms to 25x22 and saves the mean values
% for each genre of spectrograms


genres = ["blues" "classical" "country" "disco" "hiphop" "jazz" "metal" "pop" "reggae" "rock"];

blues_songs = zeros(25,22,100);
classical_songs = zeros(25,22,100);
country_songs = zeros(25,22,100);
disco_songs = zeros(25,22,100);
hiphop_songs = zeros(25,22,100);
jazz_songs = zeros(25,22,100);
metal_songs = zeros(25,22,100);
pop_songs = zeros(25,22,100);
reggae_songs = zeros(25,22,100);
rock_songs = zeros(25,22,100);


row_indices = 1:5:125;
col_indices = 1:10:215;

% Get spectrogram data
for i=1:length(genres)
    % Do for first 9
    for j=1:9
        song_name = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genres(i) + "/" + genres(i) + "0" + num2str(j) + ".csv";
        curr_song = readtable(song_name);
        curr_song = table2array(curr_song);
        
        % Make 25x22
        curr_song = curr_song(row_indices,col_indices);
        
        switch genres(i)
            case "blues"
                blues_songs(:,:,j) = curr_song;
            case "classical"
                classical_songs(:,:,j) = curr_song;
            case "country"
                country_songs(:,:,j) = curr_song;
            case "disco"
                disco_songs(:,:,j) = curr_song;
            case "hiphop"
                hiphop_songs(:,:,j) = curr_song;
            case "jazz"
                jazz_songs(:,:,j) = curr_song;
            case "metal"
                metal_songs(:,:,j) = curr_song;
            case "pop"
                pop_songs(:,:,j) = curr_song;
            case "reggae"
                reggae_songs(:,:,j) = curr_song;
            case "rock"
                rock_songs(:,:,j) = curr_song;
         end
    end
    
    % Do for the rest
    for j = 10:99
        song_name = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genres(i) + "/" + genres(i) + num2str(j) + ".csv";
        curr_song = readtable(song_name);
        curr_song = table2array(curr_song);
        
        % Make 25x22
        curr_song = curr_song(row_indices,col_indices);
        
        switch genres(i)
            case "blues"
                blues_songs(:,:,j) = curr_song;
            case "classical"
                classical_songs(:,:,j) = curr_song;
            case "country"
                country_songs(:,:,j) = curr_song;
            case "disco"
                disco_songs(:,:,j) = curr_song;
            case "hiphop"
                hiphop_songs(:,:,j) = curr_song;
            case "jazz"
                jazz_songs(:,:,j) = curr_song;
            case "metal"
                metal_songs(:,:,j) = curr_song;
            case "pop"
                pop_songs(:,:,j) = curr_song;
            case "reggae"
                reggae_songs(:,:,j) = curr_song;
            case "rock"
                rock_songs(:,:,j) = curr_song;
         end
    end
end
    

% Get means for each genre
blues_mean = zeros(25,22);
classical_mean = zeros(25,22);
country_mean = zeros(25,22);
disco_mean = zeros(25,22);
hiphop_mean = zeros(25,22);
jazz_mean = zeros(25,22);
metal_mean = zeros(25,22);
pop_mean = zeros(25,22);
reggae_mean = zeros(25,22);
rock_mean = zeros(25,22);


for i=1:25
    for j=1:22
        blues_mean(i,j) = mean(blues_songs(i,j,:));
        classical_mean(i,j) = mean(classical_songs(i,j,:));
        country_mean(i,j) = mean(country_songs(i,j,:));
        disco_mean(i,j) = mean(disco_songs(i,j,:));
        hiphop_mean(i,j) = mean(hiphop_songs(i,j,:));
        jazz_mean(i,j) = mean(jazz_songs(i,j,:));
        metal_mean(i,j) = mean(metal_songs(i,j,:));
        pop_mean(i,j) = mean(pop_songs(i,j,:));
        reggae_mean(i,j) = mean(reggae_songs(i,j,:));
        rock_mean(i,j) = mean(rock_songs(i,j,:));
    end
end

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

