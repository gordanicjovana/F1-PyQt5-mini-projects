import sys
import random
import time
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout
from PyQt5.QtGui import QFont,QPainter,QColor
from PyQt5.QtCore import Qt,QTimer

class F1ReactionTest(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('F1 Reaction Test')
        self.setFixedSize(500,380)
        self.setStyleSheet("background-color:#121212;color:white;")

        self.light_timer=QTimer()
        self.light_timer.timeout.connect(self.turn_on_next_light)

        self.random_delay_timer=QTimer()
        self.random_delay_timer.timeout.connect(self.lights_out)

        self.lights_state=0
        self.game_running=False
        self.can_react=False
        self.start_time=0

        self.title_label=QLabel('F1 reaction time test',self)
        self.title_label.setFont(QFont('Helvetica',16,QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("color:#FFFF00;margin-bottom:10px;")

        self.result_label=QLabel('Press START,wait for lights to go OUT,then hit SPACE!',self)
        self.result_label.setFont(QFont('Helvetica',11,QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("color:#AAAAAA;margin-top:15px;")

        self.start_btn=QPushButton('START SEQUENCE',self)
        self.start_btn.setFont(QFont('Helvetica',11,QFont.Bold))
        self.start_btn.setCursor(Qt.PointingHandCursor)
        self.start_btn.setStyleSheet("""QPushButton{background-color:#FFFF00;color:black;border-radius:5px;padding:12px;margin-top:10px;}QPushButton:hover{background-color:#CCCC00}""")
        self.start_btn.clicked.connect(self.start_sequence)

        main_layout=QVBoxLayout()
        main_layout.addWidget(self.title_label)
        main_layout.addSpacing(120)
        main_layout.addWidget(self.start_btn)
        main_layout.addWidget(self.result_label)
        main_layout.setContentsMargins(30,30,30,30)
        self.setLayout(main_layout)

    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        start_x=75
        y_pos=90
        diameter=50
        spacing=20

        for i in range(5):
            if i<self.lights_state:
                painter.setBrush(QColor('#FF0000'))
            else:
                painter.setBrush(QColor('#333333'))

            painter.setPen(Qt.NoPen)
            painter.drawEllipse(start_x+i*(diameter+spacing),y_pos,diameter,diameter)

    def start_sequence(self):
        self.start_btn.setEnabled(False)
        self.result_label.setText("Focus on the lights...")
        self.result_label.setStyleSheet("color:#AAAAAA;")
        self.lights_state=0
        self.game_running=True
        self.can_react=False
        self.update()

        self.light_timer.start(800)

    def turn_on_next_light(self):
        if self.lights_state<5:
            self.lights_state+=1
            self.update()
        else:
            self.light_timer.stop()
            random_delay=random.randint(1000,3000)
            self.random_delay_timer.start(random_delay)

    def lights_out(self):
        self.random_delay_timer.stop()
        self.lights_state=0
        self.update()
        self.can_react=True
        self.start_time=time.time()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Space and self.game_running:
            if self.can_react:
                end_time=time.time()
                reaction_time=int((end_time-self.start_time)*1000)

                if reaction_time<150:
                    msg=f"Reaction time:{reaction_time}ms.Unreal!You have amazing reflexes!"
                    color="#00FF00"
                elif reaction_time<250:
                    msg=f"Reaction time:{reaction_time}ms.Great start,ready for the grid!"
                    color="#00FF00"
                else:
                    msg=f"Reaction time:{reaction_time}ms.Box,box!A bit slow today."
                    color="#FFFF00"

                self.result_label.setText(msg)
                self.result_label.setStyleSheet(f"color:{color};font-weight:bold;")
            else:
                self.light_timer.stop()
                self.random_delay_timer.stop()
                self.lights_state=0
                self.update()
                self.result_label.setText("FALSE START!Jumped the lights.5 second penalty!")
                self.result_label.setStyleSheet("color:#FF0000;font-weight:bold;")

            self.game_running=False
            self.can_react=False
            self.start_btn.setEnabled(True)

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=F1ReactionTest()
    ex.show()
    sys.exit(app.exec_())