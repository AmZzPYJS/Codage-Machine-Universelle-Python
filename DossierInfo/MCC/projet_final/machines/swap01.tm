name: Swap 0 and 1
init: q0
accept: qF

// transforme chaque 0 en 1 et chaque 1 en 0, s'arrête sur blanc
q0,0
q0,1,>
q0,1
q0,0,>
q0,_
qF,_,-
