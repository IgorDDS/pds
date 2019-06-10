imagem = imread('C:\Users\igord\Documents\pds\2.2\alumgrns.bmp');

figure , imshow(imagem);

% Borra a imagem para diminuir a quantidade de bordas falsas
imagem_borrada = imgaussfilt(imagem,1.3);

% Encontra as bordas na imagem borrada
BW = edge(imagem_borrada,'Sobel');

figure , imshow(BW)

% Conta o número de regiões
contador_regioes = bwconncomp(BW); %Conta as diferentes regi�es na imagem

numero_de_regioes  = contador_regioes.NumObjects;

% Essa função retorna o mesmo valor que a de cima.
% s = regionprops(BW,'centroid');
% numero_de_regioes_2 = size(s);