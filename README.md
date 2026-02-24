Weighted Boolean Threshold Decomposition
A Structural Approach to Order Statistics
Overview

This repository presents a structural framework for computing order statistics using threshold-based Boolean decomposition. The method reformulates classical selection problems—such as median, weighted median, and nth-order statistics—through vertical dominance layers defined over the value domain.

Instead of relying exclusively on positional indexing or partition-based recursion, the approach decomposes the dataset across discrete thresholds and evaluates dominance structure at each level. Order statistics emerge from cumulative dominance behavior rather than index selection alone.

The implementation accompanies a formal IEEE-formatted thesis that provides proofs, theoretical grounding, and analytical evaluation.

Conceptual Foundation

Let 
𝐴
=
{
𝑎
1
,
…
,
𝑎
𝑁
}
A={a
1
	​

,…,a
N
	​

} be a finite set of ordered values.
For each threshold 
𝑡
t, define:

𝐵
𝑡
(
𝑖
)
=
{
1
	
if 
𝑎
𝑖
≥
𝑡


0
	
otherwise
B
t
	​

(i)={
1
0
	​

if a
i
	​

≥t
otherwise
	​


Each threshold induces a Boolean dominance vector. The collection of such vectors across all relevant thresholds forms an implicit Boolean matrix that represents the vertical structure of the dataset.

Two core observations follow:

Order statistics correspond to structural transitions in dominance balance.

Weighted statistics correspond to cumulative mass crossings within these dominance layers.

This perspective transforms selection into a discrete integration problem over dominance strata.

Implemented Components
1. Weighted Boolean Matrix Trace

Sorts values while preserving associated weights.

Computes cumulative weight over threshold survival sets.

Identifies the weighted median as the first dominance level where cumulative mass exceeds half the total weight.

Provides trace output for structural inspection.

This formulation makes the weighted median equivalent to detecting a crossing in a discrete survival function.

2. Hybrid ADS Boolean Operator

The hybrid module generalizes threshold evaluation through rule-based activation:

Majority dominance (median)

P-th maximum condition

P-th minimum condition

Instead of selecting an index directly, the algorithm integrates rule activations across threshold widths. The resulting statistic is reconstructed from structural dominance intervals.

This creates a unified mechanism for multiple order-statistic types within a single Boolean framework.

Why This Matters

Classical approaches such as QuickSelect optimize positional selection but provide limited structural insight. The threshold-decomposition model emphasizes:

Deterministic behavior

Interpretability of dominance structure

Natural extension to weighted settings

Unified treatment of multiple selection rules

The method is particularly suitable for bounded integer domains or contexts where structural analysis is as important as computational efficiency.

Repository Structure
src/            Core algorithms
experiments/    Benchmark scripts
tests/          Unit validation
examples/       Minimal working demos
docs/           IEEE thesis (PDF)
Minimal Example
from src.weighted_median import weighted_boolean_matrix_trace

arr = [4, 5, 6, 7, 8]
weights = [3, 2, 4, 6, 5]

weighted_boolean_matrix_trace(arr, weights)
Complexity

Sorting: 
𝑂
(
𝑁
log
⁡
𝑁
)
O(NlogN)

Threshold scan: 
𝑂
(
𝑅
𝑁
)
O(RN)

Median detection: 
𝑂
(
𝑁
)
O(N)

Where 
𝑅
R is the value range.
For bounded domains, performance is predictable and stable.
