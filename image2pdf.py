import img2pdf

def converterI2P(filename):
    pdfname = filename.split('.')[0]+'.pdf'
    with open(pdfname,'wb') as f:
        f.write(img2pdf.convert(filename))
    return pdfname
