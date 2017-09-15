function [liblinearModelEvalArray, bestAccVal, bestAccValIndex, featuresExcluded] = evaluateLiblinearModelMultiParamsFine(trainingLabels, trainingInstance, genesTrain, genesVal, numOneTrain, numOneVal)

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

modelCount = 0;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0001, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0002, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0003, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0004, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0005, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0006, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0007, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0008, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .0009, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .001, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .002, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .003, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .004, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .005, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .006, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .007, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .008, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .009, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .01, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .02, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .03, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .04, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .05, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .06, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .07, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .08, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .09, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .2, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .3, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .4, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .5, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .6, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .7, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .8, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, .9, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 2, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 3, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 4, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 5, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 6, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 7, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 8, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 9, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 10, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 20, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 30, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 40, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;


modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 50, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 60, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 70, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 80, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 90, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 100, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 200, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 300, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 400, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 500, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 600, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 700, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 800, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 900, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 0, -c, 1000, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0001, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0002, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0003, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0004, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0005, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0006, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0007, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0008, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .0009, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .001, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .002, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .003, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .004, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .005, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .006, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .007, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .008, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .009, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .01, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .02, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .03, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .04, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .05, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .06, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .07, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .08, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .09, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .2, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .3, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .4, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .5, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .6, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .7, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .8, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, .9, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 1, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 2, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 3, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 4, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 5, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 6, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 7, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 8, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 9, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 10, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 20, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 30, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 40, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;


modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 50, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 60, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 70, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 80, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 90, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 100, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 200, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 300, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 400, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 500, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 600, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 700, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 800, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 900, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;

modelCount = modelCount + 1;
model = train(trainingLabels(genesTrain), sparse(trainingInstanceStandardizedModified(genesTrain,:)), '-s, 6, -c, 1000, -B, 1');
liblinearModelEval = evaluateLiblinearModel(trainingLabels, trainingInstanceStandardizedModified, genesTrain, genesVal, numOneTrain, numOneVal, model);
if liblinearModelEval.accVal(1) > bestAccVal
    % The validation accuracy of the current model is higher than those of
    % previous models
    bestAccVal = liblinearModelEval.accVal(1);
    bestAccValIndex = modelCount;
end
liblinearModelEvalArray{modelCount} = liblinearModelEval;