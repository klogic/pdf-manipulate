from PyPDF2 import PdfFileWriter, PdfFileReader

page = PdfFileReader('original.pdf')
secondHalf = PdfFileReader('original.pdf')
output = PdfFileWriter()
numPages = page.getNumPages()
print ("document has %s pages." % numPages)

for i in range(numPages):
	page_data = page.getPage(i)
	pageWidthFrom = page_data.mediaBox.getUpperLeft_x()
	pageWidthTo =  page_data.mediaBox.getUpperRight_x()
	pageWidthHalf = pageWidthTo/2;
	print("the document half page is %s", pageWidthHalf);

    ### trim first half ###
	page_data.mediaBox.lowerLeft = (page_data.mediaBox.getLowerLeft_x(), page_data.mediaBox.getLowerLeft_y())
	page_data.mediaBox.upperRight = (pageWidthHalf, page_data.mediaBox.getUpperRight_y())

	page_data2 = secondHalf.getPage(i)
	pageWidthFrom = page_data2.mediaBox.getUpperLeft_x()
	pageWidthTo =  page_data2.mediaBox.getUpperRight_x()
	pageWidthHalf = pageWidthTo/2;
    ## trim second half ###
	page_data2.mediaBox.lowerLeft = (pageWidthHalf, page_data2.mediaBox.getLowerLeft_y())
	page_data2.mediaBox.upperRight = (page_data2.mediaBox.getUpperRight_x(), page_data2.mediaBox.getUpperRight_y())

    ## add to output pdf ###
	output.addPage(page_data)
	output.addPage(page_data2)

## write to pdf files ##
with open('output.pdf', 'wb') as fh:
       output.write(fh)
