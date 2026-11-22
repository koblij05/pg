
import sys
from pathlib import Path

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Tato funkce načte binární soubor z cesty file_name,
    z něj přečte prvních header_length bytů a ty vrátí pomocí return
    """
    with open(file_name, "rb") as fp:
        header = fp.read(header_length)
    return header


def is_jpeg(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné jpeg_header
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanými hlavičkami v proměnných gif_header1 a gif_header2
    """
    # Nebudu spoléhat na stejnou délku
    header1 = read_header(file_name, len(gif_header1))
    header2 = read_header(file_name, len(gif_header2))
    return header1 == gif_header1 or header2 == gif_header2


def is_png(file_name):
    """
    Funkce zkusí přečíst ze souboru hlavičku obrázku jpeg,
    tu srovná s definovanou hlavičkou v proměnné png_header
    """
    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):
    """
    Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f'Soubor {file_name} je typu jpeg')
    elif is_gif(file_name):
        print(f'Soubor {file_name} je typu gif')
    elif is_png(file_name):
        print(f'Soubor {file_name} je typu png')
    else:
        print(f'Soubor {file_name} je neznámého typu')


if __name__ == '__main__':
    try:
        if len(sys.argv) <= 1:
            print("Není zadán žádný soubor. Je nutné použít parametr při spuštění.")
            sys.exit(1)
        file_name = sys.argv[1]
        if not Path(file_name).exists():
            print(f'Soubor "{file_name}" neexistuje.')
            sys.exit(1)
        print_file_type(file_name)
        
        x = 0 / 0

    except Exception as e:
        print(f"Nastala obecná chyba aplikace: {e}")