# Video Caption Editor

A Gradio-based web application for editing video captions individually or in bulk. Perfect for managing video datasets with subtitle files.

## Features

- **📁 Folder Scanning**: Point to any folder containing videos and their corresponding .txt caption files
- **🎥 Video Preview**: Auto-playing video previews in a responsive grid layout
- **✏️ Manual Editing**: Edit captions individually with instant save functionality
- **🚀 Bulk Operations**: Apply prefix, suffix, or replace operations to multiple captions at once
- **📄 Pagination**: 3x3 grid per page for optimal performance with large video sets
- **💾 Safe Backups**: Automatic .bak file creation before modifications
- **🔄 Selection Management**: Select all, clear selection, or toggle individual items

## Supported Video Formats

- .mp4
- .webm  
- .mkv
- .mov
- .avi

## Installation

1. Install Python 3.11 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and navigate to: `http://localhost:8816`

3. Enter the path to a folder containing videos and .txt files

4. Click "Load" to scan the folder

5. Use the interface to:
   - Navigate between pages
   - Select videos for bulk operations
   - Edit captions manually
   - Apply bulk prefix/suffix/replace operations

## File Structure

The application expects this file structure:
```
your_video_folder/
├── video1.mp4
├── video1.txt
├── video2.webm
├── video2.txt
└── ...
```

If a .txt file doesn't exist for a video, it will be created when you save a caption.

## Bulk Operations

### Prefix
Adds text to the beginning of selected captions.
- Option: "Only if it doesn't exist" prevents duplicates

### Suffix  
Adds text to the end of selected captions.
- Option: "Only if it doesn't exist" prevents duplicates

### Replace
Replaces all occurrences of target text with new text.
- Requires both "Text" and "Target" fields

## Safety Features

- **Automatic Backups**: Creates .bak files before first edit of the day
- **UTF-8 Encoding**: Ensures proper character handling
- **Error Handling**: Graceful handling of file permission issues
- **Validation**: Input validation for all operations

## Technical Details

- **Port**: 8816
- **Framework**: Gradio 4.0+
- **Encoding**: UTF-8 with Unix line endings
- **Grid Size**: 3x3 videos per page
- **Video Features**: Autoplay, loop, muted by default

## Troubleshooting

- **Videos not loading**: Check if your browser supports the video format
- **Permission errors**: Ensure write access to the target folder
- **Performance issues**: Use pagination - don't load too many videos at once
- **.mkv issues**: Some browsers have limited .mkv support, prefer .mp4/.webm

## License

Open source - feel free to modify and distribute.# captionOrganizer
