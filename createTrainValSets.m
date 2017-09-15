function trainVal = createTrainValSets(geneListPos, geneListNeg, trainFrac)

% Creates training and validation sets from data
% Input:
%   1.  geneListPos: Indexes of genes in the positive set
%   2.  geneListNeg: Indexes of genes in the negative set
%   3.  trainFrac: Fraction of genes that will be used for training
% Output:
%   1.  trainVal: struct with the following fields:
%       1.  genesTrain: Indexes of genes in the training set; genes in the
%           positive set have their indexes before those of genes in the
%           negative set
%       2.  genesVal: Indexes of genes in the validation set; genes in the
%           negative set have their indexes before those of genes in the
%           positive set
%       3.  trainingLabels: Labels of genes for training followed by labels
%           of genes for validation, where 1 is for the positive set and -1
%           is for the negative set -- length is the length of genesTrain +
%           the length of genesVal

genesTrainPos = [];
numPos = length(geneListPos);
numTrainPos = round(trainFrac * numPos);
for i = 1:numTrainPos
    % Choose numTrainPos genes randomly from the positive set to include in
    % the training set
    randNum = randi(numPos, 1);
    while ~isempty(find(ismember(genesTrainPos, geneListPos(randNum))))
        % While the randomly selected gene has already been selected for
        % the training set, select a different gene
        randNum = randi(numPos, 1);
    end
    genesTrainPos = vertcat(genesTrainPos, geneListPos(randNum));
end

genesTrainNeg = [];
numNeg = length(geneListNeg);
numTrainNeg = round(trainFrac * numNeg);
for i = 1:round(numTrainNeg)
    % Choose numTrainNeg genes randomly from the negative set to include in
    % the training set
    randNum = randi(numNeg, 1);
    while ~isempty(find(ismember(genesTrainNeg, geneListNeg(randNum))))
        % While the randomly selected gene has already been selected for
        % the training set, select a different gene
        randNum = randi(numNeg, 1);
    end
    genesTrainNeg = vertcat(genesTrainNeg, geneListNeg(randNum));
end

genesValPos = setdiff(geneListPos, genesTrainPos);
genesValNeg = setdiff(geneListNeg, genesTrainNeg);
trainVal.genesTrain = vertcat(genesTrainPos(1:min(numTrainPos, numTrainNeg)), genesTrainNeg(1:min(numTrainPos, numTrainNeg)));
trainVal.genesVal = vertcat(genesValPos(1:min(numPos-numTrainPos, numNeg-numTrainNeg)), genesValNeg(1:min(numPos-numTrainPos, numNeg-numTrainNeg)));
trainingLabelsTrain = zeros(length(trainVal.genesTrain), 1);
trainingLabelsTrain(1:min(numTrainPos, numTrainNeg)) = 1;
trainingLabelsTrain(min(numTrainPos, numTrainNeg)+1:length(trainingLabelsTrain)) = -1;
trainingLabelsVal = zeros(length(trainVal.genesVal), 1);
trainingLabelsVal(1:min(numPos-numTrainPos, numNeg-numTrainNeg)) = 1;
trainingLabelsVal(min(numPos-numTrainPos, numNeg-numTrainNeg)+1:length(trainingLabelsVal)) = -1;
trainVal.trainingLabels = vertcat(trainingLabelsTrain, trainingLabelsVal);