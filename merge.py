import os

# Отдельная благодарность Gemini за код c;

def merge_lst_files():
    source_dir = 'sources'
    output_file = 'all_files.lst'
    unique_lines = set()

    # Проверяем, существует ли папка sources
    if not os.path.exists(source_dir):
        print(f"Ошибка: Папка '{source_dir}' не найдена!")
        return

    # Читаем все файлы с расширением .lst из папки sources
    for filename in os.listdir(source_dir):
        if filename.endswith('.lst'):
            file_path = os.path.join(source_dir, filename)
            print(f"Обработка файла: {filename}")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    clean_line = line.strip()
                    clean_line = clean_line.replace("=","")
                    # Пропускаем пустые строки и комментарии
                    if clean_line and not clean_line.startswith('#'):
                        unique_lines.add(clean_line)

    # Записываем уникальные строки в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as f:
        # Сортировка по алфавиту для красоты и удобства чтения git diff
        for line in sorted(unique_lines):
            f.write(line + '\n')
            
    print(f"Успешно! Объединено уникальных строк: {len(unique_lines)}. Результат в {output_file}")

if __name__ == '__main__':
    merge_lst_files()
