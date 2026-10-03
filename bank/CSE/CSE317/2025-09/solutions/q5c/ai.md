---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "pi*(s) = argmax_a sum P(s'|s,a) U(s'). Rover at (3,1): Left (0.651 > Up 0.632). Policy: (1,1) Up, (1,2) Up, (1,3) Right, (2,3) Right, (3,3) Right, (3,2) Up, (2,1) Left, (3,1) Left, (4,1) Left."
sources: ["MNM slides MDP-1-SB (optimal action, Bellman equation)", "AIMA 4e sec. 17.1, Fig. 17.2-17.3 (4x3 world)"]
---
**Set-up.** Cells are $(x,y)$, with column $x=1..4$ and row $y=1..3$. $(2,2)$ is a wall, and $(4,3)=+1$ and $(4,2)=-1$ are terminal. The rover is at $(3,1)$. An action moves in the intended direction with probability 0.8, and at $\pm 90^\circ$ with probability 0.1 each. Bumping into a wall or the edge leaves the rover where it is. The given numbers are the optimal utilities $U(s)$.

Once $U$ is known, the optimal policy is one step of look-ahead (MEU):

$$\pi^*(s)=\arg\max_{a}\sum_{s'}P(s'\mid s,a)\,U(s').$$

Every term $R(s)=-0.04$ is the same for all actions, so it does not affect the arg max.

**Rover's cell $(3,1)$.** Neighbours: up $(3,2)=0.660$, left $(2,1)=0.655$, right $(4,1)=0.388$; down is the edge, so the rover stays at $0.611$.

$$\text{Up}:\;0.8(0.660)+0.1(0.655)+0.1(0.388)=0.632$$

$$\text{Left}:\;0.8(0.655)+0.1(0.660)+0.1(0.611)=0.651$$

$$\text{Right}:\;0.8(0.388)+0.1(0.660)+0.1(0.611)=0.438$$

$$\text{Down}:\;0.8(0.611)+0.1(0.655)+0.1(0.388)=0.593$$

$\pi^*(3,1)=$ **Left**. Going Up is shorter, but it passes next to the $-1$ cell; Left takes the long, safe way round.

**Four more cells.**

$(1,1)$, with neighbours $(1,2)=0.762$, $(2,1)=0.655$ and itself $0.705$:

$$\text{Up}=0.8(0.762)+0.1(0.705)+0.1(0.655)=0.746$$

$$\text{Right}=0.8(0.655)+0.1(0.762)+0.1(0.705)=0.671$$

Left $=0.711$ and Down $=0.700$, so $\pi^*(1,1)=$ **Up**.

$(3,2)$, with neighbours $(3,3)=0.918$, $(3,1)=0.611$, $(4,2)=-1$ and the wall (stay, $0.660$):

$$\text{Up}=0.8(0.918)+0.1(0.660)+0.1(-1)=0.700$$

$$\text{Left}=0.8(0.660)+0.1(0.918)+0.1(0.611)=0.681$$

$$\text{Right}=0.8(-1)+0.1(0.918)+0.1(0.611)=-0.647$$

Down $=0.455$, so $\pi^*(3,2)=$ **Up**.

$(3,3)$, with neighbours $(4,3)=+1$, $(2,3)=0.868$, $(3,2)=0.660$ and the edge (stay, $0.918$):

$$\text{Right}=0.8(1)+0.1(0.918)+0.1(0.660)=0.958$$

$$\text{Up}=0.8(0.918)+0.1(0.868)+0.1(1)=0.921$$

Left $=0.852$ and Down $=0.715$, so $\pi^*(3,3)=$ **Right**.

$(4,1)$, with neighbours $(4,2)=-1$, $(3,1)=0.611$ and the edge (stay, $0.388$):

$$\text{Left}=0.8(0.611)+0.1(-1)+0.1(0.388)=0.428$$

$$\text{Up}=0.8(-1)+0.1(0.611)+0.1(0.388)=-0.700$$

Down $=0.410$ and Right $=0.249$, so $\pi^*(4,1)=$ **Left**.

**Optimal policy** (the same computation for the remaining cells gives $(1,2)$ Up, $(1,3)$ Right, $(2,3)$ Right, $(2,1)$ Left):

| Row | Col 1 | Col 2 | Col 3 | Col 4 |
|:-:|:-:|:-:|:-:|:-:|
| 3 | $\rightarrow$ | $\rightarrow$ | $\rightarrow$ | +1 |
| 2 | $\uparrow$ | wall | $\uparrow$ | $-1$ |
| 1 | $\uparrow$ | $\leftarrow$ | $\leftarrow$ (rover) | $\leftarrow$ |

*Check:* the utilities satisfy the Bellman equation $U(s)=-0.04+\max_a\sum_{s'}P(s'\mid s,a)U(s')$ with $\gamma=1$. For example, $U(3,1)=-0.04+0.651=0.611$. This is AIMA's 4$\times$3 world (Fig. 17.2(a)).
