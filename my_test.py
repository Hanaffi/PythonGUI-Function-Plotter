from PyQt5 import QtCore
from main import MatplotlibWidget
import pytest

@pytest.fixture
def app(qtbot):
     TESTER = MatplotlibWidget()
     qtbot.addWidget(TESTER)
     return TESTER


# Initial values
def test_initial_y_of_x(app):
    assert app.y_of_x.text() == ""
def test_initial_from_x(app):
    assert app.from_x.text() == ""
def test_initial_to_x(app):
    assert app.to_x_2.text() == ""

# Clicking plot without giving values
def test_1(app, qtbot):
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == "x values must be numbers"

# Clicking plot without specifing function format
def test_2(app, qtbot):
    app.to_x_2.setText("1")
    app.from_x.setText("10")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == "Invalid function format!"

# Clicking plot with specifing wrong function format
def test_3(app, qtbot):
    app.to_x_2.setText("1")
    app.from_x.setText("10")
    app.y_of_x.setText("2x+10")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == "Invalid function format!"

# Clicking plot with specifing wrong function format
def test_4(app, qtbot):
    app.to_x_2.setText("1")
    app.from_x.setText("10")
    app.y_of_x.setText("8+4*x2")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == "Invalid function format!"

# Clicking plot with specifing valid function format
def test_6(app, qtbot):
    app.to_x_2.setText("1")
    app.from_x.setText("10")
    app.y_of_x.setText("2*x+10")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == ""

# Clicking plot with from>to
def test_7(app, qtbot):
    app.to_x_2.setText("100")
    app.from_x.setText("10")
    app.y_of_x.setText("8+4*x^2")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == ""

# Clicking plot with specifing valid function format
def test_8(app, qtbot):
    app.to_x_2.setText("1")
    app.from_x.setText("10")
    app.y_of_x.setText("8+4*x^2")
    qtbot.mouseClick(app.plot_button, QtCore.Qt.LeftButton)
    assert app.error_place.text() == ""

