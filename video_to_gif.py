from moviepy.editor import VideoFileClip

videoClip=VideoFileClip("/home/shaurya/Desktop/s1/Hello - Cutest 3 Second Video Ever!.3gpp")
videoClip.write_gif("/home/shaurya/Desktop/s1/hello.gif")
print("Conversion Finished...")
