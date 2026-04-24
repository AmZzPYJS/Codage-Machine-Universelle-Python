name: Compare x<y
init: qSeekHash
accept: qAccept

qSeekHash,0,_
qSeekHash,0,_,>,-
qSeekHash,1,_
qSeekHash,1,_,>,-
qSeekHash,#,_
qCopyY,#,_,>,-

qCopyY,0,_
qCopyY,0,0,>,>
qCopyY,1,_
qCopyY,1,1,>,>
qCopyY,_,_
qBack,_,_,<,<

qBack,0,0
qBack,0,0,<,<
qBack,1,1
qBack,1,1,<,<
qBack,#,0
qBack,#,0,<,<
qBack,#,1
qBack,#,1,<,<
qBack,0,_
qBack,0,_,<,-
qBack,1,_
qBack,1,_,<,-
qBack,#,_
qBack,#,_,<,-
qBack,_,_
qLen,_,_,>,>

qLen,0,0
qLen,0,0,>,>
qLen,0,1
qLen,0,1,>,>
qLen,1,0
qLen,1,0,>,>
qLen,1,1
qLen,1,1,>,>

qLen,#,0
qAccept,#,0,-,-
qLen,#,1
qAccept,#,1,-,-

qLen,0,_
qLoop,0,_,-,-
qLen,1,_
qLoop,1,_,-,-

qLen,#,_
qBack2,#,_,<,<

qBack2,0,0
qBack2,0,0,<,<
qBack2,0,1
qBack2,0,1,<,<
qBack2,1,0
qBack2,1,0,<,<
qBack2,1,1
qBack2,1,1,<,<
qBack2,#,0
qBack2,#,0,<,<
qBack2,#,1
qBack2,#,1,<,<
qBack2,0,_
qBack2,0,_,<,-
qBack2,1,_
qBack2,1,_,<,-
qBack2,#,_
qBack2,#,_,<,-
qBack2,_,_
qCmp,_,_,>,>

qCmp,0,0
qCmp,0,0,>,>
qCmp,1,1
qCmp,1,1,>,>
qCmp,0,1
qAccept,0,1,-,-
qCmp,1,0
qLoop,1,0,-,-
qCmp,#,_
qLoop,#,_,-,-

qLoop,0,0
qLoop,0,0,-,-
qLoop,0,1
qLoop,0,1,-,-
qLoop,0,_
qLoop,0,_,-,-

qLoop,1,0
qLoop,1,0,-,-
qLoop,1,1
qLoop,1,1,-,-
qLoop,1,_
qLoop,1,_,-,-

qLoop,#,0
qLoop,#,0,-,-
qLoop,#,1
qLoop,#,1,-,-
qLoop,#,_
qLoop,#,_,-,-

qLoop,_,0
qLoop,_,0,-,-
qLoop,_,1
qLoop,_,1,-,-
qLoop,_,_
qLoop,_,_,-,-