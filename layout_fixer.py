"""Layout Fixer command-line engine.

Russian uses the standard Windows keyboard key positions.
Tajik-specific letters use reversible ~ escape sequences because there is
no single universally compatible physical-key mapping for those characters.
"""
from __future__ import annotations

RU_TO_EN = {
    "ё": "\u0060", "й": "q", "ц": "w", "у": "e", "к": "r", "е": "t",
    "н": "y", "г": "u", "ш": "i", "щ": "o", "з": "p", "х": "[", "ъ": "]",
    "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "р": "h", "о": "j",
    "л": "k", "д": "l", "ж": ";", "э": "'", "я": "z", "ч": "x", "с": "c",
    "м": "v", "и": "b", "т": "n", "ь": "m", "б": ",", "ю": ".",
}
RU_TO_EN.update({key.upper(): value.upper() for key, value in list(RU_TO_EN.items())})
RU_TO_EN.update({"Ё": "~", "Х": "{", "Ъ": "}", "Ж": ":", "Э": '"', "Б": "<", "Ю": ">"})

TJ_TO_EN = {
    **RU_TO_EN,
    "ғ": "~g", "ӣ": "~i", "қ": "~q", "ӯ": "~u", "ҳ": "~h", "ҷ": "~j",
    "Ғ": "~G", "Ӣ": "~I", "Қ": "~Q", "Ӯ": "~U", "Ҳ": "~H", "Ҷ": "~J",
}

def reverse_map(mapping: dict[str, str]) -> dict[str, str]:
    """Build a reversible map; duplicate target keys are rejected."""
    reversed_mapping: dict[str, str] = {}
    for source, target in mapping.items():
        if target in reversed_mapping:
            raise ValueError(f"Mapping is not reversible: {target!r}")
        reversed_mapping[target] = source
    return reversed_mapping

EN_TO_RU = reverse_map(RU_TO_EN)
EN_TO_TJ = reverse_map(TJ_TO_EN)

DIRECTIONS = {
    "1": ("RU → EN", RU_TO_EN),
    "2": ("EN → RU", EN_TO_RU),
    "3": ("TJ → EN", TJ_TO_EN),
    "4": ("EN → TJ", EN_TO_TJ),
}

def convert(text: str, direction: str) -> str:
    """Convert text using direction 1–4 or its descriptive key."""
    key = {"ru_en": "1", "en_ru": "2", "tj_en": "3", "en_tj": "4"}.get(direction, direction)
    if key not in DIRECTIONS:
        raise ValueError("Direction must be one of: 1, 2, 3, 4, ru_en, en_ru, tj_en, en_tj")
    mapping = DIRECTIONS[key][1]
    # Longest tokens first makes the Tajik ~ escape sequences reversible.
    if key == "4":
        import re
        tokens = sorted(mapping, key=len, reverse=True)
        pattern = re.compile("|".join(re.escape(token) for token in tokens))
        return pattern.sub(lambda match: mapping[match.group(0)], text)
    return "".join(mapping.get(char, char) for char in text)

def detect_direction(text: str) -> str | None:
    """Detect Cyrillic source scripts; Latin text is ambiguous without a target."""
    tajik = any(char in "ғӣқӯҳҷҒӢҚӮҲҶ" for char in text)
    cyrillic = any("а" <= char.lower() <= "я" or char.lower() == "ё" for char in text)
    latin = any(("a" <= char.lower() <= "z") for char in text)
    if tajik and not latin:
        return "3"
    if cyrillic and not latin:
        return "1"
    return None

def main() -> None:
    print("\n=== Layout Fixer 4.1 ===")
    print("1. Russian → English")
    print("2. English → Russian")
    print("3. Tajik → English")
    print("4. English → Tajik")
    print("A. AUTO (Russian/Tajik Cyrillic)")
    print("0. Exit\n")
    while True:
        choice = input("Choose (1 / 2 / 3 / 4 / A / 0): ").strip().lower()
        if choice == "0":
            print("Goodbye!")
            return
        if choice == "a":
            text = input("\nEnter text: ")
            choice = detect_direction(text)
            if choice is None:
                print("AUTO cannot infer the target for Latin or mixed text. Choose 2 or 4.\n")
                continue
        if choice not in DIRECTIONS:
            print("Invalid option. Choose 1, 2, 3, 4, A, or 0.\n")
            continue
        text = input("\nEnter text: ")
        print("\n--- Result ---")
        print(convert(text, choice))
        print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
