# Updated Guidelines & Reminders

## Key Announcements & Best Practices

1. **Up to 3 annotations per image**: 1 is minimum, 2 is strongly recommended, 3 is the hard maximum. If the model response box is empty, it's a technical issue (save, reload, escalate) — not a quality issue.
2. **~90% should have numeric answers (VQA only)**: Roughly 90% of VQA questions should include a number as an answer, and ideally the number is not visually present (e.g., a tick label) but inferred by following a multi-step reasoning process. This rule does NOT apply to BabyVision, where answers are regularly non-numeric (letters, grid coordinates, MCQ labels).
3. **When in doubt, reduce to one annotation**: If there is any doubt that two annotations on the same image may be similar (skills, visual element, or question shape), cut it down to one. Two strong annotations beat three mediocre ones, and one strong annotation beats two that overlap.
4. **Direct the model to find information — don't hand it over**: Don't provide information in the prompt when you can direct the model to find it in the image instead (e.g., naming the exact location bypasses visual reasoning).
5. **Ask the model to *do* something, not just observe (VQA)**: Avoid trivial counting and surface-level data extraction. Require the model to reason (compare, compute, infer, transform). "Observe X" is not a task; "use X to determine Y" is.
6. **Make sure the rewrite answer is correct**: Always triple-check the rewrite answer against the image before submitting. Answer correctness is a top audit failure mode. (Reviewers: Work through the prompt yourself before looking at the rewrite answer.)
