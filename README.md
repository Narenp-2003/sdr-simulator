# Software-Defined Radio Simulator

A from-scratch, software-only SDR pipeline in Python: signal generation,
AM/FM modulation & demodulation, filtering, noise simulation, and
real-time spectrum/waterfall visualization. No SDR hardware required —
built to run on real downloaded IQ captures as well as synthetic signals.

## Motivation

This project implements core communication theory concepts
(modulation, demodulation, Carson's Rule, matched filtering, noise
channels) as working code rather than just simulation in MATLAB/theory
exercises — closing the gap between coursework and applied DSP/RF
engineering.

Built from first principles rather than using existing tools like GNU
Radio or the `sdr` Python package, so every modulator/demodulator is
understood and verifiable against theory.

## Project Structure

sdr-simulator/

├── src/            # Core modules (signal_gen, visualize, modulation, etc.)

├── data/           # Downloaded IQ sample files (not committed - see below)

├── notebooks/      # Jupyter notebooks for exploration/demos

├── tests/          # Unit tests verifying theory (bandwidth, power, BER)

├── docs/           # Output figures, block diagrams, write-ups

└── requirements.txt

## Setup

```bash
python -m venv sdr-env
source sdr-env/Scripts/activate     # Windows Git Bash
pip install -r requirements.txt
```

## Roadmap

- [x] **Week 1** — Signal generation, time/frequency/spectrogram visualization
- [ ] **Week 2** — AM/FM modulators built from scratch, verified against Carson's Rule
- [ ] **Week 3** — Envelope/PLL/quadrature demodulators, roundtrip SNR/THD testing
- [ ] **Week 4** — Real IQ data ingestion + FIR/IIR filtering, decode real FM broadcast
- [ ] **Week 5** — AWGN/fading channel models, BER curves, live waterfall display
- [ ] **Week 6** — CLI/GUI wrapper, polished write-up, GitHub release

## Getting Real IQ Data (no hardware needed)

- [SigMF example datasets](https://github.com/gnuradio/SigMF) — labeled IQ recordings
- [RTL-SDR.com sample library](https://www.rtl-sdr.com/) — free `.wav`/`.iq` captures
- GNU Radio bundled test signals

Place downloaded files in `data/` (gitignored — don't commit large binary
IQ files; link to sources here instead).

## Week 1: Signal Generation

Run:
```bash
cd src
python week1_demo.py
```
Generates a 1 kHz message tone, AM-modulates it onto a 100 kHz carrier,
and produces `docs/week1_output.png` showing the time-domain waveforms,
the frequency spectrum (carrier + two sidebands, matching AM theory),
and a spectrogram.
