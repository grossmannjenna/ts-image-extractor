# ts-image-extractor
Overview
Timestamp.py is a Python script that extracts a single frame from a video file (video_path) at a specified timestamp (timestamp) and saves it as an image (output_image_path). It uses FFmpeg for extracting frames from the video.

Requirements
Python 3.x
FFmpeg executable (ffmpeg.exe) installed on your system. You can download FFmpeg from ffmpeg.org.

Note: replace the value for ffmpeg_path in extract_frame with the path to the executable in your system

Running the program

python script.py <video_path> <output_image_path> <timestamp>
- <video_path>: path to the video file from which the frame will come
- <output_image_path>: path to the desired location for the output image to be saved. Include the desired image filename with the desired image extension('.jpg', '.png')
- <timestamp>: Timestamp indicating the point in the video where the frame will be extracted. It should be in the format 'H:M:S:f' where f is fractional seconds.