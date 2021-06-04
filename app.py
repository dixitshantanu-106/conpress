from flask import *
from image2pdf import converterI2P
from pdf2img import converterP2I

app = Flask(__name__)

@app.route('/')
def displayIndex():
    return render_template('index.html')

@app.route('/pdf')
def displayPdf():
    return render_template('pdf_jpeg.html')

@app.route('/jpeg')
def displayJpg():
    return render_template('jpeg_pdf.html')

outFile = ''
@app.route('/converted', methods=['GET', 'POST'])
def convert():
    global outFile
    inFile = request.files['ipfile']
    fname = inFile.filename
    print(fname)
    inFile.save(fname)
    if ('.pdf' in fname):
        outFile = converterP2I(fname)
    elif ('.jpg' in fname or '.jpeg' in fname):
        outFile = converterI2P(fname)
    return render_template('converted.html')

@app.route('/download')
def download():
    return send_file(outFile, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)