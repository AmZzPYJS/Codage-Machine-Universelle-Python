name: Unary multiplication
init: qCopyN
accept: qAccept

qCopyN,1,_,_
qCopyN,1,1,_,>,>,-
qCopyN,#,_,_
qSeekM,#,_,_,>,-,-

qSeekM,1,_,_
qMarkM,1,_,_,>,-,-
qSeekM,_,_,_
qWriteBack,_,_,_,<,-,<

qMarkM,1,_,_
qAddN,1,_,_,> ,<,-
qMarkM,_,_,_
qWriteBack,_,_,_,<,-,<

qAddN,1,1,_
qAddN,1,1,1,-,>,>
qAddN,1,_,_
qReturnM,1,_,_,-,<,-
qAddN,#,_,_
qReturnM,#,_,_,-,<,-

qReturnM,1,1,1
qReturnM,1,1,1,-,<,-
qReturnM,1,1,_
qReturnM,1,1,_,-,<,-
qReturnM,#,_,_
qMarkM,#,_,_,> ,>,-

qWriteBack,1,_,1
qWriteBack,1,_,1,<,-,<
qWriteBack,#,_,1
qWriteBack,#,_,1,<,-,<
qWriteBack,_,_,_
qCopyOut,_,_,_,>,-,>

qCopyOut,_,_,1
qCopyOut,1,_,1,>,-,>
qCopyOut,_,_,_
qAccept,_,_,_,-,-,-
