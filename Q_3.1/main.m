video = VideoReader('video1.avi');
F = video.NumberOfFrames;

frame_atual_rgb = read(video,1);
frame_atual_gray = rgb2gray(frame_atual_rgb)

[m,n] = size(frame_atual_gray);
video_final = zeros(m,n,F);
threshold = 50;

for f = 2:F  %Pra cada frame
proximo_frame_rgb = read(video,f);
proximo_frame_gray = rgb2gray(proximo_frame_rgb)
    for i = 1:m
        for j = 1:n
            if abs(frame_atual_gray(i,j) - proximo_frame_gray(i,j)) > threshold
                video_final(i,j,f) = frame_atual_gray(i,j);
            else
                video_final(i,j,f) = 0;
            end
        end
    end
frame_atual_gray = proximo_frame_gray;
end

%tendo problemas com o formato do video atual que � double, tentar passar
%pra uint8

video_final_uint8 = im2uint8(video_final)
writer = VideoWriter('C:\Users\igord\Documents\pds\3.1\video_final_3.1.avi', 'Uncompressed AVI');
writer.FrameRate = video.FrameRate;
open(writer);

for f = 1:F  %Pra cada frame
   writeVideo(writer,video_final_uint8(:,:,f));
end

close(writer)