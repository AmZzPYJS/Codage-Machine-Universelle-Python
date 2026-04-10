name: Search in list
init: qInit
accept: qAccept

qInit,0,_
qCopyX,0,|,-,>
qInit,1,_
qCopyX,1,|,-,>

qCopyX,0,_
qCopyX,0,0,>,>
qCopyX,1,_
qCopyX,1,1,>,>
qCopyX,#,_
qGoWord,#,_,>,-

qGoWord,0,0
qPrepLeft,0,0,-,-
qGoWord,0,1
qPrepLeft,0,1,-,-
qGoWord,0,_
qPrepLeft,0,_,-,-
qGoWord,0,|
qPrepLeft,0,|,-,-

qGoWord,1,0
qPrepLeft,1,0,-,-
qGoWord,1,1
qPrepLeft,1,1,-,-
qGoWord,1,_
qPrepLeft,1,_,-,-
qGoWord,1,|
qPrepLeft,1,|,-,-

qGoWord,_,0
qLoop,_,0,-,-
qGoWord,_,1
qLoop,_,1,-,-
qGoWord,_,_
qLoop,_,_,-,-
qGoWord,_,|
qLoop,_,|,-,-

qPrepLeft,0,0
qPrepLeft,0,0,-,<
qPrepLeft,0,1
qPrepLeft,0,1,-,<
qPrepLeft,0,_
qPrepLeft,0,_,-,<
qPrepLeft,0,|
qCmp,0,|,-,>

qPrepLeft,1,0
qPrepLeft,1,0,-,<
qPrepLeft,1,1
qPrepLeft,1,1,-,<
qPrepLeft,1,_
qPrepLeft,1,_,-,<
qPrepLeft,1,|
qCmp,1,|,-,>

qPrepLeft,_,0
qPrepLeft,_,0,-,<
qPrepLeft,_,1
qPrepLeft,_,1,-,<
qPrepLeft,_,_
qPrepLeft,_,_,-,<
qPrepLeft,_,|
qCmp,_,|,-,>

qCmp,0,0
qCmp,0,0,>,>
qCmp,1,1
qCmp,1,1,>,>
qCmp,#,_
qAccept,#,_,-,-

qCmp,#,0
qGoWord,#,0,>,-
qCmp,#,1
qGoWord,#,1,>,-

qCmp,0,1
qSkipWord,0,1,>,-
qCmp,1,0
qSkipWord,1,0,>,-
qCmp,0,_
qSkipWord,0,_,>,-
qCmp,1,_
qSkipWord,1,_,>,-

qSkipWord,0,0
qSkipWord,0,0,>,-
qSkipWord,0,1
qSkipWord,0,1,>,-
qSkipWord,0,_
qSkipWord,0,_,>,-
qSkipWord,0,|
qSkipWord,0,|,>,-

qSkipWord,1,0
qSkipWord,1,0,>,-
qSkipWord,1,1
qSkipWord,1,1,>,-
qSkipWord,1,_
qSkipWord,1,_,>,-
qSkipWord,1,|
qSkipWord,1,|,>,-

qSkipWord,#,0
qGoWord,#,0,>,-
qSkipWord,#,1
qGoWord,#,1,>,-
qSkipWord,#,_
qGoWord,#,_,>,-
qSkipWord,#,|
qGoWord,#,|,>,-

qSkipWord,_,0
qLoop,_,0,-,-
qSkipWord,_,1
qLoop,_,1,-,-
qSkipWord,_,_
qLoop,_,_,-,-
qSkipWord,_,|
qLoop,_,|,-,-

qLoop,0,0
qLoop,0,0,-,-
qLoop,0,1
qLoop,0,1,-,-
qLoop,0,_
qLoop,0,_,-,-
qLoop,0,|
qLoop,0,|,-,-

qLoop,1,0
qLoop,1,0,-,-
qLoop,1,1
qLoop,1,1,-,-
qLoop,1,_
qLoop,1,_,-,-
qLoop,1,|
qLoop,1,|,-,-

qLoop,#,0
qLoop,#,0,-,-
qLoop,#,1
qLoop,#,1,-,-
qLoop,#,_
qLoop,#,_,-,-
qLoop,#,|
qLoop,#,|,-,-

qLoop,_,0
qLoop,_,0,-,-
qLoop,_,1
qLoop,_,1,-,-
qLoop,_,_
qLoop,_,_,-,-
qLoop,_,|
qLoop,_,|,-,-