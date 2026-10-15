"""Resume la rentabilidad del conjunto de ventas usado en el diplomado."""

from argparse import ArgumentParser
from pathlib import Path
import sys

import pandas as pd
from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    parser = ArgumentParser()
    parser.add_argument(
        "--data",
        type=Path,
        default=Path(__file__).parent / "data" / "RetailNuevo3.csv",
        help="Ruta del CSV de ventas (por defecto: data/RetailNuevo3.csv)",
    )
    args = parser.parse_args()

    data = pd.read_csv(args.data)
    required = {"Sales", "Profit", "Discount", "Category", "Sub-Category"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Faltan columnas: {', '.join(sorted(missing))}")

    sales = data["Sales"].sum()
    profit = data["Profit"].sum()
    margin = 100 * profit / sales
    by_subcategory = data.groupby("Sub-Category")["Profit"].sum().sort_values()
    by_discount = data.groupby(data["Discount"].gt(0.2))["Profit"].agg(["size", "sum"])

    print(f"Registros: {len(data)}")
    print(f"Ventas: {sales:.2f}; ganancia: {profit:.2f}; margen: {margin:.2f}%")
    print("\nGanancia por subcategoría:\n", by_subcategory.round(2).to_string())
    print("\nDescuentos ≤20% (False) y >20% (True):\n", by_discount.round(2).to_string())

    width, height = 1200, 900
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    font_path = "C:/Windows/Fonts/arial.ttf"
    try:
        title_font = ImageFont.truetype(font_path, 32)
        label_font = ImageFont.truetype(font_path, 21)
        note_font = ImageFont.truetype(font_path, 18)
    except OSError:
        title_font = ImageFont.load_default(size=32)
        label_font = ImageFont.load_default(size=21)
        note_font = ImageFont.load_default(size=18)
    draw.text((50, 32), "Ganancia neta por subcategoría", fill="#17212b", font=title_font)
    draw.text((50, 80), "Importes en unidades del archivo de clase", fill="#556371", font=note_font)

    left, right = 300, 1030
    values = by_subcategory.to_list()
    min_value, max_value = min(values), max(values)

    def position(value: float) -> int:
        return int(left + (value - min_value) / (max_value - min_value) * (right - left))

    zero = position(0)
    draw.line((zero, 130, zero, 820), fill="#344454", width=2)
    for index, (name, value) in enumerate(by_subcategory.items()):
        y = 137 + index * 40
        x = position(value)
        draw.text((40, y), name, fill="#263442", font=label_font)
        draw.rectangle((min(x, zero), y + 3, max(x, zero), y + 25),
                       fill="#b94545" if value < 0 else "#2d6e92")
        label = f"{value:,.0f}"
        draw.text((x - 100 if value < 0 else x + 8, y + 2), label,
                  fill="#263442", font=note_font)
    draw.text((50, 850), "Rojo: pérdida neta  |  Azul: ganancia neta", fill="#556371", font=note_font)
    output = Path(__file__).parent / "images" / "profit_by_subcategory.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    print(f"\nGráfico guardado en {output}")


if __name__ == "__main__":
    main()
