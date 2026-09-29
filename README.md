# genpark-parallel-subtask-wavefront-scheduler-skill

Wavefront parallel execution scheduler grouping interdependent DAG agent tasks into concurrent stages.

## Architecture

```mermaid
flowchart TD
    Init[Stage 0: Init] --> SubA[Stage 1: Worker A]
    Init --> SubB[Stage 1: Worker B]
    Init --> SubC[Stage 1: Worker C]
    SubA --> Agg[Stage 2: Aggregate]
    SubB --> Agg
    SubC --> Agg
```

## Features
- **Maximized Concurrency**: Identifies all tasks whose prerequisites are complete.
- **Stage Isolation**: Enforces synchronization barriers between wavefronts.
