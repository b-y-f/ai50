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
P(defective \cap by A) = 0.6 \cdot 0.02 = 0.012
$$

# Quiz3

For which of the following will you always find the same solution, even if you re-run the algorithm multiple times?

> Assume a problem where the goal is to minimize a cost function, and every state in the state space has a different cost.

- Steepest-ascent hill-climbing, each time starting from a different starting state
- __Steepest-ascent hill-climbing, each time starting from the same starting state__
- Stochastic hill-climbing, each time starting from a different starting state
- Stochastic hill-climbing, each time starting from the same starting state
- Both steepest-ascent and stochastic hill climbing, so long as you always start from the same starting state
- Both steepest-ascent and stochastic hill climbing, each time starting from a different starting state
- No version of hill-climbing will guarantee the same solution every time


__Note__: Stepest-ascent hill-climbing only compare `max` values, stochastic hill climbing will pick any random higher neighbors.

---

The following two questions will both ask you about the optimization problem described below.

<blockquote>
A farmer is trying to plant two crops, Crop 1 and Crop 2, and wants to maximize his profits. The farmer will make $500 in profit from each acre of Crop 1 planted, and will make $400 in profit from each acre of Crop 2 planted. 

However, the farmer needs to do all of his planting today, during the 12 hours between 7am and 7pm. Planting an acre of Crop 1 takes 3 hours, and planting an acre of Crop 2 takes 2 hours.

The farmer is also limited in terms of supplies: he has enough supplies to plant 10 acres of Crop 1 and enough supplies to plant 4 acres of Crop 2.

Assume the variable C1 represents the number of acres of Crop 1 to plant, and the variable C2 represents the number of acres of Crop 2 to plant.
</blockquote>


What would be a valid objective function for this problem?

__500 * C1 + 400 * C2__

What are the constraints for this problem?

__3 * C1 + 2 * C2 <= 12, C1 <= 10, C2 <= 4__

---

The following question will ask you about the below exam scheduling constraint satisfaction graph, where each node represents a course. Each course is associated with an initial domain of possible exam days (most courses could be on Monday, Tuesday, or Wednesday; a few are already restricted to just a single day). An edge between two nodes means that those two classes must have exams on different days.

