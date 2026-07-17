"""
week2_demo.py
Week 2 deliverable: AM + FM modulation, verified against Carson's Rule.
Run: python week2_demo.py
"""

import matplotlib.pyplot as plt
from signal_gen import (
    sampling_time_vector, generate_message_signal,
    am_dsb_modulate, fm_modulate,
    compute_fft, carson_bandwidth_fm, am_bandwidth, measure_bandwidth,
)
from visualize import plot_spectrum


def main():
    fs = 1_000_000
    duration = 0.02
    message_freq = 1000
    carrier_freq = 100_000
    freq_deviation = 5000  # Δf for FM

    t = sampling_time_vector(duration, fs)
    message = generate_message_signal(t, freq=message_freq, amplitude=0.8)

    # --- AM ---
    am_signal = am_dsb_modulate(message, carrier_freq=carrier_freq, t=t)
    am_freqs, am_mag = compute_fft(am_signal, fs)
    am_measured_bw = measure_bandwidth(am_freqs, am_mag)
    am_theory_bw = am_bandwidth(message_freq)

    # --- FM ---
    fm_signal = fm_modulate(message, carrier_freq, t, freq_deviation=freq_deviation)
    fm_freqs, fm_mag = compute_fft(fm_signal, fs)
    fm_measured_bw = measure_bandwidth(fm_freqs, fm_mag)
    fm_theory_bw = carson_bandwidth_fm(freq_deviation, message_freq)

    print("=== AM ===")
    print(f"Theoretical bandwidth (2*fm): {am_theory_bw} Hz")
    print(f"Measured bandwidth (from spectrum): {am_measured_bw:.0f} Hz")

    print("\n=== FM ===")
    print(f"Theoretical bandwidth (Carson's Rule): {fm_theory_bw} Hz")
    print(f"Measured bandwidth (from spectrum): {fm_measured_bw:.0f} Hz")

    # --- Plot both spectra side by side ---
    fig, axes = plt.subplots(2, 1, figsize=(10, 6))
    plot_spectrum(am_freqs, am_mag, title="AM Spectrum", ax=axes[0],
                  xlim=(carrier_freq - 5000, carrier_freq + 5000))
    plot_spectrum(fm_freqs, fm_mag, title="FM Spectrum (Carson's Rule check)", ax=axes[1],
                  xlim=(carrier_freq - fm_theory_bw, carrier_freq + fm_theory_bw))

    plt.tight_layout()
    plt.savefig("../docs/week2_output.png", dpi=150)
    print("\nSaved figure to ../docs/week2_output.png")


if __name__ == "__main__":
    main()
