name: Search in list
init: qCopyX
accept: qAccept

qCopyX,0,_
qCopyX,0,0,>,>
qCopyX,1,_
qCopyX,1,1,>,>
qCopyX,#,_
qGoWord,#,_,>,-

qGoWord,0,_
qPrep,0,_,-,-
qGoWord,1,_
qPrep,1,_,-,-
qGoWord,_,_
qLoop,_,_,-,-

qPrep,0,0
qPrep,0,0,-,<
qPrep,0,1
qPrep,0,1,-,<
qPrep,1,0
qPrep,1,0,-,<
qPrep,1,1
qPrep,1,1,-,<
qPrep,#,0
qPrep,#,0,-,<
qPrep,#,1
qPrep,#,1,-,<
qPrep,0,_
qCmp,0,_,-,>
qPrep,1,_
qCmp,1,_,-,>

qCmp,0,0
qCmp,0,0,>,>
qCmp,1,1
qCmp,1,1,>,>
qCmp,#,_
qAccept,#,_,-,-
qCmp,0,1
qSkip,0,1,>,-
qCmp,1,0
qSkip,1,0,>,-
qCmp,0,_
qSkip,0,_ ,>,-
qCmp,1,_
qSkip,1,_ ,>,-

qSkip,0,0
qSkip,0,0,>,-
qSkip,1,1
qSkip,1,1,>,-
qSkip,0,_
qSkip,0,_ ,>,-
qSkip,1,_
qSkip,1,_ ,>,-
qSkip,#,_
qGoWord,#,_,>,-

qLoop,0,0
qLoop,0,0,-,-
qLoop,1,1
qLoop,1,1,-,-
qLoop,#,_
qLoop,#,_,-,-
qLoop,_,_
qLoop,_,_,-,-
