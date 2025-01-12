from pathlib import Path
import shutil
import sys


# Функція для рекурсивного копіювання та сортування файлів
def process_directory(source_dir, dest_dir):
    try:
        source_path = Path(source_dir)
        dest_path = Path(dest_dir)

        # Перебір всіх елементів у директорії
        for item in source_path.iterdir():
            if item.is_dir():
                # Рекурсивно обробляємо піддиректорії
                process_directory(item, dest_path)

            elif item.is_file():
                # Отримуємо розширення файлу
                file_extension = item.suffix.lstrip(".").lower() or "unknown"

                # Створюємо піддиректорію на основі розширення
                extension_dir = dest_path / file_extension
                extension_dir.mkdir(parents=True, exist_ok=True)

                # Копіюємо файл до піддиректорії
                shutil.copy2(item, extension_dir / item.name)

    except Exception as e:
        print(f"Помилка обробки '{source_dir}': {e}")


# Головна функція
def main():
    if len(sys.argv) < 2:
        print(
            "Вкажіть шлях до вихідної та цільової директорій. Наприклад: python main.py [source_dir] [dest_dir]"
        )
        return

    source_dir = Path(sys.argv[1])
    dest_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Вихідна директорія '{source_dir}' не існує або це не директорія.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    print(f"Копіювання файлів із '{source_dir}' до '{dest_dir}'...")

    process_directory(source_dir, dest_dir)
    print("Копіювання завершено.")


if __name__ == "__main__":
    main()