function commonLinesFilt = sampleCommonSites(readsDataFileName, dirLines, commonLines, speciesCols)
% Gets the common sites that are drawn from approximately the same
% reads distribution as the directional sites

% Input:
%   1.  readsDataFileName: Name of the file with the reads data; matrix in
%       file is n x m, where n is the number of DNase sites and m is the
%       number of samples
%   2.  dirLines: Line numbers of differential sites in the appropriate
%       direction, which is an l x 1 vector, where l is the number of
%       differential sites in the appropriate direction
%   3.  commonLines: Vector of indexes of unfiltered common sites
%   4.  speciesCols: Cols in readsData with the species of interest
% Output:
%   1.  commonLinesFilt: l x 1 vector, where l is the number of differential
%       sites in the appropriate direction, that contains the sampled
%       common sites

readsData = importdata(readsDataFileName);
readsDataMedians = median(readsData(:,speciesCols), 2);
commonLinesFilt = zeros(length(dirLines), 1);
for i = 1:length(dirLines)
    % Iterate through the lines for differential sites and find the closest
    % line for common sites
    currentMedian = readsDataMedians(dirLines(i));
    closestMedianDiff = Inf;
    closestMedianLines = [];
    for j = 1:length(commonLines)
        % Iterate through the lines for common sites and find the one whose
        % median number of reads is closest to the median number of reads
        % for the differential site but has not yet been included
        if (~isempty(find(commonLinesFilt == commonLines(j)))) || (~isempty(find(dirLines == commonLines(j))))
            % The current site has already been included or is a differential site, so skip it
            continue
        end
        commonMedian = readsDataMedians(commonLines(j));
        medianDiff = abs(currentMedian - commonMedian);
        if medianDiff < closestMedianDiff
            % The median is closer to the current differential site median than
            % all previous medians
            closestMedianDiff = medianDiff;
            closestMedianLines = [commonLines(j)];
        elseif medianDiff == closestMedianDiff
            % The median is equally close to the current differential site
            % median as the previous closest median
            closestMedianLines = vertcat(closestMedianLines, commonLines(j));
        end
    end
    commonLinesFilt(i) = closestMedianLines(randi(length(closestMedianLines), 1));
end