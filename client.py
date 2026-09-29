"""Parallel Subtask Wavefront Scheduler.
100% Python Standard Library.
"""

from collections import defaultdict

class WavefrontScheduler:
    """Partitions DAG tasks into concurrent wavefront execution stages."""
    @staticmethod
    def build_wavefronts(tasks: list, dependencies: dict) -> list:
        task_level = {}
        for _ in range(len(tasks) + 1):
            changed = False
            for t in tasks:
                prereqs = dependencies.get(t, [])
                if not prereqs:
                    if t not in task_level:
                        task_level[t] = 0
                        changed = True
                else:
                    if all(p in task_level for p in prereqs):
                        level = max(task_level[p] for p in prereqs) + 1
                        if task_level.get(t) != level:
                            task_level[t] = level
                            changed = True
            if not changed:
                break

        levels = defaultdict(list)
        for t, lvl in task_level.items():
            levels[lvl].append(t)

        wavefronts = []
        for lvl in sorted(levels.keys()):
            wavefronts.append({
                "stage": lvl,
                "parallel_tasks": sorted(levels[lvl])
            })
        return wavefronts
