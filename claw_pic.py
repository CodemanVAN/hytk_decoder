import requests
import re
import os
import decode
import sys
from PyQt5.QtWidgets import QPushButton,QWidget, QApplication,QMessageBox
import donate,main_wd
import time
reg=re.compile('<a rel="noreferrer" href="(.*?)" title="(.*?)" target="_blank" class="j_th_tit ">')
reg2=re.compile('<img class="BDE_Image" src="(.*?)"')
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'
}
def start():
    QMessageBox.about(main_wd.widget,'提醒:',"正在开始处理，可能会卡顿，受网速和电脑性能影响，请耐心等待")
    time.sleep(3)
    mode=main_wd.wd.single.isChecked()
    page=main_wd.wd.spinBox.value()
    n=0
    if not os.path.exists('download'):
        os.makedirs('download')
    if not os.path.exists('decode_pic'):
        os.makedirs('decode_pic')
    for i in range(0,page+1,50):
        url=r'https://tieba.baidu.com/f?kw=%E5%B9%BB%E5%BD%B1%E5%9D%A6%E5%85%8B&pn='+str(i)
        rsp=requests.get(url,headers=headers)
        if rsp.status_code==200:
            name=re.findall(reg,str(rsp.text.encode('utf-8')))
            for new in name:
                if r'/p/' in new[0]:
                    rsp=requests.get('https://tieba.baidu.com/'+new[0],headers=headers)
                    if rsp.status_code==200:
                        pics=re.findall(reg2,str(rsp.text))
                        for pic in pics:
                            p=requests.get(pic,headers=headers)
                            with open(r'download/'+str(n)+pic[-4:],'wb') as f:
                                f.write(p.content)
                            if mode:
                                decode.decode(r'download/',str(n)+pic[-4:],mode)
                            n+=1
                            main_wd.wd.label_5.setText('正在处理第'+str(n)+'图片')
                        time.sleep(0.5)
        time.sleep(1)
    if not mode:
        decode.decode(r'download/',os.listdir('download'),mode)
    QMessageBox.about(main_wd.widget,'处理结果:',"共下载"+str(n)+'张图片   解码成功'+str(len(os.listdir('decode_pic')))+'张图片')
    donate_wd.widget.show()
class my_main_wd(QWidget):
    def __init__(self):
        super(my_main_wd,self).__init__()
        self.widget= QWidget()
        self.wd=main_wd.Ui_main_windows()
        self.wd.setupUi(self.widget)
        self.wd.start.clicked.connect(start)
        self.wd.spinBox.setMaximum(1000)
class donate_wd(QWidget):
    def __init__(self):
        super(donate_wd,self).__init__()
        self.widget= QWidget()
        self.wd=donate.Ui_form()
        self.wd.setupUi(self.widget)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    donate_wd=donate_wd()
    main_wd=my_main_wd()
    main_wd.widget.show()
    sys.exit(app.exec_())