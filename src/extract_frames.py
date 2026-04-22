import cv2
import os


def extract_frames(video_path, output_dir, step=5):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    i = 0
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if i % step == 0:
            cv2.imwrite(f"{output_dir}/{frame_id:05d}.jpg", frame)
            frame_id += 1

        i += 1

    cap.release()
    print(f"Extracted {frame_id} frames")



if __name__ == "__main__":
    extract_frames("test.MOV","data/frames")