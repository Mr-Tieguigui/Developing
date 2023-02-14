[项目网址](https://pdfminersix.readthedocs.io/en/latest/)
# 特征
完全用Python编写。
解析、分析和转换 PDF 文档。
将内容提取为文本、图像、html 或hOCR。
PDF-1.7 规范支持。（嗯，差不多）。
支持中日韩语言和垂直书写脚本。
支持各种字体类型（Type1、TrueType、Type3 和 CID）。
支持提取图像（JPG，JBIG2，位图）。
支持各种压缩（ASCIIHexDecode，ASCII85Decode，LZWDecode，FlateDecode，RunLengthDecode， CCITTFaxDecode）
支持 RC4 和 AES 加密。
支持 AcroForm 交互式表单提取。
目录 提取。
标记内容提取。
自动布局分析。
# 安装
pip install pdfminer.six
pip install 'pdfminer.six[image]'

[测试文档](./test.ipynb)
[个人提取文档和图片](./test.py)
