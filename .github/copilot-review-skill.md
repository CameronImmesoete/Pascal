# Code Review Standards

> Base review standards: [CameronImmesoete/.github/.github/copilot-review-skill.md@1f79bfb](https://github.com/CameronImmesoete/.github/blob/1f79bfb3e9eee277d05ecdd3332220204cb0f38b/.github/copilot-review-skill.md)

## Repository-Specific Review Criteria

### Algorithm Correctness
- Pascal's triangle values match binomial coefficients
- Each row sum equals 2^n
- Symmetry property: C(n,k) = C(n,n-k)
- Edge values are always 1

### Edge Cases
- Row 0 returns [1]
- Negative row numbers rejected with clear error
- Large row numbers: integer overflow handling
- Input validation (non-negative integers only)
