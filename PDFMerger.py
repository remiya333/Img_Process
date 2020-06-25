'''
This code merges the PDFs given in the Commandline as args
using the PyPDF2 and the PdfFileMerger class
'''
import PyPDF2
import sys
#inputs taken from the cmmandline starting from 1
inputs = sys.argv[1:]
# @function to mergePDFs
def MergePDF(PDFlist):
    merger = PyPDF2.PdfFileMerger()
    for pdf in PDFlist:
        print(pdf)
        merger.append(pdf)

    merger.write('MergerPDF.pdf')
#calling function
MergePDF(inputs)


