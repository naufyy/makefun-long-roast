"""One-line satirical roast for make.fun: a lawmaker who regulates the
internet writes the rules, then cannot turn her own draft into a PDF."""

from pathlib import Path

TEXT = "The chair of the digital privacy committee writes laws for algorithms she has never met, then forwards every draft to her grandson with the subject line \"please make this a PDF\"."

OUTPUT = Path("/output/entry.txt")

def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")

if __name__ == "__main__":
    main()
