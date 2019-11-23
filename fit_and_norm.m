% Min-Max fit all the rows, then normalize each song

total_features = readtable("C:/Users/Katon/Documents/finalproject/total_features.csv");
harmonic_features = readtable("C:/Users/Katon/Documents/finalproject/harmonic_features.csv");
percussive_features = readtable("C:/Users/Katon/Documents/finalproject/percussive_features.csv");

total_features = table2array(total_features);
harmonic_features = table2array(harmonic_features);
percussive_features = table2array(percussive_features);

new_total_features = zeros(27,1000);
new_percussive_features = zeros(27,1000);
new_harmonic_features = zeros(27,1000);

new_trow = zeros(1000,1);
new_hrow = zeros(1000,1);
new_prow = zeros(1000,1);

for i = 1:26
    for j = 1:1000
        t_val = total_features(i,j);
        h_val = harmonic_features(i,j);
        p_val = percussive_features(i,j);
        
        fit_t_val = (t_val - min(total_features(i,:))) / (max(total_features(i,:)) - min(total_features(i,:)));
        fit_h_val = (h_val - min(harmonic_features(i,:))) / (max(harmonic_features(i,:)) - min(harmonic_features(i,:)));
        fit_p_val = (p_val - min(percussive_features(i,:))) / (max(percussive_features(i,:)) - min(percussive_features(i,:)));
        
        new_trow(j) = fit_t_val;
        new_hrow(j) = fit_h_val;
        new_prow(j) = fit_p_val;
    end
    new_total_features(i,:) = new_trow;
    new_harmonic_features(i,:) = new_hrow;
    new_percussive_features(i,:) = new_prow;
end


new_total_features(27,:) = total_features(27,:);
new_harmonic_features(27,:) = harmonic_features(27,:);
new_percussive_features(27,:) = percussive_features(27,:);

% Normalize each column (song)
for i = 1:1000
    new_total_features(1:26,i) = new_total_features(1:26,i) / norm(new_total_features(1:26,i));
    new_harmonic_features(1:26,i) = new_harmonic_features(1:26,i) / norm(new_harmonic_features(1:26,i));
    new_percussive_features(1:26,i) = new_percussive_features(1:26,i) / norm(new_percussive_features(1:26,i));
end

writematrix(new_total_features, 'norm_total_features.csv');
writematrix(new_percussive_features, 'norm_perc_features.csv');
writematrix(new_harmonic_features, 'norm_harm_features.csv');



