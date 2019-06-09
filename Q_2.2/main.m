imagem = imread('C:\Users\igord\Documents\pds\2.2\alumgrns.bmp');

figure , imshow(imagem);

imagem_borrada = imgaussfilt(imagem,1.3);
BW = edge(imagem_borrada,'Sobel');

figure , imshow(BW)

contador_regioes = bwconncomp(BW); %Conta as diferentes regiões na imagem

numero_de_regioes  = contador_regioes.NumObjects;

s = regionprops(BW,'centroid');
numero_de_regioes_2 = size(s);