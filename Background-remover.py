import os
from rembg import remove

# Ścieżki folderów (możesz zmienić na swoje foldery)
input_folder = r'C:\Users\Marcin\Desktop\InputFolder'  # Folder wejściowy z plikami
output_folder = r'C:\Users\Marcin\Desktop\OutputFolder'  # Folder wyjściowy na zapisane pliki

# Upewnij się, że folder wyjściowy istnieje
os.makedirs(output_folder, exist_ok=True)

# Przechodzenie przez wszystkie pliki w folderze wejściowym
for filename in os.listdir(input_folder):
    input_path = os.path.join(input_folder, filename)

    # Sprawdzanie, czy plik jest obrazem (opcjonalnie możesz dodać inne rozszerzenia)
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        output_path = os.path.join(output_folder, filename)
        try:
            # Otwieranie pliku wejściowego
            with open(input_path, 'rb') as input_file:
                input_data = input_file.read()

            # Usuwanie tła
            output_data = remove(input_data)

            # Zapisywanie pliku wynikowego w folderze wyjściowym
            with open(output_path, 'wb') as output_file:
                output_file.write(output_data)

            print(f"Pomyślnie przetworzono: {filename}")
        except Exception as e:
            print(f"Błąd podczas przetwarzania {filename}: {e}")
    else:
        print(f"Pomijam plik: {filename} (nie jest obsługiwanym obrazem)")

print("Proces zakończony.")
