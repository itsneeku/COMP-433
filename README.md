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
- `uv run run.py --data ETTm2 --data_path ETTm2.csv`
- `uv run run.py --data ETTh1 --data_path ETTh1.csv`
- `uv run run.py --data ETTh2 --data_path ETTh2.csv`
- `uv run run.py --data custom --data_path exchange_rate.csv --enc_in 8 --dec_in 8 --c_out 8`
- `uv run run.py --data custom --data_path ecommerce.csv --enc_in 6 --dec_in 6 --c_out 6 --freq d --seq_len 24 --label_len 12 --pred_len 24`