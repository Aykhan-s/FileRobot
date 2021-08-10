from PyQt6 import QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QWidget
from MainWindow import Ui_MainWindow
import sys
import os
import main as mn
import webbrowser
from Form import Ui_Form
import rc_icons

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        
        self.x = Ui_Form()
        self.x.setupUi(self)
       
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.fr = Window2()
        
        #tab1<
        self.ui.combo.addItems(['PDF', 'TXT', 'PPTX', 'PPT', 'XLSX', 'DOCX', 
                                'DOC', 'MP4', 'MP3', 'PNG', 'JPG', 'JPEG', 'ICO'])
        
        self.exception_folder = []
        self.exception_folder_print = []
        self.exception_files = []
        self.exception_files_print = []
        self.directory = ''
        self.new_folder = ''
        
        self.ui.actionGitHub.triggered.connect(lambda : webbrowser.open("https://github.com/Ayxan3-14/Projects"))
        self.ui.select_radio_btn.clicked.connect(self.select_radio_btn_def)
        self.ui.search_btn.clicked.connect(self.file_sh)
        self.ui.open_btn.clicked.connect(self.file_open)
        self.ui.includ_radio_btn.clicked.connect(self.includ_radio_btn_def)
        self.ui.exception_folder_btn.clicked.connect(self.exception_folder_def)
        self.ui.exception_file_btn.clicked.connect(self.exception_file_def)
        self.ui.delete_btn.clicked.connect(self.delete_def)
        self.ui.create_btn.clicked.connect(self.create_folder)
        self.ui.copy_btn.clicked.connect(self.copy_def)
        self.ui.clear_btn.clicked.connect(self.clear_def)
        self.ui.actionHaqq_nda.triggered.connect(self.about)
        #tab1>
        
        #tab2<
        self.directory_tab2 = ''
        self.ui.pushButton_3.clicked.connect(self.file_sh_tab2)
        self.ui.pushButton.clicked.connect(self.file_open_tab2)
        self.ui.pushButton_4.clicked.connect(self.clear_def_tab2)
        self.ui.pushButton_6.clicked.connect(self.delete_def_tab2)
        self.ui.pushButton_2.clicked.connect(self.goto_file)
        #tab2>
    
    def clear_def_tab2(self):
        self.ui.lineEdit.clear()
        self.ui.checkBox.setChecked(False)
        self.directory_tab2 = ''
        self.ui.label_3.setText('Seçilməyib')
        self.ui.pushButton_6.setDisabled(True)
    
    def goto_file(self):
        if self.ui.lineEdit_2.text():
            try:
                os.startfile(self.ui.lineEdit_2.text())
            
            except FileNotFoundError:
                QMessageBox.warning(self, 'Adres düzgün dəyil!', 'Qovluq (fayl) adresi düzgün dəyil')
            
        else:
            QMessageBox.warning(self, 'Qovluq adresi daxil etməlisiniz!', 'Qovluq (fayl) adresi daxil etməmisiniz')
    
    def delete_def_tab2(self):
        icon = ":/icons/icons/Google-Noto-Emoji-Symbols-73028-warning.ico"
        text = f'{self.d.cnt} ədəd {self.d.file_name} faylını silmək istəyirsiniz?'
        
        result = self.notification_screen(icon, 'Fayllar silinir', text, 'Yox', 'Hə')

        if result == 16384:
            self.d.file_delete()
            self.ui.pushButton_6.setDisabled(True)
            st = '{} qovluğundakı\n{} ədəd {} faylı silindi.'
            st = st.format(self.directory_print_tab2, self.d.cnt, self.d.file_name)
            QMessageBox.information(self, 'Fayllar Silindi', st)
    
    def file_open_tab2(self):
        x = str(QFileDialog.getExistingDirectory(self, "Axtarılacaq qovluğu seçin", os.getenv('HOME')))
        if x:
            self.ui.pushButton_6.setDisabled(True)
            self.directory_tab2 = x.replace('/','\\')
            self.directory_print_tab2 = os.path.split(self.directory_tab2)[1]
            self.ui.label_3.setText(self.directory_print_tab2)
            
    def file_sh_tab2(self):
        if not self.ui.lineEdit.text():
            QMessageBox.warning(self, 'Fayl adı daxil etməlisiniz!', 'Fayl adı daxil etməmisiniz')
            
        elif not self.directory_tab2:
            QMessageBox.warning(self, 'Axtarılacaq qovluq seçməlisiniz!', 'Axtarılacaq qovluq seçməmisiniz')

        else:
            self.d = mn.Search_file(self.ui.lineEdit.text(), self.directory_tab2)
            
            if self.ui.checkBox_2.isChecked() and self.ui.checkBox.isChecked():
                self.d.file_search_extention()
            
            elif not self.ui.checkBox_2.isChecked() and not self.ui.checkBox.isChecked():
                self.d.file_search_lower()
            
            elif self.ui.checkBox.isChecked():
                self.d.file_search()
                
            elif self.ui.checkBox_2.isChecked():
                self.d.file_search_lower_extention()
                
            if self.d.cnt != 0:
                self.ui.pushButton_6.setDisabled(False)
                text = '{} qovluğunda\n{} ədəd {} faylı tapıldı.'
                text = text.format(self.directory_print_tab2, self.d.cnt, self.d.file_name)
                icon = ":/icons/icons/Custom-Icon-Design-Flatastic-1-Information.ico"
                text = f'{self.d.cnt} ədəd {self.d.file_name} faylı tapıldı'
        
                result = self.notification_screen(icon, 'Fayl tapıldı', text, 'Bağla', 'Göstər')
        
                if result == 16384:
                    self.fr.show()
                    self.fr.setWindowIcon(QtGui.QIcon(":/icons/icons/Custom-Icon-Design-Flatastic-1-Information.ico"))
                    file_print = [i for i in self.d.l]
                    self.fr.x.textBrowser.setText(('\n'+'-'*90).join(file_print))
                    
            else:
                QMessageBox.information(self, 'Fayl tapılmadı!', f'{self.d.file_name} adında fayl tapılmadı')
            

    
    def about(self):
        text = '''<font size = 4><b>Ayxan Şahsuvarov</b> tərəfindən hazırlandı.
    <br><br>
    Bütün boğuşdurma haqları sərbəstdi.
    <br><br>
    <br><br>
    </font>
    <font size = 2>© Hüquqları qorunmur</font>
    '''
        QMessageBox.about(self, 'Haqqında', text)
        
    def clear_def(self):
        self.ui.exception_folder_lbl.setText('Seçilməyib')
        self.ui.exception_file_lbl.setText('Seçilməyib')
        self.ui.create_file_lbl.setText('Seçilməyib')
        self.ui.open_lbl.setText('Seçilməyib')
        self.directory = ''
        self.new_folder = ''
        self.exception_folder = []
        self.exception_folder_print = []
        self.exception_files = []
        self.exception_files_print = []
        self.ui.include_line_edit.clear()
        self.ui.exception_folder_btn.setDisabled(True)
        self.ui.exception_file_btn.setDisabled(True)
        self.ui.copy_btn.setDisabled(True)
        self.ui.delete_btn.setDisabled(True)
        self.ui.create_btn.setDisabled(True)
        self.ui.select_radio_btn.setChecked(True)
        self.ui.combo.setDisabled(False)
        self.ui.include_line_edit.setDisabled(True)
        self.ui.include_line_edit.setPlaceholderText('')
        self.ui.combo.setCurrentIndex(0)
        
    def select_radio_btn_def(self):
        self.ui.combo.setDisabled(False)
        self.ui.include_line_edit.setDisabled(True)
        self.ui.include_line_edit.setPlaceholderText('')
        self.ui.combo.showPopup()
        
    def includ_radio_btn_def(self):
        self.ui.combo.setDisabled(True)
        self.ui.include_line_edit.setDisabled(False)
        self.ui.include_line_edit.setPlaceholderText('Fayl tipini daxil edin')
        
    def file_open(self):
        x = str(QFileDialog.getExistingDirectory(self, "Axtarılacaq qovluğu seçin", os.getenv('HOME')))
        if x:
            self.ui.copy_btn.setDisabled(True)
            self.ui.delete_btn.setDisabled(True)
            self.directory = x.replace('/','\\')
            self.directory_print = os.path.split(self.directory)[1]
            self.ui.open_lbl.setText(os.path.split(self.directory_print)[1])
            self.ui.exception_folder_btn.setDisabled(False)
            self.ui.exception_file_btn.setDisabled(False)
            
    def create_folder(self):
        x = QFileDialog.getExistingDirectory(self, 'Faylların kopyalanacağı yeri seçin', os.getenv('HOME'))
        if x:
            self.new_folder = x.replace('/','\\')
            self.ui.create_file_lbl.setText(os.path.split(self.new_folder)[1])

    def exception_folder_def(self):
        x = str(QFileDialog.getExistingDirectory(self, "İstisna olunacaq qovluq seçin", self.directory))
        if x:
            x = x.replace('/','\\')
            if x not in self.exception_folder:
                self.ui.copy_btn.setDisabled(True)
                self.ui.delete_btn.setDisabled(True)
                self.exception_folder.append(x)
                self.exception_folder_print.append(os.path.split(x)[1])
                self.ui.exception_folder_lbl.setText('\n'.join(self.exception_folder_print))
        
    def exception_file_def(self):
        x = QFileDialog.getOpenFileName(self, "İstisna olunacaq fayl seçin", self.directory)[0]
        if x:
            x = x.replace('/','\\')
            if x not in self.exception_files:
                self.ui.copy_btn.setDisabled(True)
                self.ui.delete_btn.setDisabled(True)
                self.exception_files.append(x)
                self.exception_files_print.append(os.path.split(x)[1])
                self.ui.exception_file_lbl.setText('\n'.join(self.exception_files_print))
        
    def file_sh(self):
        if not self.directory:
            QMessageBox.warning(self, 'Axtarılacaq qovluq seçməlisiniz!', 'Axtarılacaq qovluq seçməmisiniz')
            
        else:
            if self.ui.select_radio_btn.isChecked():
                file_name = self.ui.combo.currentText()
                self.file_sh_print(file_name)
                
            elif self.ui.includ_radio_btn.isChecked():
                file_name = self.ui.include_line_edit.text()
                if file_name:
                    self.file_sh_print(file_name)
                    
                else:
                    QMessageBox.warning(self, 'Fayl tipini daxil etməlisiniz!', 'Fayl tipini daxil etməmisiz')
                    
    def file_sh_print(self, file_name):
        self.c = mn.Copy_file(file_name.upper(), self.directory, 
                            self.exception_folder, self.exception_files)

        if self.c.cnt != 0:
            self.ui.copy_btn.setDisabled(False)
            self.ui.delete_btn.setDisabled(False)
            self.ui.create_btn.setDisabled(False)
            
            icon = ":/icons/icons/Custom-Icon-Design-Flatastic-1-Information.ico"
            text = f'{self.c.cnt} ədəd {self.c.file_name} faylı tapıldı'
        
            result = self.notification_screen(icon, 'Fayllar tapıldı', text, 'Bağla', 'Göstər')
        
            if result == 16384:
                self.fr.show()
                self.fr.setWindowIcon(QtGui.QIcon(":/icons/icons/Custom-Icon-Design-Flatastic-1-Information.ico"))
                file_print = [k for i,k,j in self.c.d]
                self.fr.x.textBrowser.setText(('\n'+'-'*88).join(file_print)) 
        else:
            QMessageBox.information(self, 'Fayl tapılmadı!', f'{self.c.file_name} tipində fayl tapılmadı')
        
    def copy_def(self):
        if not self.new_folder:
            QMessageBox.warning(self, 'Faylların kopyalanacağı yer seçməlisiniz!', 'Faylların kopyalanacağı yer seçməmisiniz')        
            
        else:
            self.c.file_copy(self.new_folder)
            st = '{} qovluğundakı {} ədəd {} faylının\n{} dənəsi {} qovluğuna kopyalandı.'
            st = st.format(self.directory_print, self.c.cnt, 
                                                       self.c.file_name, len(self.c),
                                                       os.path.split(self.new_folder)[1]+'\\'+os.path.split(self.c.doc_address)[1])
            QMessageBox.information(self, 'Fayllar Kopyalandı', st)
            
    def notification_screen(self, icon, windowtitle, text, btn_no_text, btn_yes_text):
        mb = QMessageBox()
        mb.setWindowIcon(QtGui.QIcon(icon))
        mb.setWindowTitle(windowtitle)
        mb.setText(text)
        mb.setStandardButtons(QMessageBox.StandardButton.Yes |
                          QMessageBox.StandardButton.No)
        mb.setEscapeButton(QMessageBox.StandardButton.No)
            
        btn_no = mb.button(QMessageBox.StandardButton.No)
        btn_no.setText(btn_no_text)
        btn_yes = mb.button(QMessageBox.StandardButton.Yes)
        btn_yes.setText(btn_yes_text)
        
        result = mb.exec()
        
        return result
        
    def delete_def(self):
        icon = ":/icons/icons/Google-Noto-Emoji-Symbols-73028-warning.ico"
        text = f'{self.c.cnt} ədəd {self.c.file_name} faylını silmək istəyirsiniz?'
        
        result = self.notification_screen(icon, 'Fayllar silinir', text, 'Yox', 'Hə')

        if result == 16384:
            self.c.file_delete()
            self.ui.copy_btn.setDisabled(True)
            self.ui.delete_btn.setDisabled(True)
            st = '{} qovluğundakı\n{} ədəd {} faylı silindi.'
            st = st.format(self.directory_print, self.c.cnt, self.c.file_name)
            QMessageBox.information(self, 'Fayllar Silindi', st)
            

app = QtWidgets.QApplication(sys.argv)
wnd = Window()
wnd.show()
sys.exit(app.exec())