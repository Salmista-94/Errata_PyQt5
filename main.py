# -*- coding: utf-8 -*-
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtCore import QVariant, QUrl, QDir, QProcessEnvironment, QProcess
from PyQt5.QtQml import QQmlApplicationEngine, QQmlEngine, QQmlContext, QQmlComponent
from PyQt5.QtQuick import QQuickView, QQuickItem, QQuickWindow
from PyQt5.QtTest import QTest as Test




if __name__ == '__main__':
    import sys, os
    app = QApplication(sys.argv)

    os.putenv("QT_QUICK_CONTROLS_STYLE", "Flat")
    engine = QQmlApplicationEngine(QUrl("MAIN.qml"))

    sys.exit(app.exec_())
