import cv2
import os
from PIL import Image

os.chdir("C:\Users\abhis\Desktop\OpenCV\Classwork\4-29-26\images")
path = "C:\Users\abhis\Desktop\OpenCV\Classwork\4-29-26\images"

avg_height=0
avg_width=0
num_of_img=len(os.listdir('.'))

ResizedWidth = 400
ResizedHeight = 300
for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file)).convert('RGB')
        width,height = img.size
        print(width,height)
        imgResized = img.resize((ResizedWidth, ResizedHeight), Image.Resampling.LANCZOS)
        imgResized.save(file, 'JPEG', quality = 95)\

def VideoGenerator():
    videoName = "output.avi"
    os.chdir("C:\Users\abhis\Desktop\OpenCV\Classwork\4-29-26\images")
    images = []
    for img in os.listdir("."):
        if img.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            images.append(img)
    
    frame = cv2.imread(os.path.join(".",images[0]))
    height,width,layers = frame.shape
    video = cv2.VideoWriter(videoName,0,2,(width,height))
    for image in images:
        video.write(cv2.imread(os.path.join(".",image)))
    cv2.destroyAllWindows()
    video.release()

VideoGenerator()