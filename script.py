import subprocess
import sys
from datetime import datetime

def format_timestamp(timestamp):
    """
    Converts a timestamp into decimal seconds, manual, and detailed format
    and returns all three.

    Parameters
    ----------
    timestamp : H:M:S.f format

    Returns
    -------
    decimal_seconds
        timestamp formatted like "27.089"
    manual_format
        timestamp formatted like "00:00:27"
    detailed_format
        timestamp formatted like "00:00:27.089"
    """

    # convert timestamp to a datetime object
    time_obj = datetime.strptime(timestamp, "%H:%M:%S.%f")

    # format as decimal seconds
    decimal_seconds = f"{time_obj.hour * 3600 + time_obj.minute * 60 \
                         + time_obj.second + time_obj.microsecond / 1e6:.3f}"

    # format as manual format
    manual_format = time_obj.strftime("%H:%M:%S")

    # format as detailed format
    detailed_format = time_obj.strftime("%H:%M:%S.%f")[:-3]
    
    return decimal_seconds, manual_format, detailed_format

def extract_frame(video_path, timestamp, output_image_path):
    """
    Extracts a picture from the video at the given timestamp and saves it in
    the output path

    Parameters
    ----------
    video_path : str
        the file location of the video
    timestamp : datetime obj
        chosen time to extract the image
    output_image_path : str
        file path to place extracted image
    
    Returns
    -------
    none
    """

    # path to ffmpeg executable(change depending on your computer's installation)
    ffmpeg_path = r'C:\ffmpeg\ffmpeg.exe'

    # extract frame at given timestamp using ffmpeg
    command = [
        ffmpeg_path,
        '-ss', timestamp,
        '-i', video_path,
        '-frames:v','1',
        '-q:v', '2',
        output_image_path
    ]
    subprocess.run(command,check=True)

def main():
    # ensure the number of arguments is correct
    if len(sys.argv) != 4:
        print("Usage: timestamp.py <video_path> <output_image_path> <timestamp>")
        sys.exit(1)
    
    # declare variables
    video_path = sys.argv[1]
    output_image_path = sys.argv[2]
    timestamp = sys.argv[3]

    # get all timestamp formats
    decimal_seconds, manual_format, detailed_format = format_timestamp(timestamp)

    # get frame at the timestamp and store in specified location
    extract_frame(video_path, detailed_format, output_image_path)

if __name__=="__main__":
    main()