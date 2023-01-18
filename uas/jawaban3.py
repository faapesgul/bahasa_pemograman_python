"""
GUI (graphical user interface), adalah bentuk antarmuka pengguna yang memungkinkan pengguna untuk berinteraksi dengan perangkat elektronik melalui ikon
grafis dan indikator audio seperti notasi utama, bukan UI berbasis teks, mengetik label perintah atau navigasi teks.
GUI diperkenalkan sebagai reaksi terhadap kurva pembelajaran CLI yang curam (command-line interfaces), yang membutuhkan perintah untuk diketik
pada keyboard komputer.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QLabel)

app = QApplication([])
label = QLabel('Nama: Fikri Alam Arya Putra')
label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
label.show()
app.exec()
