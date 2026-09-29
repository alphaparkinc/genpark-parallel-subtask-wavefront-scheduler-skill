from client import WavefrontScheduler

tasks = ["init", "fetch_a", "fetch_b", "process"]
deps = {"fetch_a": ["init"], "fetch_b": ["init"], "process": ["fetch_a", "fetch_b"]}
wf = WavefrontScheduler.build_wavefronts(tasks, deps)
print("Parallel Wavefronts:", wf)
