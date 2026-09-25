import cv2
import os

def extract_frames(video_path, output_dir, sample_rate):
    os.makedirs(output_dir, exist_ok=True)

    if sample_rate <= 0:
        print("Error: sample_rate must be greater than 0")
        return

    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print(f"Error: could not open video {video_path}")
        return

    fps = video.get(cv2.CAP_PROP_FPS)
    if sample_rate > fps:
        print(f"Error: sample_rate cannot exceed video FPS ({fps})")
        video.release()
        return
    
    frame_interval = round(fps / sample_rate)
    frame_paths = []
    frame_count = 0

    while True:
        success, frame = video.read()
        if not success:
            break

        if frame_count % frame_interval == 0:
            frame_path = f"{output_dir}/frame_{frame_count}.jpg"
            cv2.imwrite(frame_path, frame)
            frame_paths.append(frame_path)

        frame_count += 1

    video.release()
    return frame_paths


frame_paths = extract_frames("data/test.mov", "data/frames", 1)
print(frame_paths)
