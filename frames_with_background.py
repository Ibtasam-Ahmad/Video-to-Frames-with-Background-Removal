import cv2
import os
from rembg import remove

def extract_frames(video_path, output_dir):
  """Extracts frames from a video, removes background using rembg, and saves as images.

  Args:
      video_path (str): Path to the video file.
      output_dir (str): Directory to save the extracted frames.
  """

  cap = cv2.VideoCapture(video_path)

  if not cap.isOpened():
    print("Error opening video file:", video_path)
    return

  print("Video opened successfully:", video_path)

  frame_count = 0
  while True:
    ret, frame = cap.read()

    if not ret:
      break

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
      os.makedirs(output_dir)

    # Remove background using rembg
    foreground = remove(frame)

    # Construct output path
    frame_path = os.path.join(output_dir, f"frame_{frame_count}.jpg")

    # Save the foreground image
    cv2.imwrite(frame_path, foreground)
    print(f"Frame {frame_count} with background removed saved to: {frame_path}")

    frame_count += 1

  cap.release()

def process_videos_in_folder(video_folder, output_folder):
  """Processes all videos in a specified folder and extracts frames with background removal using rembg.

  Args:
      video_folder (str): Path to the folder containing videos.
      output_folder (str): Directory to save the extracted frames.
  """

  for video_file in os.listdir(video_folder):
    if video_file.endswith(".mp4"):
      video_path = os.path.join(video_folder, video_file)
      # Create output directory based on video name (optional)
      output_dir = os.path.join(output_folder, video_file[:-4])
      extract_frames(video_path, output_dir)

# Replace with your video folder and output folder paths
video_folder = "./Input_Video_10100104"
output_folder = "./Output_video_10100104"

process_videos_in_folder(video_folder, output_folder)
