function liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstances, genesTrain, genesVal, numOneTrain, numOneVal, model)

% Evalutes the model learned by Liblinear

% Input:
%   1.  trainingLabels: m x 1 vector, where m is the number of genes, with 
%       class labels for the entire data-set
%   2.  trainingInstances: m x n matrix, where m is the number of genes and
%       n is the number of features, with features for the entire data-set
%   3.  genesTrain: p x 1 vector, where p is the number of genes in the
%       training set, of the indexes of the genes in the training set,
%       where the indexes for class 1 come 1st and the indexes for class -1
%       come 2nd
%   4.  genesVal: q x 1 vector, where q is the number of genes in the
%       validation set, of the indexes of the genes in the validation set,
%       where the indexes for class 1 come 1st and the indexes for class -1
%       come 2nd
%   5.  numOneTrain: number of genes from class 1 in the training set
%   6.  numOneVal: number of genes from class 1 in the validation set
%   7.  model: struct with trained model from Liblinear
% Output:
%   1.  liblinearModelEval: struct with the following fields:
%       1.  model: struct with trained model from Liblinear
%       2.  predTrain: p x 1 vector, where p is the number of genes in the
%           training set, of predicted outputs for the training set
%       3.  accTrain: accuracy of predictions for the training set
%       4.  decisTrain: p x 2 vector, where p is the number of genes in the
%           training set, of the probability of each gene in the training
%           set belonging to each class
%       5.  accClassOneTrain: accuracy of predictions for class 1 in the
%           training set
%       6.  accClassNegOneTrain: accuracy of predictions for class -1 in
%           the training set
%       7.  predVal: q x 1 vector, where q is the number of genes in the
%           validation set, of predicted outputs for the validation set
%       8.  accVal: accuracy of predictions for the training set
%       9.  decisVal: q x 2 vector, where q is the number of genes in the
%           validation set, of the probability of each gene in the
%           validation set belonging to each class
%       10.  accClassOneVal: accuracy of predictions for class 1 in the
%           validation set
%       11.  accClassNegOneVal: accuracy of predictions for class -1 in
%           the validation set

liblinearModelEval = struct();
liblinearModelEval.model = model;

[liblinearModelEval.predTrain, liblinearModelEval.accTrain, liblinearModelEval.decisTrain] = predict(trainingLabels(genesTrain), sparse(trainingInstances(genesTrain,:)), model, '-b 1');
liblinearModelEval.accClassOneTrain = length(find(liblinearModelEval.predTrain(1:numOneTrain) == 1))/numOneTrain;
liblinearModelEval.accClassNegOneTrain = length(find(liblinearModelEval.predTrain(numOneTrain+1:length(liblinearModelEval.predTrain)) == -1))/(length(liblinearModelEval.predTrain) - numOneTrain);

[liblinearModelEval.predVal, liblinearModelEval.accVal, liblinearModelEval.decisVal] = predict(trainingLabels(genesVal), sparse(trainingInstances(genesVal,:)), model, '-b 1');
liblinearModelEval.accClassOneVal = length(find(liblinearModelEval.predVal(1:numOneVal) == 1))/numOneVal;
liblinearModelEval.accClassNegOneVal = length(find(liblinearModelEval.predVal(numOneVal+1:length(liblinearModelEval.predVal)) == -1))/(length(liblinearModelEval.predVal) - numOneVal);