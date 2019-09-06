eligible(X) :- highGPA(X), student(X).
eligible(X) :- minority(X), fairGPA(X), student(X).
-eligible(X) :- -fairGPA(X), -highGPA(X), student(X).
interview(X) :- not &k{ eligible(X) }, not &k{ -eligible(X) }, student(X).