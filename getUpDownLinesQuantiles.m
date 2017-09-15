function [upLines, downLines, quantileLines] = getUpDownLinesQuantiles(readsDataFileName, diffDNaseDataFileName, cutoff, quantileNum, speciesCols, fdrCut)
% Gets the up-regulated sites, the down-regulated sites, and
% the lines with read counts between the bottom and top quantile using the
% output from a differential expression tool
% Input:
%   1.  readsDataFileName: Name of the file with the reads data; matrix in
%       file is n x m, where n is the number of DNase sites and m is the
%       number of samples
%   2.  diffDNaseDataFileName: Name of the file with the differential DNase
%       information from a differential expression too; file contains a
%       data structure with the following relevant fields:
%       1.  data: Matrix with the output values from the differential
%           expresison too; if the tool is edgeR, matrix is n x 3, where n
%           is the number of DNase sites and the 3rd column contains the
%           p-values
%   3.  cutoff: Number of reads for which, if a sample has more than that
%       number of reads for a DNase site, the site will be excluded from
%       analysis
%   4.  quantileNum: Number of quantiles that will be computed
%   5.  speciesCols: Cols in readsData with the species of interest
%   6.  fdrCut: Cutoff for the fdr (originally 0.01)
% Output:
%   1.  upLines: Indexes of lines that are up-regulated for the current
%       species
%   2.  downLines: Indexes of lines that are down-regulated for the current
%       species
%   3.  quantileLines: Indexes of lines that fit the common criteria for
%       the current species

readsData = importdata(readsDataFileName);
diffDNaseData = importdata(diffDNaseDataFileName);
[~, ~, idx] = fdr(diffDNaseData.data(:,3), fdrCut);
upLines = [];
downLines = [];
otherSpeciesCols = setdiff(1:1:size(readsData,2), speciesCols);
for i = 1:length(idx)
    % Iterate through the differentially expressed sites and find those
    % that are up and down-regulated
    if ~isempty(find(readsData(idx(i),:) > cutoff))
        % There is a very large number of reads for the current site in
        % some sample, so exclude it
        continue
    end
    if mean(readsData(idx(i),speciesCols)) > mean(readsData(idx(i),otherSpeciesCols))
        % The site is up-regulated in the current species
        upLines = vertcat(upLines, idx(i));
    elseif mean(readsData(idx(i),speciesCols)) < mean(readsData(idx(i),otherSpeciesCols))
        % The site is down-regulated in the current species
        downLines = vertcat(downLines, idx(i));
    end
end

quantileVals = zeros(quantileNum, length(speciesCols));
for i = 1:length(speciesCols)
    % Iterate through the columns with the species and get the appropriate
    % quantiles for each
    sampleUp = readsData(upLines, speciesCols(i));
    quantileVals(:,i) = quantile(sampleUp, quantileNum);
end
quantileLines = [];
for i = 1:size(readsData, 1)
    % Iterate through the sites and find those that fit the quantile
    % criteria
    criteriaFit = 1;
    for j = 1:length(speciesCols)
        % Iterate through the samples for the current species and check
        % whether each sample fits the quantile critera
        if (readsData(i, speciesCols(j)) < quantileVals(1,j)) || (readsData(i, speciesCols(j)) > quantileVals(quantileNum,j))
            % The quantile critera has not been met
            criteriaFit = 0;
            break
        end
    end
    if criteriaFit == 1
        % The quantile criteria has been met
        quantileLines = vertcat(quantileLines, i);
    end
end