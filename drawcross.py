from PIL import Image, ImageDraw
img=Image.open('img0096.png')
draw=ImageDraw.Draw(img)
width,height=img.size
draw.line(((width/2-125,height/2-100),(width/2+125,height/2-100)),fill=255)
draw.line(((width/2-125,height/2+100),(width/2+125,height/2+100)),fill=255)
draw.line(((width/2-125,height/2-100),(width/2-125,height/2+100)),fill=255)
draw.line(((width/2+125,height/2-100),(width/2+125,height/2+100)),fill=255)
img.show()
img.save('crossline.png')
print 'width=%d, height=%d' %(width,height)
