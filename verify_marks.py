#!/usr/bin/env python3
"""
Проверка регрессии: убеждается, что номер слайда ("N — 18") стоит
на одной и той же координате на всех страницах PDF.

Запуск: pip install pypdfium2 && python3 verify_marks.py
"""
import re
import pypdfium2 as pdfium

PDF_PATH = "presentation/Медиацентр_презентация+кейсы.pdf"
MARK_RE = re.compile(r"\d\s?\d\s?—\s?1\s?8")

def main():
    pdf = pdfium.PdfDocument(PDF_PATH)
    sizes = {tuple(round(v, 1) for v in pdf[i].get_size()) for i in range(len(pdf))}
    bottoms = set()
    missing = []

    for i in range(len(pdf)):
        textpage = pdf[i].get_textpage()
        text = textpage.get_text_bounded()
        m = MARK_RE.search(text)
        if not m:
            missing.append(i + 1)
            continue
        boxes = [textpage.get_charbox(j) for j in range(m.start(), m.end()) if text[j].strip()]
        bottoms.add(round(min(b[1] for b in boxes), 2))

    print(f"страниц: {len(pdf)}")
    print(f"размеры страниц: {sizes}")
    print(f"Y-координата номера на всех страницах: {bottoms}")

    if missing:
        print(f"✗ FAIL — номер не найден на страницах: {missing}")
        raise SystemExit(1)
    if len(bottoms) != 1:
        print("✗ FAIL — номер стоит на разных координатах")
        raise SystemExit(1)

    print(f"✓ OK — единственное значение на {len(pdf)} из {len(pdf)}")

if __name__ == "__main__":
    main()
