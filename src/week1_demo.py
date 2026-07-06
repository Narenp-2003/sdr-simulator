"""
week1_demo.py
Week 1 deliverable: generate a clean AM signal and visualize it.
Run: python week1_demo.py
"""

import matplotlib.pyplot as plt
from signal_gen import (
    sampling_time_vector, generate_message_signal,
    am_dsb_modulate, compute_fft,
)
from visualize import plot_time_domain, plot_spectrum, plot_spectrogram


def main():
    fs = 1_000_000
    duration = 0.02
    message_freq = 1000
    carrier_freq = 100_000

    t = sampling_time_vector(duration, fs)
    message = generate_message_signal(t, freq=message_freq, amplitude=0.8)
    am_signal = am_dsb_modulate(message, carrier_freq=carrier_freq, t=t)
    freqs, mag = compute_fft(am_signal, fs)

    fig, axes = plt.subplots(4, 1, figsize=(10, 12))
    plot_time_domain(t, message, title="Message Signal (1 kHz tone)", ax=axes[0])
    plot_time_domain(t, am_signal, title="AM Modulated Signal (100 kHz carrier)", ax=axes[1])
    plot_spectrum(freqs, mag, title="Spectrum of AM Signal", ax=axes[2], xlim=(90_000, 110_000))
    plot_spectrogram(am_signal, fs, title="Spectrogram of AM Signal", ax=axes[3])

    plt.tight_layout()
    plt.savefig("../docs/week1_output.png", dpi=150)
    print("Saved figure to ../docs/week1_output.png")


if __name__ == "__main__":
    main()
