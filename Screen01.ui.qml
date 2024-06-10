

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 6.7
import QtQuick.Controls 6.7
import Vocoin
import Qt.SafeRenderer
import QtQuick.Layouts
import FlowView
import QtQuick.Studio.Components
import QtQuick.Studio.Effects
import QtQuick.Studio.LogicHelper
import SimulinkConnector
import QtQuickUltralite.Studio.Components
import QtQuickUltralite.Profiling
import QtQuickUltralite.Layers

Rectangle {
    id: login_window
    width: Constants.width
    height: Constants.height
    color: "#222222"

    SLConnector {
        root: login_window
    }

    Text {
        id: login_title
        x: 191
        y: 159
        width: 98
        height: 45
        color: "#ffffff"
        text: qsTr("login")
        font.pixelSize: 24
        horizontalAlignment: Text.AlignHCenter
        font.bold: true
    }

    TextField {
        id: password_input
        x: 140
        y: 362
        opacity: 0.5
        visible: true
        hoverEnabled: false
        placeholderTextColor: "#81353637"
        selectionColor: "#222222"
        placeholderText: qsTr("password")
        clip: false
    }

    Button {
        id: sing_in
        x: 140
        y: 408
        width: 200
        height: 40
        text: qsTr("sing in")
        highlighted: true
        display: AbstractButton.TextOnly
        font.styleName: "Bold"
        font.pointSize: 12
        flat: false
        icon.color: "#000000"
        icon.height: 35
        icon.width: 35
    }

    Button {
        id: sing_up
        x: 140
        y: 454
        width: 200
        height: 40
        text: qsTr("sing up")
        highlighted: true
        display: AbstractButton.TextOnly
        font.styleName: "Bold"
        font.pointSize: 12
    }

    TextField {
        id: login_input
        x: 140
        y: 316
        opacity: 0.5
        visible: true
        hoverEnabled: false
        placeholderTextColor: "#81353637"
        selectionColor: "#222222"
        placeholderText: qsTr("login")
        color: "#000000"
        clip: false
    }

    Text {
        id: debug_line
        x: 140
        y: 274
        width: 200
        height: 36
        color: "#ffffff"
        text: qsTr("")
        font.pixelSize: 24
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }
}
