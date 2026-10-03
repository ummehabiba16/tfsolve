---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Decision-theoretic agent: (1) update the belief state from the last action and the current percept; (2) for each action, compute the probabilities of its outcomes given the belief state and the action, and the expected utility; (3) select the action with maximum expected utility. Converting a multiply connected network to a singly connected one (a polytree is already singly connected): clustering (join tree), i.e. merge nodes on undirected cycles into meganodes, e.g. Sprinkler and Rain into Spr+Rain in the sprinkler network."
sources: ["AIMA 3e sec. 13.1.3 (DT-AGENT, Fig. 13.1), sec. 14.4.4 (clustering)"]
---
**Steps of a decision-theoretic agent** (AIMA's DT-AGENT):

```text
function DT-AGENT(percept) returns an action
    persistent: belief_state, probabilistic beliefs about the current state of the world
                action, the agent's action
    update belief_state based on action and percept
    calculate outcome probabilities for actions,
        given action descriptions and current belief_state
    select action with highest expected utility,
        given probabilities of outcomes and utility information
    return action
```

1. **Update the belief state:** combine the previous belief, the last action (transition model) and the new percept (sensor model) into a probability distribution over the current world states.
2. **Predict outcomes:** for each available action, compute $P(\text{Result}(a)=s'\mid\mathbf{e},a)$.
3. **Choose by maximum expected utility:** $a^*=\arg\max_a\sum_{s'}P(s'\mid a,\mathbf{e})\,U(s')$.

**Polytree and singly connected tree.** A polytree *is* a singly connected network: at most one undirected path between any two nodes. The conversion the question means is from a **multiply connected** network **into** a singly connected one (a polytree), so that the linear-time polytree algorithm can be used. This is done by **clustering (join-tree) algorithms**: nodes lying on undirected cycles are merged into **meganodes**, whose values are the combinations of the merged variables, until no undirected cycle remains.

*Example:* the sprinkler network $Cloudy\to Sprinkler$, $Cloudy\to Rain$, $Sprinkler\to WetGrass\leftarrow Rain$ has the cycle $Cloudy$, $Sprinkler$, $WetGrass$, $Rain$. Merging $Sprinkler$ and $Rain$ into one node $Spr{+}Rain$ with 4 values (tt, tf, ft, ff) gives the chain $Cloudy\to Spr{+}Rain\to WetGrass$, a polytree. The meganode's CPT is $P(S,R\mid C)=P(S\mid C)P(R\mid C)$, and $WetGrass$'s CPT is indexed by the meganode's values.
