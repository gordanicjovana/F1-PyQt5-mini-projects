import sys
from PyQt5.QtWidgets import(QApplication,QWidget,QLabel,QLineEdit,QPushButton,QVBoxLayout,QHBoxLayout,QGroupBox,QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.uic.Compiler.qtproxies import QtWidgets


class F1FuelCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('F1 strategy and fuel calculator')
        self.setFixedSize(450,400)
        self.setStyleSheet("background-color:#1E1E1E;color:#FFFFFF;")

        title_font=QFont('Helvetica',16,QFont.Bold)
        label_font=QFont('Helvetica',10);
        btn_font=QFont('Helvetica',11,QFont.Bold)

        self.title_label=QLabel('F1 strategy and fuel calculator',self)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignHCenter)
        self.title_label.setStyleSheet("color:#FFFF00;margin-bottom:15px;")

        input_group=QGroupBox("Race Parameters")
        input_group.setStyleSheet("QGroupBox{border:1px solid #444444;border-radius:5px;margin-top:10px;padding:10px;}color:#AAAAAA")
        group_layout=QVBoxLayout()

        self.laps_label=QLabel('Total Race laps:')
        self.laps_label.setFont(label_font)
        self.laps_input=QLineEdit()
        self.laps_input.setPlaceholderText('e.g, 53(Monza)')
        self.laps_input.setStyleSheet("background-color:#2D2D2D;border:1px solid #555555;padding:5px;border-radius:3px;color:white")

        self.cons_label = QLabel('Avg fuel consumption per lap(kg):')
        self.cons_label.setFont(label_font)
        self.cons_input = QLineEdit()
        self.cons_input.setPlaceholderText('e.g, 1.75')
        self.cons_input.setStyleSheet("background-color:#2D2D2D;border:1px solid #555555;padding:5px;border-radius:3px;color:white")

        group_layout.addWidget(self.laps_label)
        group_layout.addWidget(self.laps_input)
        group_layout.addWidget(self.cons_label)
        group_layout.addWidget(self.cons_input)
        input_group.setLayout(group_layout)

        self.calc_btn=QPushButton('CALCULATE STRATEGY',self)
        self.calc_btn.setFont(btn_font)
        self.calc_btn.setCursor(Qt.PointingHandCursor)
        self.calc_btn.setStyleSheet("""QPushButton{background-color:#FFFF00;color:black;border-radius:5px;padding:10px;margin-top:10px}QPushButton:hover{background-color:#CCCC00;}""")
        self.calc_btn.clicked.connect(self.calculate_fuel)

        self.result_label=QLabel('',self)
        self.result_label.setFont(QFont('Helvetica',11))
        self.result_label.setAlignment(Qt.AlignHCenter)
        self.result_label.setStyleSheet("color:#00FF00;margin-top:15px;")

        main_layout=QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addWidget(input_group)
        main_layout.addWidget(self.calc_btn)
        main_layout.addWidget(self.result_label)
        main_layout.setContentsMargins(20,20,20,20)

        self.setLayout(main_layout)

    def calculate_fuel(self):
        try:
            laps=int(self.laps_input.text())
            consumption=float(self.cons_input.text())

            if laps<=0 or consumption<=0:
                raise ValueError

            race_fuel=laps*consumption
            total_fuel_req=race_fuel+1.0

            if total_fuel_req>110.0:
                QMessageBox.warning(self,'Fuel limit Exceeded',f"Warning: Calculated fuel({total_fuel_req:.2f}kg)exceeds maximum F1 tank capacity(110 kg)!\nConsider lift-and-coast strategy.")

            self.result_label.setText(
                f"Minimum Fuel needed:{total_fuel_req:.2f}kg\n"
                f"(Includes 1.0 kg FIA sample requirement)"
            )
            self.result_label.setStyleSheet("color:#00FF00;font-weight:bold;")

        except ValueError:
            QMessageBox.critical(self,'Input Error','Please enter valid positive number for laps and consumption.')

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=F1FuelCalc()
    ex.show()
    sys.exit(app.exec_())