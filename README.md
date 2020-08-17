### Motivation
- This repo is created to test whether some soft actor critic implementations suffers from maximization bias. 
- The original paper states that two independent q-tables are used to benefit training large and complex tasks.
- But in practice many did not use the idea of decoupling q-value selection and q-value update in many SAC implementations, it seems.
- So I'm trying to figure out how well those algorithms does at Sutton's RL book figure 6.5, the maximiation bias example. 
### Description
- Basically, we start in state A and if we move to state B, we have many choices.
- Each choice in state B leads to a terminal state, at which the agent gains a reward with a mean of -0.1 and variance of a customized value. (A value of 2 proved that one of the SAC implmentations suffer from maximization bias.)
- But there is another move that will always return zero and end the episode at state A, and eventually a successful agent should prefer that.
- In a simple (non-deep) RL case, Sutton demonstrated the advantage of double q-learning over single q-learning using this enviornment.
- If a SAC implementation fails in this example, I do not know any good fix that gets the benefit from "both worlds", that is the benefit from SAC and avoiding maximization bias. This is essentially a dependency problem. But I believe with more efforts and more data structures it can be solved in a rather straightforward fashion, pretty much like the many complex momentum and importance resampling methods in RL. 
### Note
- All of these should be taken with a grain of salt. Some of the implementations I wanted to test are really mature. And I could be totally wrong. This is just out of curiosity and gaining a deeper understanding of the inner workings of some of these algorithms and their implementations.