"""
visualize.py
Week 1: Visualization utilities
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as scipy_signal


def plot_time_domain(t, sig, title="Time Domain", ax=None, n_samples=500):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 3))
    n = min(n_samples, len(t))
    ax.plot(t[:n] * 1000, sig[:n])
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Amplitude")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    return ax


def plot_spectrum(freqs, magnitude, title="Frequency Spectrum", ax=None, xlim=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(freqs / 1000, magnitude)
    ax.set_xlabel("Frequency (kHz)")
    ax.set_ylabel("Magnitude")
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    if xlim:
        ax.set_xlim(xlim[0] / 1000, xlim[1] / 1000)
    return ax


def plot_spectrogram(sig, sample_rate, title="Spectrogram", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 4))
    f, t_spec, Sxx = scipy_signal.spectrogram(sig, fs=sample_rate, nperseg=1024)
    Sxx_db = 10 * np.log10(Sxx + 1e-12)
    im = ax.pcolormesh(t_spec * 1000, f / 1000, Sxx_db, shading="gouraud", cmap="viridis")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Frequency (kHz)")
    ax.set_title(title)
    return ax, im
