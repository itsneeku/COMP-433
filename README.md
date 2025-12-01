# COMP 433

# Team Members
Youssef Ouakaa (40157718) 

Gabriel Asencios (40176253) 

Nicolae Rusu (40245233) 

Ryan Mazari (40241379)


## Project Description

This project implements and evaluates the **Retrieval-Augmented Forecasting of Time-series (RAFT)** model for long-term time series forecasting. We conducted experiments on multiple benchmark datasets (ETT, exchange rate, solar energy, weather) and one custom dataset (e-commerce). Our work involved adapting the RAFT implementation, creating preprocessing pipelines, and evaluating model performance across different forecasting configurations. For detailed methodology and results, refer to our final paper.

## Requirements

- **Python 3.9.13** (required)
- All dependencies are defined using `uv` in `pyproject.toml`. Key libraries: PyTorch (>=2.8.0), NumPy, Pandas, scikit-learn, sktime, matplotlib, tqdm
- Install dependencies: `uv sync`
- **Note:** `torch` wheels are resolved from PyPI. GPU-accelerated wheels are only available for Linux on PyPI. Windows and macOS use CPU-only wheels.

## Source Code Package

The PyTorch source code is organized in the `RAFT/` directory:

- `RAFT/models/RAFT.py` - Main RAFT model
- `RAFT/layers/Retrieval.py` - Retrieval mechanism
- `RAFT/exp/exp_long_term_forecasting.py` - Training and evaluation
- `RAFT/data_provider/` - Data loading utilities
- `RAFT/utils/` - Utility functions
- `RAFT/run.py` - Main entry point
- `preprocessors/` - Dataset preprocessing scripts

## Dataset Download

### ETT Datasets

ETT datasets (ETTh1, ETTh2, ETTm1, ETTm2) should be placed in `RAFT/data/ETT/`. Download from: [ETDataset repository](https://github.com/zhouhaoyi/ETDataset)

### Other Datasets

For download links to other benchmark datasets (exchange rate, solar energy, weather) and the custom e-commerce dataset, refer to our final paper. These datasets should be placed according to the path passed in the commands.

## Running commands

All commands should be run from within `./RAFT/` directory:

```bash
cd ./RAFT
```

### Training Examples

```bash
# ETT benchmarks
uv run run.py --data ETTm1 --data_path ETTm1.csv
uv run run.py --data ETTm2 --data_path ETTm2.csv
uv run run.py --data ETTh1 --data_path ETTh1.csv
uv run run.py --data ETTh2 --data_path ETTh2.csv

# Other benchmarks
uv run run.py --data custom --data_path exchange_rate.csv --enc_in 8 --dec_in 8 --c_out 8
uv run run.py --data custom --root_path ./data/solar-energy/ --data_path Alabama_137_Plants_2006.csv --features M --target "0" --freq t --embed timeF --num_workers 0 --enc_in 137 --dec_in 137 --c_out 137 --d_model 128 --d_ff 256 --batch_size 16 --n_period 2 --model_id Solar_Alabama_Run2
uv run run.py --data custom --root_path ./data/weather/ --data_path weather_2024.csv --model_id Weather_Paper_Reproduction --model RAFT --data custom --features M --target "T (degC)" --freq t --embed timeF --num_workers 0 --seq_len 720 --label_len 360 --pred_len 96 --e_layers 2 --d_layers 1 --factor 1 --enc_in 21 --dec_in 21 --c_out 21 --d_model 512 --d_ff 2048 --n_heads 8 --top_k 1 --des 'Exp' --learning_rate 0.01 --batch_size 32

# Custom e-commerce dataset
uv run run.py --data custom --data_path ecommerce.csv --enc_in 6 --dec_in 6 --c_out 6 --freq d --seq_len 24 --label_len 12 --pred_len 24
```

During training, the model automatically validates and tests. Results are saved in `./RAFT/results/`, and `./RAFT/test_results/`.

## Changes to source

See `fix(RAFT)` commits
