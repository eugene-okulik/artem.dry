import os
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('logs_dir', help='Путь к папке с логами')
    parser.add_argument('--text', required=True, help='Текст для поиска')
    args = parser.parse_args()

    logs_dir = args.logs_dir
    search_text = args.text

    if not os.path.isdir(logs_dir):
        print("Ошибка: это не папка или путь не существует.")
        return

    found = False

    for filename in os.listdir(logs_dir):
        filepath = os.path.join(logs_dir, filename)
        if not os.path.isfile(filepath):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"Не удалось прочитать {filename}: {e}")
            continue

        for i, line in enumerate(lines):
            if search_text.lower() in line.lower():
                timestamp = "время не найдено"
                for j in range(i, -1, -1):
                    if (len(lines[j]) >= 19
                            and lines[j][4] == '-'
                            and lines[j][7] == '-'
                            and lines[j][13] == ':'
                            and lines[j][16] == ':'):
                        timestamp = lines[j][:19].strip()
                        break

                words = line.split()
                context = "контекст не извлечён"
                for wi, word in enumerate(words):
                    if search_text.lower() in word.lower():
                        start = max(0, wi - 5)
                        end = min(len(words), wi + 6)
                        fragment = words[start:end]
                        fragment[wi - start] = f"[{fragment[wi - start]}]"
                        context = " ".join(fragment)
                        break
                else:
                    context = line.strip()[:100] + ("..." if len(line.strip()) > 100 else "")

                print(f"Файл: {filename}")
                print(f"Время: {timestamp}")
                print(f"Контекст: {context}\n")
                found = True

    if not found:
        print("Ничего не найдено.")


if __name__ == "__main__":
    main()
