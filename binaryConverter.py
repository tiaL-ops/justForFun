import tkinter as tk
from tkinter import messagebox


# Functions for conversions
def to_biased_signed(nb, bit):
    try:
        nb = int(nb)
        bit = int(bit)
        bias = 2**(bit - 1)
        biased_value = nb + bias
        binary_representation = ""

        while biased_value > 0:
            remainder = biased_value % 2
            biased_value = biased_value // 2
            binary_representation = str(remainder) + binary_representation

        # Ensure the result is padded to the correct bit length
        binary_representation = binary_representation.zfill(bit)
        return binary_representation
    except Exception as e:
        messagebox.showerror("Error", str(e))


def to_twos_complement(nb, bit):
    try:
        nb = int(nb)
        bit = int(bit)
        if nb >= 0:
            return bin(nb)[2:].zfill(bit)
        else:
            abs_binary = bin(abs(nb))[2:].zfill(bit)
            inverted_binary = ''.join('1' if b == '0' else '0' for b in abs_binary)
            twos_complement_value = int(inverted_binary, 2) + 1
            return bin(twos_complement_value)[2:].zfill(bit)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def ieee_754_to_float(binary_str):
    try:
        if len(binary_str) != 32:
            raise ValueError("Input must be a 32-bit binary string.")
        
        sign_bit = int(binary_str[0])
        exponent_bits = binary_str[1:9]
        fraction_bits = binary_str[9:]

        sign = (-1) ** sign_bit
        exponent_raw = int(exponent_bits, 2)
        exponent_bias = 127
        exponent = exponent_raw - exponent_bias

        mantissa = 1.0
        for i, bit in enumerate(fraction_bits):
            if bit == '1':
                mantissa += 2 ** -(i + 1)

        float_value = sign * mantissa * (2 ** exponent)
        return float_value
    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Setup
def convert():
    number = entry_number.get()
    bit_size = entry_bits.get()
    binary = entry_binary.get()

    if selected_option.get() == 1:
        result.set(to_biased_signed(number, bit_size))
    elif selected_option.get() == 2:
        result.set(to_twos_complement(number, bit_size))
    elif selected_option.get() == 3:
        result.set(str(ieee_754_to_float(binary)))


# Create main window
window = tk.Tk()
window.title("Binary Conversions")
window.geometry("400x400")

# Input fields and labels
label_number = tk.Label(window, text="Enter number:")
label_number.pack()

entry_number = tk.Entry(window)
entry_number.pack()

label_bits = tk.Label(window, text="Enter bit size:")
label_bits.pack()

entry_bits = tk.Entry(window)
entry_bits.pack()

label_binary = tk.Label(window, text="Enter binary (32 bits for IEEE 754):")
label_binary.pack()

entry_binary = tk.Entry(window)
entry_binary.pack()

# Radio buttons to select conversion type
selected_option = tk.IntVar()

radio_biased = tk.Radiobutton(window, text="Biased Signed Binary", variable=selected_option, value=1)
radio_biased.pack()

radio_twos = tk.Radiobutton(window, text="Two's Complement", variable=selected_option, value=2)
radio_twos.pack()

radio_ieee = tk.Radiobutton(window, text="IEEE-754 to Float", variable=selected_option, value=3)
radio_ieee.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.pack()

# Output field for the result
result = tk.StringVar()

label_result = tk.Label(window, text="Result:")
label_result.pack()

output_result = tk.Entry(window, textvariable=result, state='readonly')
output_result.pack()

# Run the application
window.mainloop()
