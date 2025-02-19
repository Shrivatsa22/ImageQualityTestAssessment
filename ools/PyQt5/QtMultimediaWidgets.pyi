# The PEP 484 type hints stub file for the QtMultimediaWidgets module.
#
# Generated by SIP 6.8.6
#
# Copyright (c) 2024 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

import PyQt5.sip

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtNetwork
from PyQt5 import QtMultimedia
from PyQt5 import QtWidgets

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., Any], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        PyQt5.sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], PyQt5.sip.Buffer, int, None]


class QVideoWidget(QtWidgets.QWidget, QtMultimedia.QMediaBindableInterface):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def videoSurface(self) -> typing.Optional[QtMultimedia.QAbstractVideoSurface]: ...
    def setMediaObject(self, object: typing.Optional[QtMultimedia.QMediaObject]) -> bool: ...
    def paintEvent(self, event: typing.Optional[QtGui.QPaintEvent]) -> None: ...
    def moveEvent(self, event: typing.Optional[QtGui.QMoveEvent]) -> None: ...
    def resizeEvent(self, event: typing.Optional[QtGui.QResizeEvent]) -> None: ...
    def hideEvent(self, event: typing.Optional[QtGui.QHideEvent]) -> None: ...
    def showEvent(self, event: typing.Optional[QtGui.QShowEvent]) -> None: ...
    def event(self, event: typing.Optional[QtCore.QEvent]) -> bool: ...
    saturationChanged: typing.ClassVar[QtCore.pyqtSignal]
    hueChanged: typing.ClassVar[QtCore.pyqtSignal]
    contrastChanged: typing.ClassVar[QtCore.pyqtSignal]
    brightnessChanged: typing.ClassVar[QtCore.pyqtSignal]
    fullScreenChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setSaturation(self, saturation: int) -> None: ...
    def setHue(self, hue: int) -> None: ...
    def setContrast(self, contrast: int) -> None: ...
    def setBrightness(self, brightness: int) -> None: ...
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def setFullScreen(self, fullScreen: bool) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def saturation(self) -> int: ...
    def hue(self) -> int: ...
    def contrast(self) -> int: ...
    def brightness(self) -> int: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def mediaObject(self) -> typing.Optional[QtMultimedia.QMediaObject]: ...


class QCameraViewfinder(QVideoWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def setMediaObject(self, object: typing.Optional[QtMultimedia.QMediaObject]) -> bool: ...
    def mediaObject(self) -> typing.Optional[QtMultimedia.QMediaObject]: ...


class QGraphicsVideoItem(QtWidgets.QGraphicsObject, QtMultimedia.QMediaBindableInterface):

    def __init__(self, parent: typing.Optional[QtWidgets.QGraphicsItem] = ...) -> None: ...

    def videoSurface(self) -> typing.Optional[QtMultimedia.QAbstractVideoSurface]: ...
    def setMediaObject(self, object: typing.Optional[QtMultimedia.QMediaObject]) -> bool: ...
    def itemChange(self, change: QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any: ...
    def timerEvent(self, event: typing.Optional[QtCore.QTimerEvent]) -> None: ...
    nativeSizeChanged: typing.ClassVar[QtCore.pyqtSignal]
    def paint(self, painter: typing.Optional[QtGui.QPainter], option: typing.Optional[QtWidgets.QStyleOptionGraphicsItem], widget: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def boundingRect(self) -> QtCore.QRectF: ...
    def nativeSize(self) -> QtCore.QSizeF: ...
    def setSize(self, size: QtCore.QSizeF) -> None: ...
    def size(self) -> QtCore.QSizeF: ...
    def setOffset(self, offset: typing.Union[QtCore.QPointF, QtCore.QPoint]) -> None: ...
    def offset(self) -> QtCore.QPointF: ...
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def mediaObject(self) -> typing.Optional[QtMultimedia.QMediaObject]: ...


class QVideoWidgetControl(QtMultimedia.QMediaControl):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    saturationChanged: typing.ClassVar[QtCore.pyqtSignal]
    hueChanged: typing.ClassVar[QtCore.pyqtSignal]
    contrastChanged: typing.ClassVar[QtCore.pyqtSignal]
    brightnessChanged: typing.ClassVar[QtCore.pyqtSignal]
    fullScreenChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setSaturation(self, saturation: int) -> None: ...
    def saturation(self) -> int: ...
    def setHue(self, hue: int) -> None: ...
    def hue(self) -> int: ...
    def setContrast(self, contrast: int) -> None: ...
    def contrast(self) -> int: ...
    def setBrightness(self, brightness: int) -> None: ...
    def brightness(self) -> int: ...
    def setFullScreen(self, fullScreen: bool) -> None: ...
    def isFullScreen(self) -> bool: ...
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def videoWidget(self) -> typing.Optional[QtWidgets.QWidget]: ...
