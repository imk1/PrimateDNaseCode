function [clustersList, clustersFeatureMat] = makeClustersListAndFeatureMat(seqDiffsToClustersMat, featureMat, TFFeatureFileNameList)

% Makes a list of the indexes of each sequence difference in each cluster
% and a matrix with the TF-specific features for each cluster

% Input:
%   1.  seqDiffsToClustersMat: m x p matrix, where m is the number of
%       sequence differences and p is the number of TF clusters, that
%       contains indicators for whether each sequence difference is in each
%       TF cluster
%   2.  featureMat: m x n matrix, where m is the number of sequence
%       differences and n is the number of features, that contains the
%       non-TF-specific features for each cluster
%   3.  TFFeatureFileNameList: p x 1 cell array, where p is the number of 
%       TF clusters, that contains the names of the files with the
%       TF-specific features for each TF
% Output:
%   1.  clustersList: cell array of length p, where p is the number of
%       clusters, that contains the indexes of the sequence differences in
%       each cluster
%   2.  clustersFeatureMat: cell array of length p, where p is the number
%       of clusters in which each entry is a matrix of the all of the
%       features, including the TF-specific features, for each cluster

clustersList = {};
clustersFeatureMat = {};
TFFeatures = {};
for i = 1:length(TFFeatureFileNameList)
    % Iterate through the feature files and open them
    TFFeaturesLoc = importdata(TFFeatureFileNameList{i});
    TFFeatures{i} = TFFeaturesLoc.data(:, 2:size(TFFeaturesLoc.data, 2));
end

for i = 1:size(seqDiffsToClustersMat, 2)
    % Iterate through the TF clusters and get the sequence differences in
    % each cluster and the features for each cluster
    seqDiffsInCluster = find(seqDiffsToClustersMat(:,i) == 1);
    clustersList{i} = seqDiffsInCluster;
    clusterFeatures = featureMat(seqDiffsInCluster, :);
    TFFeaturesAll = clusterFeatures;
    for j = 1:length(TFFeatureFileNameList)
        % Iterate through the TF features and append each feature to the
        % feature matrix
        TFFeaturesCurrent = TFFeatures{j}(:,i);
        clusterTFFeatures = TFFeaturesCurrent(seqDiffsInCluster, :);
        TFFeaturesAll = horzcat(TFFeaturesAll, clusterTFFeatures);
    end
    clustersFeatureMat{i} = TFFeaturesAll;
end