# COMP 433

## Requirements
- Everything is defined using `uv` in `pyproject.toml`.
- Only `python==3.9.13` was locked from the source repo. `numpy` and `tqdm`, and `torch` were version-resolved.
- `torch`'s wheels are resolved to PyPI rather than PyTorch's dedicated index. PyPI only includes GPU-accelerated wheels for Linux, while Windows and macOS use CPU-only wheels.

## Changes to source
See `fix(RAFT)` commits

## Running
All commands should be ran from within `./RAFT/`, even if the virtual env is in root.
- `cd ./RAFT`
- `uv run run.py --data ETTm1 --data_path ETTm1.csv`