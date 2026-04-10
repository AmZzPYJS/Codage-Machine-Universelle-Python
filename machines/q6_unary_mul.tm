name: Unary multiplication
init: qInit
accept: qAccept

qInit,1,_,_
qCopyN,1,|,|,-,>,>

qStartCopy,X,1,_
qCopyToRes,X,1,_,-,-,-

qCopyN,1,_,_
qCopyN,1,1,_,>,>,-
qCopyN,#,_,_
qRewind2,#,_,_,> ,<,-

qRewind2,1,1,_
qRewind2,1,1,_,-,<,-
qRewind2,1,|,_
qFindM,1,|,_,-,-,-
qRewind2,_,1,_
qRewind2,_,1,_,-,<,-
qRewind2,_,|,_
qFindM,_,|,_,-,-,-

qFindM,X,|,_
qFindM,X,|,_,>,-,-
qFindM,1,|,_
qStartCopy,X,|,_,-,>,-
qFindM,_,|,_
qAccept,_,|,_,-,-,-

qStartCopy,X,|,_
qCopyToRes,X,|,_,-,>,-

qCopyToRes,X,1,_
qCopyToRes,X,1,1,-,>,>
qCopyToRes,X,_,_
qRewind2AfterCopy,X,_,_,-,<,-

qRewind2AfterCopy,X,1,_
qRewind2AfterCopy,X,1,_,-,<,-
qRewind2AfterCopy,X,|,_
qFindM,X,|,_,>,-,-