% aturan jenis kelamin
lakilaki(eyangkung).
lakilaki(kakek).
lakilaki(ayah).
lakilaki(om).

perempuan(eyanguti).
perempuan(nenek).
perempuan(budhe).
perempuan(bunda).
perempuan(tante).
perempuan(aku).
perempuan(adik).

% aturan orang tua
bapak(eyangkung,budhe).
bapak(eyangkung,ayah).
bapak(eyangkung,om).
bapak(kakek,bunda).
bapak(kakek,tante).
bapak(ayah,aku).
bapak(ayah,adik).

ibu(eyanguti,budhe).
ibu(eyanguti,ayah).
ibu(eyanguti,om).
ibu(nenek,bunda).
ibu(nenek,tante).
ibu(bunda,aku).
ibu(bunda,adik).

% aturan program
anak(X,Y):-bapak(X,Y).
anak(X,Y):-ibu(X,Y).

orangtua(X,Y):-bapak(X,Y);ibu(X,Y).
orangtua(X,Y):-anak(Y,X).

suami(X,Y):-bapak(X,P),anak(Y,P),lakilaki(X).
istri(X,Y):-ibu(X,P),anak(Y,P),perempuan(X).

cucu(X,Z):-bapak(X,Y),anak(Y,Z).
cucu(X,Z):-ibu(X,Y),anak(Y,Z).

kakekku(Z,X):-anak(Y,Z),bapak(X,Y),lakilaki(X).
nenekku(Z,X):-anak(Y,Z),ibu(X,Y),perempuan(X).

saudaralakilaki(X,Y):-orangtua(Z,X),orangtua(Z,Y),lakilaki(X),X\=Y.
saudaraperempuan(X,Y):-orangtua(Z,X),orangtua(Z,Y),perempuan(X),X\=Y.

mertua(eyangkung,Y):-bapak(X,Y),anak(X,bunda).
mertua(eyanguti,Y):-ibu(X,Y),anak(X,bunda).
mertua(kakek,Y):-bapak(X,Y),anak(X,ayah).
mertua(nenek,Y):-ibu(X,Y),anak(X,ayah).

om(om,aku).
om(om,adik).
