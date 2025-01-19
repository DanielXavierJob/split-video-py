# Split Video by Size

This Python script allows you to split a video into smaller segments based on a maximum file size (in megabytes). It uses the `moviepy` library to process the video and ensures each segment is approximately the desired size.

## Features
- Splits videos into multiple smaller segments based on the specified size.
- Automatically calculates the duration of each segment.
- Saves the segments with minimal quality loss using the H.264 codec.

## Requirements

Make sure you have the following installed:

1. Python 3.6 or higher.
2. Required Python libraries listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. `ffmpeg` installed and available in your system PATH.
   - **Linux:**
     ```bash
     sudo apt update && sudo apt install ffmpeg
     ```
   - **Windows:** Download and install from [FFmpeg Downloads](https://ffmpeg.org/download.html).

## Usage

1. Save the script to a file, e.g., `main.py`.
2. Run the script in your terminal or command prompt:
   ```bash
   python main.py
   ```
3. Provide the path to your video file when prompted.
4. Specify the maximum size (in megabytes) for each segment. If left blank, the default size is 10 MB.

## Code Details

### Main Function

```python
def split_video_by_size(input_file, max_size_mb):
```
- **`input_file`**: The path to the input video file.
- **`max_size_mb`**: Maximum size for each segment in megabytes.

### Workflow
1. **Input Handling**:
   - The script takes the video path and desired maximum size as input.
2. **Segment Duration Calculation**:
   - The script calculates the duration for each segment based on the estimated bitrate.
3. **Video Splitting**:
   - Divides the video into smaller segments using `moviepy`'s `subclip`.
4. **Export Settings**:
   - Each segment is exported with the H.264 codec (`libx264`) and AAC audio.

### Example Execution

**Input**:
```plaintext
Path do vídeo: example.mp4
Tamanho máximo em megabytes por segmento (padrão: 10 MB): 9.8
```

**Output**:
```plaintext
Bitrate estimado: 450.12 kbps
Duração estimada por segmento: 45.67 segundos
Segmento 1 salvo: output_segments/segment_1.mp4
Segmento 2 salvo: output_segments/segment_2.mp4
...
Divisão concluída!
```

## Notes
- The script saves all segments in an `output_segments` folder created in the current directory.
- The `ultrafast` preset ensures faster encoding at the cost of slightly larger file sizes.
- Ensure that your video file is not corrupted and is in a supported format.

## Limitations
- Encoding performance depends on your system's hardware (CPU, RAM, etc.).
- The estimated segment size may not be exact due to variations in video compression.

## License
This script is provided "as is" without warranty of any kind. Feel free to modify and use it for personal or educational purposes.
