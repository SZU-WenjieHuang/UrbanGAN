from PIL import Image

dx = 512
dy = 512

files = ["shanghai-input.jpg"]
#files = ["shanghai-output.jpg"]

for file in files:
    img =Image.open(file)
    x1 = 0
    y1 = 0
    while x1 <= img.size[0]-dx:
        while y1 <= img.size[1]-dy:
            name = './shanghai-input/' + file.split('/')[-1].split('.')[0] + '-' + str(x1) + '-' + str(y1) + '.jpg'
            #name = './shanghai-output/' + file.split('/')[-1].split('.')[0] + '-' + str(x1) + '-' + str(y1) + '.jpg'
            img2 = img.crop((x1, y1, x1+dx, y1+dy))
            img2.save(name)
            y1 = y1 + dy
            print(name)
        x1 = x1 + dx
        y1 = 0
