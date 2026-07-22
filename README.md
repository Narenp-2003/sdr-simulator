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

├── src/ # Core modules (signal_gen, visualize, modulation, etc.)

├── data/ # Downloaded IQ sample files (not committed - see below)

├── notebooks/ # Jupyter notebooks for exploration/demos

├── tests/ # Unit tests verifying theory (bandwidth, power, BER)

├── docs/ # Output figures, block diagrams, write-ups

└── requirements.txt

## Setup

```bash
python -m venv sdr-env
source sdr-env/Scripts/activate     # Windows Git Bash
pip install -r requirements.txt
```

## Roadmap

- [x] **Week 1** — Signal generation, time/frequency/spectrogram visualization
- [x] **Week 2** — AM (DSB-FC) and FM modulators built from scratch, bandwidth verified against Carson's Rule
- [x] **Week 3** — AM envelope detector and FM quadrature demodulator, round-trip SNR verification
- [ ] **Week 4** — Real audio (.wav) input, complex I/Q signal representation, real IQ capture support
- [ ] **Week 5** — AWGN channel noise simulation, SNR degradation curves, live waterfall display
- [ ] **Week 6** — CLI wrapper, polished write-up, GitHub release

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

## Week 2: AM/FM Modulation + Carson's Rule Verification

Run:
```bash
cd src
python week2_demo.py
```

Implements two modulation schemes from scratch:
- **AM (DSB-FC)** — amplitude modulation, double sideband, full carrier
- **FM** — frequency modulation with adjustable frequency deviation

Verifies each against communication theory by comparing the
**theoretical** bandwidth (AM: `2×fm`, FM: Carson's Rule `2×(Δf+fm)`)
against the **measured** bandwidth from the actual FFT spectrum.

Results: theoretical and measured bandwidth matched exactly
(AM: 2000 Hz, FM: 12000 Hz), confirming the modulator implementations
are mathematically correct. Output saved to `docs/week2_output.png`.

## Week 3: Demodulation + Round-Trip Verification

Run:
```bash
cd src
python week3_demo.py
```

Implements the receiver side of the pipeline:
- **AM envelope detector** — Hilbert transform + low-pass filtering to
  recover the message from an AM waveform
- **FM quadrature demodulator** — instantaneous phase differentiation
  to recover the message from an FM waveform

Each demodulator is tested in a full round trip: original message →
modulate → demodulate → compare recovered signal to the original using
SNR (signal-to-noise ratio).

Results: AM recovery SNR of 43.7 dB, FM recovery SNR of 44.0 dB —
both near-perfect reconstructions, confirming the modulator/demodulator
pairs are mathematically consistent. Output saved to `docs/week3_output.png`.

## License

MIT
