% Лабораторная работа по ЛОИС №2
% Вариант: 4
% Автор: Терлеев А.С.
% Источники: 
% 1. Логические основы интеллектуальных систем. Практикум : учеб.- метод. пособие / В. В. Голенков [и др.]. – Минск : БГУИР, 2011. – 70 с. : ил. ISBN 978-985-488-487-5.
% 2. SWI Prolog [Электронный ресурс]. -- Режим доступа https://www.swi-prolog.org/
% 3. Искусственный интеллект: современный подход, 4-е изд., том 1 Решение проблем: знания и рассуждения / Рассел, С. и Питер, Н. – Москва : Диалектика, 2021 – 702 с.

son(son1).
son(son2).

daughter(daughter1).
daughter(daughter2).

adult(father).
adult(mother).
adult(police).

notsafe_(criminal, X) :- X \= police.
notsafe_(mother, Y) :- son(Y).
notsafe_(father, Y) :- daughter(Y).

notsafe(X, Y) :- notsafe_(X, Y); notsafe_(Y, X).

safe(X, Y) :- \+ notsafe(X, Y).

safebridge([X, Y]) :- (adult(X); adult(Y)), safe(X, Y), !.
safebridge([X]) :- adult(X).

all([
     son1, son2, father,
     daughter1, daughter2, mother,
     criminal, police
    ]).

allsafe(L) :-
    forall(
        member(H, L),
        (  
            adult(H); 
            son(H), (member(mother, L) -> member(father, L); true); 
            daughter(H), (member(father, L) -> member(mother, L); true); 
            H = criminal, member(police, L)
        )
    ), !.
    
allsafe([_]).
allsafe([]).

allPairs([H | T], [H, P2]) :-
 member(P2, T).

allPairs([_ | T], P) :-
 allPairs(T, P).
    
step_(state(Left1, left), state(Left2, right)) :-
    ( allPairs(Left1, OnBridge)
    ; member(A, Left1),
        OnBridge = [A]
    ),
    
    safebridge(OnBridge),
    
    subtract(Left1, OnBridge, Left2),
    allsafe(Left2),
    
    all(All),
    subtract(All, Left2, Right),
    allsafe(Right).

step(state(Left1, left), state(Left2, right)) :-
    step_(state(Left1, left), state(Left2, right)).

step(state(Left1, right), state(Left2, left)) :-
    all(All),
    subtract(All, Left1, Right1),
    step_(state(Right1, left), state(Right2, right)),
    subtract(All, Right2, Left2).

notequal(state(L1, P1), state(L2, P2)) :-
    \+ (
       P1 = P2,
        sort(L1, L),
        sort(L2, L)
       ).

duplCheck(_, []).
duplCheck(CurrState, [step(State1, _)|T]):-
    notequal(CurrState, State1),
    duplCheck(CurrState, T).


path(state([], _), _, []).

path(Inp, PrevSteps, [step(Inp, S1) | Steps]) :-
    step(Inp, S1),    
    duplCheck(S1, PrevSteps),
    path(S1, [step(Inp, S1) | PrevSteps], Steps).

valid_state(state(Left, Bridge)) :-
    (Bridge == left; Bridge == right),
    all(All),
    subtract(All, Left, Right),
    append(Left, Right, AllCurr),
    sort(All, Tmp),
    sort(AllCurr, Tmp).

printStep(step(state(L1, Pos1), state(L2, _))) :-
    ( Pos1 = left
    -> subtract(L1, L2, Moved),
        all(All),
        subtract(All, L1, R1),
        format('left: ~w | right: ~w~n', [L1, R1]),
        subtract(All, L1, R2),
        format('left: ~w | raft: ~w -> | right: ~w~n~n', [L2, Moved, R2])
    ; Pos1 = right
    -> subtract(L2, L1, Moved),
        all(All),
        subtract(All, L1, R1),
        format('left: ~w | right: ~w~n', [L1, R1]),
        subtract(All, L2, R2),
        format('left: ~w | raft: ~w <- | right: ~w~n~n', [L1, Moved, R2])
    ).

solve(StartLeft, StartBridge):-
    valid_state(state(StartLeft, StartBridge)),

    sort(StartLeft, SortedStertLeft),
    all(All),
    allsafe(SortedStertLeft),
    subtract(All, SortedStertLeft, StartRight),
    allsafe(StartRight),

    path(state(SortedStertLeft, StartBridge), [], Steps),
    (format('~nSolution:~n'), forall(member(Step, Steps), printStep(Step))).
