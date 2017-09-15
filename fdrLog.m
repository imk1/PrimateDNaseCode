% Compute p-values passing the fdr using the Benjamini-Hochberg procedure.
% Assumes that all p-values are actually -log10 p-values
%
% Inputs: 
% P - the vector of p-values
% Q - the FDR cutoff
% effective_N - a possible 'true' number of hypothesis we should normalize
% by (could be bigger then the number of p-values we input since we didn't
% compute all the p-vals
%
% The output is:
% num_rejected - the # of rejected hypothesis
% fdr_vec - a vector of the fdr cutoff values used by the procedure (why is this needed?)
% idx - the indices of the rejected hypothesis

% Code is taken from:
% http://www.broadinstitute.org/~orzuk/matlab/libs/stats/fdr/fdr.m and was
% written by O. Zuk
% Code is modified by: Irene Kaplow

function [num_rejected, fdr_vec, idx] = fdrLog(P, Q, effective_N, varargin)

if size(P,1)==1
    P=P';
end
Ng=length(P);
if(nargin == 2)
    effective_N = Ng;
end

[sorted_P, idx] = sort(P, 'descend');
slope = Q + log10(effective_N); %%% Ng; % can be bigger
fdr_num_vec = -log10(1:Ng)' + slope;
num_rejected = find(fdr_num_vec <= sorted_P, 1, 'last');
idx=idx(1:num_rejected);
fdr_vec = Q - log10([1:Ng]/Ng);
if(isempty(num_rejected))
    num_rejected = 0;
end