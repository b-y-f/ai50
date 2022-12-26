# Quiz 0

Between depth first search (DFS) and breadth first search (BFS), which will find a shorter path through a maze?

- DFS will always find a shorter path than BFS
- BFS will always find a shorter path than DFS
- DFS will sometimes, but not always, find a shorter path than BFS
- __BFS will sometimes, but not always, find a shorter path than DFS__
- Both algorithms will always find paths of the same length

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

