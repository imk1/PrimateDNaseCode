function [liblinearModelEvalArray, bestAccVal, bestAccValIndex, featuresExcluded] = evaluateLiblinearModelMultiParamsPlus(trainingLabels, trainingInstance, genesTrain, genesVal, numOneTrain, numOneVal)

% Uses Liblinear to train and evaluate multiple models
% NOTE HARD-CODED w0 and w1!!!!!!!!!

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
%   5.  numOneTrain: number of genes from class 1 in the training set
%   6.  numOneVal: number of genes from class 1 in the validation set
% Output:
%   1.  liblinearModelEvalArray: array containing structs with the 
%       following fields:
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
%   2.  bestAccVal: best validation accuracy
%   3.  bestAccValIndex: index of model with best validation accuracy
%   4.  featuresExcluded: list of indexes of features that were excluded
%       because their training set values were all 0s (causing NaNs during
%       standardization)


liblinearModelEvalArray = {};

bestAccVal = 0;
bestAccValIndex = 0;

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

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .001, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 1;
end
liblinearModelEvalArray{1} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .01, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 2;
end
liblinearModelEvalArray{2} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 3;
end
liblinearModelEvalArray{3} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 4;
end
liblinearModelEvalArray{4} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 10, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 5;
end
liblinearModelEvalArray{5} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 100, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 6;
end
liblinearModelEvalArray{6} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .001, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 7;
end
liblinearModelEvalArray{7} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .01, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 8;
end
liblinearModelEvalArray{8} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 9;
end
liblinearModelEvalArray{9} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 10;
end
liblinearModelEvalArray{10} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 10, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 11;
end
liblinearModelEvalArray{11} = liblinearModelEval;

model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 100, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = 12;
end
liblinearModelEvalArray{12} = liblinearModelEval;