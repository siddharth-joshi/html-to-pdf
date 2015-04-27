import time 
from pyPdf import PdfFileWriter, PdfFileReader
import StringIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from xhtml2pdf import pisa
import sys
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
#from PyQt4.QtWebKit import *
import os
import sys
import pdfkit


url = 'http://www.google.com'
temp_pdf = './temp/temp_pdf.pdf'
final_file = 'out.pdf'


pdfkit.from_url(url,final_file)

#app = QApplication(sys.argv)
#web = QWebView()
#
#web.load(QUrl(url))
#printer = QPrinter()
#
#printer.setPageSize(QPrinter.A4)
#printer.setOrientation(QPrinter.Landscape)
#printer.setOutputFormat(QPrinter.PdfFormat)
#
#printer.setOutputFileName(temp_pdf)
#
#def convertIt():
#	web.print_(printer)
#	QApplication.exit()
#
#QObject.connect(web,SIGNAL("loadFinished(bool)"), convertIt)
#
#app.exec_()
#sys.exit
