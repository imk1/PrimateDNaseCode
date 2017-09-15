function commonLinesFilt = sampleCommonSitesLengths(dirLines, commonLines, allLengths)
% Gets the common sites that are drawn from approximately the same
% length distribution as the directional sites

% Input:
%   1.  dirLines: Line numbers of differential sites in the appropriate
%       direction, which is a l x 1 vector, where l is the number of
%       differential sites in the appropriate direction
%   2.  commonLines: Vector of indexes of unfiltered common sites
%   3.  allLengths: Vector of lengths of all DNase sites
% Output:
%   1.  commonLinesFilt: l x 1 vector, where l is the number of differential
%       sites in the appropriate direction, that contains the sampled
%       common sites

commonLinesFilt = zeros(length(dirLines), 1);
for i = 1:length(dirLines)
    % Iterate through the lines for differential sites and find the closest
    % line for common sites
    currentLength = allLengths(dirLines(i));
    closestLengthDiff = Inf;
    closestLengthLines = [];
    for j = 1:length(commonLines)
        % Iterate through the lines for common sites and find the one whose
        % median number of reads is closest to the median number of reads
        % for the differential site but has not yet been included
        if (~isempty(find(commonLinesFilt == commonLines(j)))) || (~isempty(find(dirLines == commonLines(j))))
            % The current site has already been included or is a differential site, so skip it
            continue
        end
        commonLength = allLengths(commonLines(j));
        lengthDiff = abs(currentLength - commonLength);
        if lengthDiff < closestLengthDiff
            % The median is closer to the current differential site median than
            % all previous medians
            closestLengthDiff = lengthDiff;
            closestLengthLines = [commonLines(j)];
        elseif lengthDiff == closestLengthDiff
            % The median is equally close to the current differential site
            % median as the previous closest median
            closestLengthLines = vertcat(closestLengthLines, commonLines(j));
        end
    end
    commonLinesFilt(i) = closestLengthLines(randi(length(closestLengthLines), 1));
end