from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *

def text_and_image(file):
    #打开一个pdf，使用二进制读取文件，读进来的是bytes类型
    pdf0= open(file, 'rb')
    #创建一个PDFParser对象
    parser=PDFParser(pdf0)
    #这里可以输入文档密码，官方是doc=PDFDocument(parser,password),我没有密码，就没输入
    doc=PDFDocument(parser) 
    parser.set_document(doc) 
    
    #这四行代码的目的就是初始化一个interpreter ，用于后面解析页面
    #pdf资源管理器
    resources = PDFResourceManager() 
    #参数分析器
    laparam=LAParams()
    #聚合器
    device=PDFPageAggregator(resources,laparams=laparam)
    #页面解释器
    interpreter = PDFPageInterpreter(resources,device) 
    
    #这里可以拆开获取pdf的每一页
    #PDFPage.create_pages(doc)的返回值是generator类型，可以用for来遍历
    pages=[]
    for page in PDFPage.create_pages(doc):
        pages.append(page)
    #准备把page解析出来的东西存一下，方便后面用
    texts=[]
    images=[]
    
    for page in pages:
        interpreter.process_page(page)#解析page
        layout = device.get_result() #获得layout，layout可遍历
    
        #遍历layout，layout里面就是要拆的东西了
        for out in layout:
            if isinstance(out,LTTextBox):
                texts.append(out)
            if isinstance(out,LTImage):
                images.append(out)
            #当是figure类型时，需要取出它里面的东西来。figure可遍历，所以for循环取。
            #如果figure里面还是figure，就接着遍历(虽然我没见过多层figure的情况)
            if isinstance(out,LTFigure):
                figurestack=[out]
                while figurestack:
                    figure=figurestack.pop()
                    for f in figure:
                        if isinstance(f,LTTextBox):
                            texts.append(f)
                        if isinstance(f,LTImage):
                            images.append(f)
                        if isinstance(f,LTFigure):
                            figurestack.append(f)

    #文本：
    f1 = open('./text.txt','w',encoding='utf-8')
    for text in texts:
        print(text.get_text())
        f1.writelines(text.get_text())
    f1.close()

    #图片及图片另存：
    i=0 #文件名编号
    for image in images:
        with open('./figure/pic_{}.jpg'.format(i),'wb') as f:
            f.write(image.stream.get_data())
            i = i + 1

if __name__ == "__main__":
    file = './example.pdf'
    text_and_image(file)
