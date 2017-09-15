function [mtLogisticRModelEvalArray, accTrainList, accValList, bestAccVal, bestAccValIndex, featuresExcluded] = evaluatemtLogisticRModelMultiParams(trainingLabels, trainingInstance, genesTrain, genesVal, clustersVec)

% Uses Liblinear to train and evaluate multiple models

% Input:
%   1.  trainingLabels: m x 1 vector, where m is the number of genes, with 
%       class labels for the entire data-set
%   2.  trainingInstances: m x n matrix, where m is the number 
%       of genes and n is the number of features, where no features have
%       been standardized
%   3.  genesTrain: p x 1 vector, where p is the number of genes in the
%       training set, of the indexes of the genes in the training set,
%       where the indexes for class 1 come 1st and the indexes for class -1
%       come 2nd
%   4.  genesVal: q x 1 vector, where q is the number of genes in the
%       validation set, of the indexes of the genes in the validation set,
%       where the indexes for class 1 come 1st and the indexes for class -1
%       come 2nd
%   5.  clustersVec: m x 1 vector, where m is the number of genes/sequence
%       differences, that contains the index of the cluster for each
%       gene/sequence difference
% Output:
%   1.  mtLogisticRModelEvalArray: array containing the models for each
%       cluster and each regularization parameter, where each model is a k
%       x n matrix of weights, where k is the number of clusters and n is
%       the number of features
%   2.  accTrainList: l x k matrix, where l is the number of regularization
%       parameters and k is the number of clusters, that contains the
%       training accuracy for each regularization parameter in each cluster
%   3.  accValList: l x k matrix, where l is the number of regularization
%       parameters and k is the number of clusters, that contains the
%       validation accuracy for each regularization parameter in each 
%       cluster
%   4.  bestAccVal: best validation accuracy for each cluster
%   5.  bestAccValIndex: index of model with best validation accuracy for
%       each cluster
%   6.  featuresExcluded: list of indexes of features that were excluded
%       because their training set values were all 0s (causing NaNs during
%       standardization)

numClusters = max(clustersVec); % TRUE NUMBER OF CLUSTERS IS numClusters + 1 BECAUSE CLUSTERS ARE 0-INDEXED

mtLogisticRModelEvalArray = {};

accTrainList = zeros(8, numClusters + 1);
accValList = zeros(8, numClusters + 1);

trainingInstanceStandardized = zeros(size(trainingInstance));
for i = 1:size(trainingInstanceStandardized, 2)
   % Iterate through the features and standardize each feature using the
   % training set
   trainingInstanceStandardized(:,i) = (trainingInstance(:,i) - mean(trainingInstance(genesTrain,i)))/std(trainingInstance(genesTrain,i), 1);
end

featuresExcluded = [];
trainingInstanceStandardizedModified = [];
for i = 1:size(trainingInstanceStandardized, 2)
    % Iterate through the features and find those that are not NaNs
    if isempty(find(isnan(trainingInstanceStandardized(:,i))))
        % The current feature is not all 0s in the training set, so include
        % it
        trainingInstanceStandardizedModified = horzcat(trainingInstanceStandardizedModified, trainingInstanceStandardized(:,i));
    else
        featuresExcluded = vertcat(featuresExcluded, i);
    end
end

labelsClustOrderTrain = [];
for i = 0:numClusters
    % Iterate through the clusters and add the training labels for each
    % cluster to the vector of training labels
    labelsClustOrderTrain = vertcat(labelsClustOrderTrain, trainingLabels(intersect(find(clustersVec == i), genesTrain)));
end

instanceStandardizedTrain = [];
for i = 0:numClusters
    % Iterate through the clusters and add the standardized data for each
    % cluster to the matrix of training data
    instanceStandardizedTrain = vertcat(instanceStandardizedTrain, trainingInstanceStandardizedModified(intersect(find(clustersVec == i), genesTrain), :));
end

optsTrain = struct();
optsTrain.rFlag = 0;
optsTrain.nFlag = 0;
indTrain = [0];
for i = 0:numClusters
    % Iterate through the clusters and add the last index of each cluster
    % in the data to the index vector
    lastInd = indTrain(length(indTrain));
    indTrain = vertcat(indTrain, lastInd + length(intersect(find(clustersVec == i), genesTrain)));
end
optsTrain.ind = indTrain;

regParamList = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000];
numRegParams = 1;
model = struct();
model.Paremeters = 0;
model.nr_class = 2;
model.nr_feature = size(trainingInstanceStandardizedModified, 2);
model.bias = 1;
model.Label = [1, -1];
for i = 1:length(regParamList);
    % Iterate through regularization parameters and try the classifier on
    % each
    regParam = regParamList(i);
    [x, c, funVal, ValueL] = mtLogisticR(instanceStandardizedTrain, labelsClustOrderTrain, regParam, optsTrain);
    mtLogisticRModelEvalArray{numRegParams} = x;
    for i = 1:numClusters + 1
        % Iterate through the clusters and find the accuracy for each
        model.w = vertcat(x(:,i), c(i))';
        [predTrain, accTrain, decisTrain] = predict(trainingLabels(intersect(find(clustersVec == i - 1), genesTrain)), sparse(trainingInstanceStandardizedModified(intersect(find(clustersVec == i - 1), genesTrain), :)), model, '-b 1');
        [predVal, accVal, decisVal] = predict(trainingLabels(intersect(find(clustersVec == i - 1), genesVal)), sparse(trainingInstanceStandardizedModified(intersect(find(clustersVec == i - 1), genesVal), :)), model, '-b 1');
        accTrainList(numRegParams, i) = accTrain(1);
        accValList(numRegParams, i) = accVal(1);
    end
    regParam = regParam * 10;
    numRegParams = numRegParams + 1;
end

[bestAccVal, bestAccValIndex] = max(accValList, [], 1);
