
genres = ["blues" "classical" "country" "disco" "hiphop" "jazz" "metal" "pop" "reggae" "rock"];

filename = "C:/Users/Katon/Documents/finalproject/spectrograms/";

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
        
        spec_vec = zeros(129,1);
        spec_vec(1:128,1) = mean(spec,2);
        spec_vec(129,1) = i;
        
        spec_vecs(:,index) = spec_vec;
        index = index + 1;
    end    
end

writematrix(spec_vecs, 'C:/Users/Katon/Documents/finalproject/spectrograms/all_spects.csv');

