# Concepts

Short reference notes explaining the ideas behind the practices: the mechanisms, the evidence, and what's still unsolved.

- [Cache economics & whole-bill anatomy](cache-economics-and-whole-bill-anatomy.md) - the ~10x cache-read discount, what breaks it, and what a token-only meter misses.
- [Compaction economics](compaction-economics.md) - why compacting a context window is a costed, harness-designed operation, not a free safety valve.
- [Model economics](model-economics.md) - why per-token price barely predicts per-task cost, and how to pick the right-sized model.
- [Orchestration economics](orchestration-economics.md) - the coordination tax multi-agent systems pay that nobody has reliably measured.
- [Whole-bill reconciliation](whole-bill-reconciliation.md) - why calculated spend and the actual provider invoice are different numbers, and what closing that gap requires.
- [Harness-waste taxonomy & sizing](harness-waste-taxonomy.md) - ten known types of fixable-without-a-better-model spend, each with its mechanism and published size.
- [Measuring capability-limit vs harness-waste](measuring-capability-vs-harness-waste.md) - what's proven and what's still open in separating model-forced spend from fixable harness spend.
- [Per-session waste attribution](per-session-waste-attribution-methods.md) - a five-rung ladder of methods for reading waste out of one live session transcript, and why the top rung is still empty.
- [The harness as a learnable object](harness-as-learnable-object.md) - a 2026 research wave treating the agent harness itself, not the model, as what to optimize.
- [The case against the thesis (steelman)](case-against-the-thesis.md) - the strongest evidence-backed argument that honest whole-bill measurement isn't a defensible bet, and where it survives.
