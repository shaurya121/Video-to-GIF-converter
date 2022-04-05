
# Video to GIF converter

A video can be easily converted to a GIF (graphics interchange format) file using 'moviepy' package.


## Screenshots

![App Screenshot](https://raw.githubusercontent.com/shaurya121/Video-to-GIF-converter/main/example.gif)


## Installation

Install moviepy package using pip:

```python
  pip install moviepy
```
    
## Usage/Examples

Import a method called VideoFileClip:
```python
from moviepy.editor import VideoFileClip
```

Specify path of the video and GIF file:
```python
videoClip=VideoFileClip("input_file.mp4")
videoClip.write_gif("output_file.gif")
```

## Acknowledgements

 - [freecodecamp.org](https://freecodecamp.org)
