% O tipo mais comum de daltonismo é protonopia, essas pessoas tem problemas
% com verde e vermelho mas ainda tem sensitividade para o amarelo e azul.
% Portanto eu tenho duas abordagens. Primeira, simplesmente percorrer a
% matriz e jogar tons de vermelho pro amarelo e tons de verde pro azul.
% Segunda, usar o filtro fornecido nesse link https://github.com/PlanetCentauri/ColorblindFilter/blob/master/Code

%Carregando imagem
imagem = imread('C:\Users\igord\Documents\pds\2.3\dalton.bmp');
figure, imshow (imagem);

%Agora posso mexer no tom (hue) da imagem diretamente
imagem_hsv = rgb2hsv(imagem);

%https://www.researchgate.net/figure/HSV-color-chart-used-to-convert-the-positions-into-colors_fig3_224246861
%http://colorizer.org/


F=fft2(imagem);
vermelho = zeros(128,128,3);
vermelho(:,:,1) = 255;
verde = zeros(128,128,3);
verde(:,1,:) = 255;
azul = zeros(128,128,3);
azul(1,:,:) = 255;
vermelho_hsv = rgb2hsv(vermelho);
verde_hsv = rgb2hsv(verde);
azul_hsv = rgb2hsv(azul);
% preciso girar as cores em 45 graus quando
% estiverem no range do vermelho ou do verde
% http://www.tech-faq.com/hsv.html

%0 = vermelho
%0.33 = verde
%0.66 = azul

[X , Y , lixo] = size(imagem_hsv);
for x = 1:X
    for y = 1:Y
%         if imagem_hsv(x , y , 1) > 0.9 && imagem_hsv(x , y , 2) < 30 && imagem_hsv(x , y , 3) > 230
        if imagem_hsv(x , y , 1) < 0.15
            imagem_hsv(x , y , 1) = imagem_hsv(x , y , 1)+ 0.6;
%             imagem_hsv(x , y , 3) = imagem_hsv(x , y , 3) - 0.3;
%         elseif imagem_hsv(x , y , 1) > 0.9
%             imagem_hsv(x , y , 1) = imagem_hsv(x , y , 1)-0.1;
%             imagem_hsv(x , y , 2) = imagem_hsv(x , y , 2) + 0.3; % dica de um amigo
        elseif imagem_hsv(x , y , 1) <0.45
            imagem_hsv(x , y , 1) = imagem_hsv(x , y , 1)-0.3;
            imagem_hsv(x , y , 3) = imagem_hsv(x , y , 3) - 0.3;
%         elseif imagem_hsv(x , y , 1) <0.40
%             imagem_hsv(x , y , 2) = min(imagem_hsv(x , y , 2) + 0.3 , 1);
%         elseif imagem_hsv(x , y , 1) > 150*um_grau && imagem_hsv(x , y , 1) <= 180*um_grau
%             imagem_hsv(x , y , 1) = imagem_hsv(x , y , 1)+120*um_grau;
%             imagem_hsv(x , y , 2) = imagem_hsv(x , y , 2) + 0.3;
        end
    end
end

imagem_final = hsv2rgb(imagem_hsv);
figure, imshow (imagem_final);

imwrite(imagem_final,'saida.bmp')
