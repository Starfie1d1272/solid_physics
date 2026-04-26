# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Planetary Solid Physics (行星固体物理) course repository at Nanjing University. Each homework assignment is self-contained in its own directory (`HW1`–`HW4`).

## Project Structure

```
HW1/        — Gutenberg-Richter law analysis (standalone .py scripts)
HW2/        — Stress tensor & Coulomb Failure Function (standalone .py scripts)
HW3/        — Seismic waveform processing (Jupyter notebook, SAC data)
HW4/        — Mars inner core ray tracing & Earth-flattening transform (Jupyter notebooks)
HW5/        — Zoeppritz coefficients for SV wave incidence (Jupyter notebook)
```

Each HW typically has:
- Code (`.py` or `.ipynb`)
- `data/` — input data files
- `figures/` — output plots (PNG)
- `README.md` — context and run instructions
- Reports in Markdown/PDF

## Key Dependencies

- `numpy`, `pandas`, `matplotlib` — used across all assignments
- `obspy` (v1.5+) with `TauP` — used in HW3 (SAC I/O, instrument response, rotation) and HW4 (ray tracing, model compilation)
- `geopandas` + `cartopy` — used in HW1 (global earthquake mapping)
- `scipy` — used in HW4 (integration, root-finding, interpolation)

## Running Code

### Standalone Python scripts (HW1, HW2)
```bash
cd HW1 && python analysis.py
cd HW1 && python figures.py
cd HW2 && python text1.py
cd HW2 && python "text2(f).py"
cd HW2 && python "text2(g).py"
cd HW2 && python "text2(h).py"
```

### Jupyter notebooks (HW3, HW4)
```bash
cd HW3 && jupyter notebook hw3.ipynb
cd HW4 && jupyter notebook HW4_text1.ipynb
cd HW4 && jupyter notebook HW4_text2.ipynb
```

Or in VS Code: open the `.ipynb` file and run cells sequentially.

### Local Mac verification (miniforge/mamba)
```bash
cd ~/GitHub/solid_physics/HW5 && mamba run -n solid_physics python verify.py
```

### Remote Windows verification (SSH)
```bash
cd ~/GitHub/solid_physics/HW5 && ssh 192.168.144.2 "cd /d D:\GitHub\solid_physics\HW5 && C:\ProgramData\anaconda3\Scripts\conda.exe run -n solid_physics python verify.py"
```

### Installing dependencies
```bash
pip install numpy pandas matplotlib obspy scipy
# HW1 maps need:
pip install geopandas cartopy
```

## Important Implementation Details

- **HW1**: `analysis.py` fits the G-R law $\lg N = a - bM$ via `np.polyfit` on binned earthquake magnitudes. `figures.py` uses `geopandas.read_file()` to load Natural Earth vector data for the global map.
- **HW2**: All scripts implement stress tensor coordinate transformation formulas directly. `text2(g).py` computes Coulomb Failure Function $\Delta CFF = |\Delta\tau_s| + \mu_s \Delta\sigma_n$. `text2(h).py` computes earthquake time advancement $\Delta t = \Delta CFF_{\text{jump}} / \dot{CFF}$.
- **HW3**: Pipeline: read SAC files → download station metadata from EarthScope → detrend → remove instrument response (to velocity) → rotate NE→RT using back azimuth → plot record sections with theoretical P/S arrivals from `obspy.taup.TauPyModel("iasp91")`.
- **HW4**: `HW4_text1.ipynb` builds two Mars 1D velocity models (`.nd` files compiled to `.npz` via `build_taup_model`) with/without solid inner core, then uses `TauPyModel` for ray path computation. `HW4_text2.ipynb` implements ray tracing from scratch using three methods (cartesian, spherical, earth-flattening) with singularity-avoiding substitution $u = \sqrt{r - r_{\text{turn}}}$ for numerical integration.
- **TauP model files** (HW4): `.nd` files define layer interfaces with keywords `mantle`, `outer-core`, `inner-core`. Compiled `.npz` files go in `models/` directory.
