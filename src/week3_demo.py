"""
week3_demo.py
Week 3 deliverable: AM/FM demodulation, round-trip verification.
Run: python week3_demo.py
"""

import matplotlib.pyplot as plt
from signal_gen import (
    sampling_time_vector, generate_message_signal,
    am_dsb_modulate, fm_modulate,
    am_envelope_detect, fm_quadrature_demodulate,
    signal_to_noise_ratio,
)
from visualize import plot_time_domain


def main():
    fs = 1_000_000
    duration = 0.02
    message_freq = 1000
    carrier_freq = 100_000
    freq_deviation = 5000

    t = sampling_time_vector(duration, fs)
    message = generate_message_signal(t, freq=message_freq, amplitude=0.8)

    # --- AM round trip ---
    am_signal = am_dsb_modulate(message, carrier_freq=carrier_freq, t=t)
    am_recovered = am_envelope_detect(am_signal, fs)
    am_snr = signal_to_noise_ratio(message, am_recovered)

    # --- FM round trip ---
    fm_signal = fm_modulate(message, carrier_freq, t, freq_deviation=freq_deviation)
    fm_recovered = fm_quadrature_demodulate(fm_signal, fs, carrier_freq, freq_deviation)
    fm_snr = signal_to_noise_ratio(message, fm_recovered)

    print("=== AM Round Trip ===")
    print(f"Recovered signal SNR: {am_snr:.1f} dB")

    print("\n=== FM Round Trip ===")
    print(f"Recovered signal SNR: {fm_snr:.1f} dB")

    # --- Plot original vs recovered for both ---
    fig, axes = plt.subplots(4, 1, figsize=(10, 10))
    plot_time_domain(t, message, title="Original Message", ax=axes[0])
    plot_time_domain(t, am_recovered, title=f"AM Recovered (SNR: {am_snr:.1f} dB)", ax=axes[1])
    plot_time_domain(t, message, title="Original Message", ax=axes[2])
    plot_time_domain(t, fm_recovered, title=f"FM Recovered (SNR: {fm_snr:.1f} dB)", ax=axes[3])

    plt.tight_layout()
    plt.savefig("../docs/week3_output.png", dpi=150)
    print("\nSaved figure to ../docs/week3_output.png")


if __name__ == "__main__":
    main()
