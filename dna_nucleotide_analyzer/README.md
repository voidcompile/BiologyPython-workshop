# 🧬 DNA Nucleotide Analyzer

A beginner-friendly Python script that reads a DNA sequence, counts the frequency of nucleotides (A, T, G, C), and visualizes the results using a simple bar chart. Perfect for students, researchers, or anyone exploring computational biology or bioinformatics with Python.

---

## 🚀 Features

- ✅ Reads DNA sequence from a `.txt` file
- ✅ Cleans and validates sequence (removes invalid characters)
- ✅ Counts the number of each nucleotide (A, T, G, C)
- ✅ Displays results in the terminal
- ✅ Plots a clear bar chart with `matplotlib`

---

## 📁 File Structure

dna_nucleotide_analyzer/
├── dna_nucleotide_analyzer.py # Main Python script
├── sample_dna.txt # Sample DNA input file
└── README.md # Project documentation

---

## 📦 Requirements

- Python 3.6+
- matplotlib

Install required packages:

```bash
pip install matplotlib
```

---

## 🧪 How to Run
Clone the repository or download the files.

Make sure the file sample_dna.txt is in the same directory and contains your DNA sequence, for example:
ATCGATCGGCTTAAGGCCATGCTAGCATCGATCGATCGATCGTAGCTAGCTAGCTA

Run the script:
python dna_nucleotide_analyzer.py

You will see:

The nucleotide counts printed in the terminal.

A bar chart displaying the frequency of A, T, G, and C.

---

🧠 How It Works
1. Read Sequence
The script reads the DNA sequence from sample_dna.txt, removes line breaks, converts it to uppercase, and filters out any characters that are not A, T, G, or C.

raw = file.read().replace('\n', '').upper()
cleaned = ''.join([nt for nt in raw if nt in "ATGC"])

2. Count Nucleotides
Using collections.Counter, it counts how many times each nucleotide appears.

Counter(sequence)

---

## 📚 Example Output
Console Output:
Nucleotide counts:
  A: 12
  T: 10
  G: 14
  C: 9

Bar Chart:
A clean, colorful histogram showing the frequencies.

---

## 🧩 Next Steps / Ideas
This simple project can be extended to:

Calculate GC content

Read FASTA files

Detect mutations or motifs

Translate DNA to protein


---

🧑‍💻 Author
Created by @voidcompile
Part of the BiologyPython-workshop series.

📢 [github: @voidcompile](https://github.com/voidcompile)
📢 [Telegram: @voidcompile](https://t.me/voidcompile)
📢 [youtube: @voidcompile](https://www.youtube.com/@voidcompile)
📢 [email: voidcompile@gmail.com]







