from pdf2image import convert_from_path
from zipfile import ZipFile
 
def converterP2I(filename):
    images = convert_from_path(filename)
    z = ZipFile('converted.zip', 'w')
    for i in range(len(images)):
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
        z.write('page'+ str(i) +'.jpg')
    else:
        z.close()
    return 'converted.zip'
    
