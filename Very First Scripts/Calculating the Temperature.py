
# Calculalating the Temperature.py

import tkinter as tk
root = tk.Tk()
root.title("Temperature Calculation")
cLabel = tk.Label(root, text="Celsius")
fLabel = tk.Label(root, text="Fahrenheit")
cEntry = tk.Entry(root, width=25)
cfButton = tk.Button(root, text">>")
fEntry = tk.Entry(root, width=25)
cLabel.grid(row=1, column=10)
fLabel.grid(row=1, column=30)
cEntry.grid(row=2, column=10)
cfButton.grid(row=2, column=15)
fEntry.grid(row=2, column=30)

# conversion from Celsius to Fahrenheit
def cfConvert():
	cTemp = float(cEntry.get())
	fTemp = round(cTemp * 9/5 + 32)
	fEntry.delete(0, tk.END)
	fEntry.insert(0, str(fTemp))

def main():
	cfButton.configure(command=cfConvert)
	 

main()