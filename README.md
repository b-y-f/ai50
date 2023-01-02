# Quiz 0

Between depth first search (DFS) and breadth first search (BFS), which will find a shorter path through a maze?

- DFS will always find a shorter path than BFS
- BFS will always find a shorter path than DFS
- DFS will sometimes, but not always, find a shorter path than BFS
- __BFS will sometimes, but not always, find a shorter path than DFS__
- Both algorithms will always find paths of the same length

__Note__: In `degrees` project, we will find the shortest path, understand this could help solve that project easier.

---

The following question will ask you about the below maze. Grey cells indicate walls. A search algorithm was run on this maze, and found the yellow highlighted path from point A to B. In doing so, the red highlighted cells were the states explored but that did not lead to the goal.
![](https://lh4.googleusercontent.com/J_8Pjw1vZv18-YU5Yhqeu2KyS5pGR5QlPBB29TeBPsM4Rz28QjAN_sAMfi4EKK34mTOkXc7zWa5_eMoJz0e6JXIJLO4uWtuWBFGwni-7hby5iZzpUyh9zYgiK5vEmURLYA=w571)


Of the four search algorithms discussed in lecture — depth-first search, breadth-first search, greedy best-first search with Manhattan distance heuristic, and A* search with Manhattan distance heuristic — which one (or multiple, if multiple are possible) could be the algorithm used?

- Could only be A*
- Could only be greedy best-first search
- __Could only be DFS__ 
- Could only be BFS
- Could be either A* or greedy best-first search
- Could be either DFS or BFS
- Could be any of the four algorithms
- Could not be any of the four algorithms

__Note:__ This one is bit tricky, we can first exclude greedy BF and A* since in the second fork road of the maze, the shortest and optimzed road is __going up__, but actually the path is __going down__. Then if it is BFS, it will continues explore in second fork road, so excluded. 

---

Why is depth-limited minimax sometimes preferable to minimax without a depth limit?
 
- __Depth-limited minimax can arrive at a decision more quickly because it explores fewer states__
- Depth-limited minimax will achieve the same output as minimax without a depth limit, but can sometimes use less memory
- Depth-limited minimax can make a more optimal decision by not exploring states known to be suboptimal
- Depth-limited minimax is never preferable to minimax without a depth limit

---

The following question will ask you about the Minimax tree below, where the green up arrows indicate the MAX player and red down arrows indicate the MIN player. The leaf nodes are each labelled with their value.

![](https://lh6.googleusercontent.com/hgd-oC-sTrXfCzfvK2jVpAmQQ6kZ8THvcqKWPUd5ega7Q0Z5zvKqXdseQtujdwElKiJinmYOqJFNFztJMorr0LqfO8QCzw9UReF8RuhVpRYAcS3V408CgdRwUs17PKBZxg=w740)

What is the value of the root node? 
5

---

# Quiz1

The following question will ask you about the following logical sentences.
1. If Hermione is in the library, then Harry is in the library.
2. Hermione is in the library.
3. Ron is in the library and Ron is not in the library.
4. Harry is in the library.
5. Harry is not in the library or Hermione is in the library.
6. Ron is in the library or Hermione is in the library.

Which of the following logical entailments is true?

- Sentence 6 entails Sentence 3 x 
- Sentence 6 entails Sentence 2 x
- __Sentence 2 entails Sentence 5 2:T => 5:T/F or T => T__
- Sentence 1 entails Sentence 4 x
- Sentence 5 entails Sentence 6 x
- Sentence 1 entails Sentence 2 x

__Note__: _"entile"_ means if $\alpha$ is `True` then $\beta$ also true.

Can be represented as : $\alpha\models \beta$


---

There are other logical connectives that exist, other than the ones discussed in lecture. One of the most common is "Exclusive Or" (represented using the symbol ⊕). The expression A ⊕ B represents the sentence "A or B, but not both." Which of the following is logically equivalent to A ⊕ B?

- (A ∧ B) ∨ ¬ (A ∨ B)
- __(A ∨ B) ∧ ¬ (A ∧ B)__
- (A ∨ B) ∧ (A ∧ B)
- (A ∨ B) ∧ ¬ (A ∨ B)

__Note__:

```python
# (A ∧ B) ∨ ¬ (A ∨ B)
def t1(a,b):
    return (a and b) or not (a or b)

# (A ∨ B) ∧ ¬ (A ∧ B)
def t2(a,b):
    return (a or b) and not (a and b)

# (A ∨ B) ∧ (A ∧ B)
def t3(a,b):
    return (a or b) and (a and b)

# (A ∨ B) ∧ ¬ (A ∨ B)
def t4(a,b):
    return (a or b) and not (a or b)

A = [True, False]
B = [True, False]

for i in A:
    for j in B:
        # print(i,j,t1(i,j))
        print(i,j,t2(i,j))
        # print(i,j,t3(i,j))
        # print(i,j,t4(i,j))
```

---


Let propositional variable R be that "It is raining," the variable C be that "It is cloudy," and the variable S be that "It is sunny." Which of the following a propositional logic representation of the sentence "If it is raining, then it is cloudy and not sunny."?

- (R → C)  ∧ ¬S
- R → C  → ¬S
- R ∧ C  ∧ ¬S
- __R → (C  ∧ ¬S)__
- (C ∨ ¬S) → R

---

Consider, in first-order logic, the following predicate symbols. Student(x) represents the predicate that "x is a student." Course(x) represents the predicate that "x is a course." Enrolled(x, y) represents the predicate that "x is enrolled in y." Which of the following is a first-order logic translation of the sentence "There is a course that Harry and Hermione are both enrolled in."?

- ∀x. Enrolled(Harry, x) ∧ ∀y. Enrolled(Hermione, y)
- ∀x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)
- ∀x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)
- __∃x. Course(x) ∧ Enrolled(Harry, x) ∧ Enrolled(Hermione, x)__
- ∃x. Enrolled(Harry, x) ∨ Enrolled(Hermione, x)
- ∃x. Enrolled(Harry, x) ∧ ∃y. Enrolled(Hermione, y)

