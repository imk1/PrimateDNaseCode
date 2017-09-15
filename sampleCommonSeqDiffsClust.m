function commonClustersRowsFilt = sampleCommonSeqDiffsClust(dirClustersRows, commonClustersRows, dirData, commonData, dataCol)
% Gets the common sequence differences from sites that are drawn from
% approximately the same reads/length distribution as the sequence
% differences in the differential sites; sites are sampled from the same
% cluster as the differential sites

% Input:
%   1.  dirClustersRows: Line numbers of sequences differences in the differential sites in the appropriate
%       direction in each cluster, which is a n-entry cell array in which 
%       each entry is an l x 1 vector, where n is the number of clusters and l is the number of
%       sequence differences in differential sites in the appropriate
%       direction in the current cluster (l might vary from cluster to
%       cluster)
%   2.  commonClustersRows: Line numbers of sequences differences in the common sites in each cluster, which is a n-entry cell array in which 
%       each entry is an m x 1 vector, where n is the number of clusters and m is the number of
%       sequence differences in common sites in the current cluster (m might vary from cluster to
%       cluster)
%   3.  dirData: Data, such as reads and length, that will be used for
%       sampling and is taken from the differential sites with the sequence
%       differences
%   4.  commonData: Data, such as reads and length, that will be used for
%       sampling and is taken from the common sites with the sequence
%       differences
%   5.  dataCol: Column with the data that will be used for sampling
% Output:
%   1.  commonClustersRowsFilt: Line numbers of sampled sequences 
%       differences in the common sites in each cluster, which is a n-entry cell array in which 
%       each entry is an l x 1 vector, where n is the number of clusters and l is the number of
%       sequence differences in differential (and filtered common) sites in the appropriate
%       direction in the current cluster (l might vary from cluster to
%       cluster)

commonClustersRowsFilt = {};
for j = 1:length(dirClustersRows)
    % Iterate through the clusters and subsample for each cluster
    commonClustersRowsFilt{j} = zeros(length(dirClustersRows{j}), 1);
    for i = 1:length(dirClustersRows{j})
        % Iterate through the lines for sequence differences from differential sites and find the closest
        % line for common sites
        currentData = dirData(dirClustersRows{j}(i), dataCol);
        closestDataDiff = Inf;
        closestDataLines = [];
        for k = 1:length(commonClustersRows{j})
            % Iterate through the lines for sequences differences from the common sites and find the one whose
            % data is closest to the data for the sequence difference
            % from the differential site but has not yet been included
            if ~isempty(find(commonClustersRowsFilt{j} == commonClustersRows{j}(k)))
                % The current site has already been included or is a differential site, so skip it
                continue
            end
            currentDataCommon = commonData(commonClustersRows{j}(k), dataCol);
            dataDiff = abs(currentData - currentDataCommon);
            if dataDiff < closestDataDiff
                % The median is closer to the current differential site median than
                % all previous medians
                closestDataDiff = dataDiff;
                closestDataLines = [commonClustersRows{j}(k)];
            elseif dataDiff == closestDataDiff
                % The median is equally close to the current differential site
                % median as the previous closest median
                closestDataLines = vertcat(closestDataLines, commonClustersRows{j}(k));
            end
        end
        commonClustersRowsFilt{j}(i) = closestDataLines(randi(length(closestDataLines), 1));
    end
end