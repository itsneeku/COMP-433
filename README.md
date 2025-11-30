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
- `uv run run.py --data custom --root_path ./data/solar-energy/ --data_path Alabama_137_Plants_2006.csv --features M --target "0" --freq t --embed timeF --num_workers 0 --enc_in 137 --dec_in 137 --c_out 137 --d_model 128 --d_ff 256 --batch_size 16 --n_period 2 --model_id Solar_Alabama_Run2`
-  `uv run run.py --data custom --root_path ./data/weather/ --data_path weather_2024.csv --model_id Weather_Paper_Reproduction --model RAFT --data custom --features M --target "T (degC)" --freq t --embed timeF --num_workers 0 --seq_len 720 --label_len 360 --pred_len 96 --e_layers 2 --d_layers 1 --factor 1 --enc_in 21 --dec_in 21 --c_out 21 --d_model 512 --d_ff 2048 --n_heads 8 --top_k 1 --des 'Exp' --learning_rate 0.01 --batch_size 32`