__Note__:∃x is existential quantification: there __exist an__ object x. ∀x is universal Quantification for __all__ object of x. 

---

# Quiz2

Consider a standard 52-card deck of cards with 13 card values (Ace, King, Queen, Jack, and 2-10) in each of the four suits (clubs, diamonds, hearts, spades). If a card is drawn at random, what is the probability that it is a spade or a two?

>Note that "or" in this question refers to inclusive, not exclusive, or.

__Note__: Let $A$ represent event of possiblilty get spade, $B$ is event get number two, $A$ and $B$ both __not mutually exclusive__:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)\\
= 1/4 + 1/13 - 1/52 \approx 0.308
$$

---

Imagine flipping two fair coins, where each coin has a Heads side and a Tails side, with Heads coming up 50% of the time and Tails coming up 50% of the time. What is probability that after flipping those two coins, one of them lands heads and the other lands tails?

1/2

---

The following question will ask you about the Bayesian Network shown in lecture, reproduced below.

![](https://lh4.googleusercontent.com/6aw76BG0O9NT3HroqN_aW8Q6MRq1gN4RG8U0r_JHJTidIHRQ2Do_GfZh7R39Uai2Hsh6Oa1uOGXT60p3wJbjRq8hfhlVqOnnG4zk7AkYObf_Q4h6QD5_WARYeRsiLPAc1w=w520)

Which of the following sentences is true?

- Assuming we know the train is on time, whether or not there is rain affects the probability that the appointment is attended.
- Assuming we know there is track maintenance, whether or not there is rain does not affect the probability that the appointment is attended.
- Assuming we know there is rain, whether or not there is track maintenance does not affect the probability that the train is on time.
- __Assuming we know the train is on time, whether or not there is track maintenance does not affect the probability that the appointment is attended.__
- Assuming we know there is track maintenance, whether or not there is rain does not affect the probability that the train is on time.

---

Two factories — Factory A and Factory B — design batteries to be used in mobile phones. Factory A produces 60% of all batteries, and Factory B produces the other 40%. 2% of Factory A's batteries have defects, and 4% of Factory B's batteries have defects. What is the probability that a battery is both made by Factory A and defective?

$$
P(defective \cap by A) = 0.6 \cdot 0.04 = 0.0024
$$
