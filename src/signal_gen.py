"""
signal_gen.py
Week 1: Foundations & signal generation
"""

import numpy as np


def generate_message_signal(t, freq=1000, amplitude=1.0):
    """Generate a simple sinusoidal message (baseband) signal."""
    return amplitude * np.cos(2 * np.pi * freq * t)


def generate_carrier(t, freq=100_000, amplitude=1.0):
    """Generate a carrier signal."""
    return amplitude * np.cos(2 * np.pi * freq * t)


def am_dsb_modulate(message, carrier_freq, t, carrier_amplitude=1.0):
    """
    Standard AM (DSB, with carrier) modulation.
    s(t) = Ac * [1 + ka*m(t)] * cos(2*pi*fc*t)
    """
    carrier = np.cos(2 * np.pi * carrier_freq * t)
    return carrier_amplitude * (1 + message) * carrier


def sampling_time_vector(duration, sample_rate):
    """Build a time vector for a given duration and sample rate."""
    n_samples = int(duration * sample_rate)
    return np.arange(n_samples) / sample_rate


def compute_fft(signal, sample_rate):
    """Compute single-sided FFT magnitude spectrum of a real signal."""
    n = len(signal)
    fft_vals = np.fft.rfft(signal)
    freqs = np.fft.rfftfreq(n, d=1 / sample_rate)
    magnitude = np.abs(fft_vals) / n
    return freqs, magnitude


if __name__ == "__main__":
    fs = 1_000_000
    duration = 0.01
    t = sampling_time_vector(duration, fs)

    message = generate_message_signal(t, freq=1000, amplitude=0.8)
    am_signal = am_dsb_modulate(message, carrier_freq=100_000, t=t)

    freqs, mag = compute_fft(am_signal, fs)
    peak_freq = freqs[np.argmax(mag)]

    print(f"Generated {len(am_signal)} samples over {duration*1000:.1f} ms")
    print(f"Peak frequency in spectrum: {peak_freq:.1f} Hz (expect ~100000 Hz carrier)")
