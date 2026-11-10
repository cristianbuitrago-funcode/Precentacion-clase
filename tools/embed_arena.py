"""Incrusta arena-contrarreloj.html dentro de escape-room-presentacion.html.

La presentación guarda la Arena como texto base64 en la constante ARENA_HTML_B64,
para que todo funcione con un solo archivo y sin internet. Después de editar
arena-contrarreloj.html, ejecuta desde la carpeta del proyecto:

    python3 tools/embed_arena.py
"""
import base64
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARENA = ROOT / "arena-contrarreloj.html"
PRESENTACION = ROOT / "escape-room-presentacion.html"

arena_b64 = base64.b64encode(ARENA.read_bytes()).decode("ascii")
html = PRESENTACION.read_bytes().decode("utf-8")

patron = re.compile(r'const ARENA_HTML_B64 = "[A-Za-z0-9+/=]*";')
nuevo, cambios = patron.subn(lambda _: f'const ARENA_HTML_B64 = "{arena_b64}";', html)
if cambios != 1:
    sys.exit(f"No se encontró una única constante ARENA_HTML_B64 (encontradas: {cambios}).")

PRESENTACION.write_bytes(nuevo.encode("utf-8"))
print(f"Arena incrustada en {PRESENTACION.name} ({ARENA.stat().st_size:,} bytes).")
