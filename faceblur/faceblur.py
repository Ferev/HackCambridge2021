from facenet_pytorch import MTCNN
import cv2
from PIL import ImageDraw, ImageFilter
import numpy as np
import torch
from matplotlib import pyplot as plt
from tqdm import tqdm
import time
import glob
from moviepy.editor import *
from PIL import Image as Img
import os


def process_video(input_name, output_name, temp_folder):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    mtcnn = MTCNN(margin=20, keep_all=True, post_process=False, device=device)

    v_cap = cv2.VideoCapture(input_name)
    v_len = int(v_cap.get(cv2.CAP_PROP_FRAME_COUNT))

    batch_size = 32
    frames = []
    boxes = []
    landmarks = []
    all_frames = []
    probs = []
    print('Detecting Faces')
    for _ in tqdm(range(v_len)):
        
        # Load frame
        success, frame = v_cap.read()
        if not success:
            continue
            
        # Add to batch, resizing for speed
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        all_frames.append(frame)
        frame = Img.fromarray(frame)
        frames.append(frame)
        
        
        # When batch is full, detect faces and reset batch list
        if len(frames) >= batch_size:
            batch_boxes, p, batch_landmarks = mtcnn.detect(frames, landmarks=True)
            boxes.extend(batch_boxes)
            probs.extend(p)
            frames = []

    fps = int(v_cap.get(cv2.CAP_PROP_FPS))

    frames_with_faces = []

    print('Applying Gaussian Blur')
    for ix in tqdm(range(len(all_frames))):
        frame_draw = all_frames[ix]
        frame_draw = Img.fromarray(frame_draw)
        draw = ImageDraw.Draw(frame_draw)
        try:
            for box in boxes[ix]:
                
                mask = Img.new('L', frame_draw.size)  # set color value 0 -> 255
                d = ImageDraw.Draw(mask)
                d.rectangle(box.tolist(), fill=255)
                blur = frame_draw.filter(ImageFilter.GaussianBlur(radius=15))
                frame_draw = Img.composite(blur, frame_draw, mask)
        except TypeError as e:
            pass
        except IndexError as e:
            pass
        frames_with_faces.append(frame_draw)
            
    print('Writing Video')
    TEMP_PATH = os.path.join(temp_folder, 'final_temp.mp4')
    writer = cv2.VideoWriter(TEMP_PATH, cv2.VideoWriter_fourcc(*'MJPG'), fps, (1280,720))
    for i in tqdm(range(len(frames_with_faces))):
        img = cv2.cvtColor(np.array(frames_with_faces[i]).astype('uint8'),cv2.COLOR_BGR2RGB)
        writer.write(img)
    writer.release()


    videoOUT = VideoFileClip(TEMP_PATH)
    audio = VideoFileClip(input_name).audio
    videoOUT = videoOUT.set_audio(audio)
    videoOUT.write_videofile(output_name, fps=fps, codec="libx264", audio_codec="aac")

    os.remove(TEMP_PATH)
    print('Done')


