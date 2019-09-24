np = 1e6; nd = 2;
hp = gcp('nocreate');
if isempty(hp), hp = parpool(8); end
aA = randn(np,nd); aB = randn(np,nd);
dA = distributed(aA); dB = distributed(aB);
d = zeros(np,1);
tic;
dc = sqrt(sum((dA - dB).^2, 2));
c = gather(dc);
t = toc;
display(t);