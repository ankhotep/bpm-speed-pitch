import subprocess

def change_bpm_without_pitch(input_file, output_file, factor):
    # Calculate the new tempo using the factor
    tempo_change = (factor - 1) * 100  # Convert factor to percentage change

    # Path to the rubberband executable (modify this if you've placed it elsewhere)
    rubberband_path = "C:\\speedpitch\\rubberband-3.3.0-gpl-executable-windows\\rubberband.exe"

    # Use rubberband to change the BPM without affecting pitch
    cmd = [
        rubberband_path,
        "--tempo", str(tempo_change),
        input_file,
        output_file
    ]
    subprocess.run(cmd)

# Example usage
input_file = "1_intro_120bpm.wav"
output_file = "1_intro_120bpm_1.wav"
#factor = 1.005  # Increase BPM by 50%
factor = 1.005  # Increase BPM by 50%

change_bpm_without_pitch(input_file, output_file, factor)