![](https://lh5.googleusercontent.com/z86itmjSWrW0n50XbsLxSCsBepJUq9WW4w6fqMWVgYX9yeFlnHHtlv529qaCCRsuP-0SkxKi-qx2yFd3RWHUH7BWUU3w3fsEF6_g_ByxTfi6uKgcN7jD8yNbgoS3fyLN4g=w1920)

After enforcing arc consistency on this entire problem, what are the resulting domains for the variables C, D, and E?

- __C's domain is {Mon}, D's domain is {Mon, Wed}, E's domain is {Tue, Wed}__
- C's domain is {Mon, Tue, Wed}, D's domain is {Mon, Wed}, E's domain is {Mon, Tue, Wed}
- C's domain is {Mon, Tue}, D's domain is {Wed}, E's domain is {Mon}
- C's domain is {Mon}, D's domain is {Wed}, E's domain is {Tue}
- C's domain is {Mon}, D's domain is {Mon, Wed}, E's domain is {Mon, Tue, Wed}
- C's domain is {Mon}, D's domain is {Tue}, E's domain is {Wed}

__Note__: Just prune element until everything along "edge" different.

---


# Quiz 4

Categorize the following as supervised learning, reinforcement learning, unsupervised learning, or not machine learning: __A social network’s AI uses existing tagged photos of people to identify when those people appear in new photos.__

Answer: Supervised learning

---

Imagine a regression AI that makes the following predictions for the following 5 data points. What is the total L2 loss across all of these data points (i.e., the sum of all the individual L2 losses for each data point)?

>For data point 1, the true output is 2 and the AI predicted 4. For data point 2, the true output is 4 and the AI predicted 5. For data point 3, the true output is 4 and the AI predicted 3. For data point 4, the true output is 5 and the AI predicted 2. For data point 5, the true output is 6 and the AI predicted 5.

Answer: 16

__Note__: From L2 function $L =\sum(actual - pred)^{2}$, answer can be easily calcualted.

---

If Hypothesis 1 has a lower L1 loss and a lower L2 loss than Hypothesis 2 on a set of training data, why might Hypothesis 2 still be a preferable hypothesis?

- Hypothesis 1 might be the result of loss.
- Hypothesis 1 might be the result of cross-validation.
- Hypothesis 1 might be the result of regularization.
- __Hypothesis 1 might be the result of overfitting.__
- Hypothesis 1 might be the result of regression.

---

In the ε-greedy approach to action selection in reinforcement learning, which of the following values of ε makes the approach identical to a purely greedy approach?

Answer: 0 

__Note__:ε is how offen we want move randomly. By defination : __A greedy algorithm is an approach for solving a problem by selecting the best option available at the moment.__ 1 - ε is to choice best move.


---

# Quiz 5

The following question will ask you about the below neural network, where we set w0 = -5, w1 = 2, w2 = -1, and w3 = 3. x1, x2, and x3 represent input neurons, and y represents the output neuron.

![](https://lh5.googleusercontent.com/Dl-kkbtyDwzkACM2teVcOM49UeAj14e-h9ducd3D8gp3ljTN1SDfC8MP2lrvNcLA0rxQbgd5-DWefDINKnaWwNEI_y_Qq6FVHj3BVeW-0xej8f1IYeBLjeELHaym1vR-yQ=w699)


What value will this network compute for y given inputs x1 = 3, x2 = 2, and x3 = 4 if we use a step activation function? What if we use a ReLU activation function?

A: 1 for step activation function, 11 for ReLU activation function


---


How many total weights (including biases) will there be for a fully connected neural network with a single input layer with 3 units, a single hidden layer with 5 units, and a single output layer with 4 units?

A: $3 \cdot 5 + 5 + 5 \cdot 4 + 4 = 44$

---

Consider a recurrent neural network that listens to a audio speech sample, and classifies it according to whose voice it is. What network architecture is the best fit for this problem?

A: Many-to-one (multiple inputs, single output)

__Note__: Since audio speed is a sequence of information, we can use it frame by frame as input to NN, and learn more information from previous model. In the end we will identify who the audio belongs to which person. 

---

The following question will ask you about a 4x4 grayscale image with the following pixel values.


![](https://lh6.googleusercontent.com/PCvuuTr6WMg518wI5x9AVJy6F0EspzWz6oJEpN_NpL6zQovHyZyOYxCnbj7yLwFf5-mSMWR0fElswujbZF4ZFDBZCXBSnb75-SPcy4_HOZuWmoejKQhXE8hveLclzjAoqQ=w319)

What would be the result of applying a 2x2 max-pool to the original image?

> Answers are formatted as a matrix [[a, b], [c, d]] where [a, b] is the first row and [c, d] is the second row.

A: [[16, 12], [32, 28]]

__Note__: ![](https://media.geeksforgeeks.org/wp-content/uploads/20190721025744/Screenshot-2019-07-21-at-2.57.13-AM.png)

---

Quiz 6

The following question will ask you about the below context-free grammar, where S is the start symbol.

![](https://lh4.googleusercontent.com/ZBC2-UH01Ww9_9wyPi04trSSMAPiLXZA5mRV7q-gW27I7grMhZ4uH0pb5mK_oY2YpPL7mj5jmUCb_aqbC2zT5MFxHqUSLWF6TLKbbV7PatJYwkLGJ89UJ83Jnj1lXIj18g=w578)

The following question will also ask you about the following four sentences.
- Sentence 1: Cats run.
- Sentence 2: Cats climb trees.
- Sentence 3: Small cats run.
- Sentence 4: Small white cats climb.

Of the four sentences above, which sentences can be derived from the above context-free grammar?

- Only Sentence 1
- Only Sentence 1 and Sentence 2
- Only Sentence 1 and Sentence 3
- Only Sentence 1 and Sentence 4
- Only Sentence 1, Sentence 2, and Sentence 3
- Only Sentence 1, Sentence 2, and Sentence 4
- __Only Sentence 1, Sentence 3, and Sentence 4__
- All four sentences
- None of the four sentences

__Note__: 

- s1 = NP(N) V (ok)
- s2 = NP V N (wrong)
- s3 = NP(A N) V (ok)
- s4 = A A N(NP) V (ok)

---

The following question will ask you about a corpus with the following documents.

- Document 1: a a b c
- Document 2: a c c c d e f
- Document 3: a c d d d
- Document 4: a d f

What is the tf-idf value for "d" in Document 3?

> Round answers to two decimal places. Use the natural logarithm (log base e) when taking a logarithm.

$$
tf = \frac{3}{5}\\
idf = \ln{\frac{4}{3}} \\
tf \cdot idf \approx 0.17
$$

__Note__: Answer might got problem!

---

Why is "smoothing" useful when applying Naive Bayes?

- Smoothing allows Naive Bayes to be less "naive" by not assuming that evidence is conditionally independent.
- Smoothing allows Naive Bayes to turn a conditional probability of evidence given a category into a probability of a category given evidence.
- __Smoothing allows Naive Bayes to better handle cases where evidence has never appeared for a particular category.__
- Smoothing allows Naive Bayes to better handle cases where there are many categories to classify between, instead of just two.

---

From the phrase "must be the truth", how many word n-grams of length 2 can be extracted?

A: 3