from bs4 import BeautifulSoup
from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(842, 243)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        self.groupBox = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox.setGeometry(QtCore.QRect(9, 19, 421, 161))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 20, 391, 161))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 80, 321, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=Dialog)
        self.comboBox.setGeometry(QtCore.QRect(100, 130, 321, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 30, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 190, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(230, 190, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 50, 51, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 30, 321, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 51, 31))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 51, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 80, 321, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        self.pushButton.clicked.connect(self.okbutton_click)
        self.pushButton_2.clicked.connect(self.cancelbutton_click)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Google:"))
        self.comboBox.setItemText(0, _translate("Dialog", "期間指定なし"))
        self.comboBox.setItemText(1, _translate("Dialog", "1 時間以内"))
        self.comboBox.setItemText(2, _translate("Dialog", "24 時間以内"))
        self.comboBox.setItemText(3, _translate("Dialog", "1 週間以内"))
        self.comboBox.setItemText(4, _translate("Dialog", "1 か月以内"))
        self.comboBox.setItemText(5, _translate("Dialog", "1 年以内"))
        self.lineEdit.setText(_translate("Dialog", "適切に保護することを社会的責務と考え 下記の方針に基づき その保護を徹底してまいります"))
        self.lineEdit_2.setText(_translate("Dialog", "133.242.4.17 || 133.242.1.214"))
        self.pushButton_2.setText(_translate("Dialog", "キャンセル"))
        self.pushButton.setText(_translate("Dialog", "確認"))
        self.label_3.setText(_translate("Dialog", "URL:"))
        self.lineEdit_3.setText(_translate("Dialog", "https://www.tl-assist.com/user/reservation/r8fteh3p/staff"))
        self.label_4.setText(_translate("Dialog", "Date:"))
        self.label_2.setText(_translate("Dialog", "Big:"))
        self.lineEdit_4.setText(_translate("Dialog", "https://www.tl-assist.com/user/reservation/f3c296sp/staff"))
    
    def okbutton_click(self):
        self.time = self.comboBox.currentIndex()
        self.googlekey = self.lineEdit.text()
        self.bingkey = self.lineEdit_2.text()
        self.url1 = self.lineEdit_3.text()
        self.url2 = self.lineEdit_4.text()
        self.google_query = []
        self.bing_query = []
        self.getgoogle_query()
        self.getbing_query()
        urls = []
        urls += self.getgoogle_atag(self.google_query[0])
        urls += self.getbing_atag(self.bing_query[0])
        urls += self.getbing_atag(self.bing_query[1])
        for url in urls:
            self.get_anchor_text(url)

    def getgoogle_query(self):
        res = 'https://www.google.com/search?q=' + self.googlekey
        timekey = ['', 'h', 'd', 'w', 'm', 'y']
        if self.time != 0:
            res += '&tbs=qdr:' + timekey[self.time]
        self.google_query.append(res)
        
    def getbing_query(self):
        ip = self.text_split()
        timekey = ['', '', '1"', '2"', '3"', '3"']
        res1 = 'https://www.bing.com/search?q=' + ip[0]
        res2 = 'https://www.bing.com/search?q=' + ip[1]
        if self.time == 0:
            self.bing_query.append(res1)
            self.bing_query.append(res2)
        if self.time > 1:
            res1 += '&filters=ex1%3' + 'a"ez' + timekey[self.time]
            res2 += '&filters=ex1%3' + 'a"ez' + timekey[self.time]
            self.bing_query.append(res1)
            self.bing_query.append(res2)
            
    
    def text_split(self):
        if self.bingkey.find('|'):
            self.bingkey = self.bingkey.replace('|', ' ')
        res = self.bingkey.split(' ')
        ips = [ip for ip in res if ip]
        return ips
    
    def getgoogle_atag(self ,url):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(url)

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "search")))

            if "Google" not in driver.title:
                raise Exception("Google did not load properly")

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            a_tags = soup.find_all('a', {'jsname': 'UWckNb'})
            href_values = [a.get('href') for a in a_tags]
            return href_values
        except TimeoutException:
            print("Timed out waiting for Google to load")
            return None
        except Exception as e:
            print("An error occurred:", e)
            return None
        finally:
            driver.quit()
    
    def getbing_atag(self ,url):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(url)

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "b_results")))

            soup = BeautifulSoup(driver.page_source, 'html.parser')
            h2_tags = soup.find_all('h2')
            href_values = []
            for h2_tag in h2_tags:
                a_tags = h2_tag.find_all('a')
                href_values.extend([a.get('href') for a in a_tags if a.get('href')])
            return href_values
        except TimeoutException:
            print("Timed out waiting for Bing to load")
            return None
        except Exception as e:
            print("An error occurred:", e)
            return None
        finally:
            driver.quit()
    
    def get_anchor_text(self, url):
        print('----------------------------')
        print(url)
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
            response.raise_for_status()
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                footer_tag = soup.find('footer')
                if footer_tag:
                    footer_text = footer_tag.get_text()
                    for line in footer_text.split('\n'):
                        if any(keyword in line for keyword in ['会社', '〒', 'TEL']):
                            text = self.remove_tabs(line.strip())
                            print(text)
                else:
                    return None
                print('----------------------------')
            else:
                return None

        except requests.exceptions.RequestException as e:
            return None

    def remove_tabs(self, text):
        return text.replace('\t', '').strip()

    def cancelbutton_click(self):
        sys.exit(app.exec())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
