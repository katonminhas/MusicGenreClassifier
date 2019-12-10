
rng("shuffle");


genres = ["blues" "classical" "country" "disco" "hiphop" "jazz" "metal" "pop" "reggae" "rock"];


spec_vecs = zeros(129,1000);
index = 1;
for i=1:10
    genre = genres(i);
    for j=1:100
        if j <= 10
            filename = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genre + "/" + genre + "0" + num2str(j-1) + ".csv";
        else
            filename = "C:/Users/Katon/Documents/finalproject/spectrograms/" + genre + "/" + genre + num2str(j-1) + ".csv";
        end
        
        spec = readtable(filename);
        spec = table2array(spec);
        
        % Take out 25% of the spectrogram at random
        for k=1:13824
            row_index = randi([1 128],1);
            col_index = randi([1 216],1);
            spec(row_index, col_index) = 0;
        end
       
        writematrix(spec, filename);
    end    
end


