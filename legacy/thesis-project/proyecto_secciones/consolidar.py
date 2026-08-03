#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simplificado para consolidar todas las secciones del proyecto
"""

import os
import sys
import glob

# Fix para Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def consolidar():
    """Consolida todas las secciones en orden numérico"""

    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    archivo_salida = os.path.join(os.path.dirname(carpeta_actual), "PROYECTO_FINAL_CONSOLIDADO.md")

    print("="*70)
    print("  CONSOLIDADOR DE PROYECTO")
    print("="*70)
    print()
    print(f"[*] Carpeta: {carpeta_actual}")
    print(f"[*] Salida:  {archivo_salida}")
    print()

    # Buscar todos los archivos .md numerados
    archivos = sorted(glob.glob(os.path.join(carpeta_actual, "[0-9][0-9]_*.md")))

    if not archivos:
        print("[ERROR] No se encontraron archivos de secciones")
        return

    print(f"[*] Encontrados {len(archivos)} archivos de secciones\n")

    contenido_completo = []
    total_bytes = 0

    for archivo in archivos:
        nombre = os.path.basename(archivo)
        print(f"    [+] {nombre}")

        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            contenido_completo.append(contenido)
            contenido_completo.append("\n\n")  # Espacio entre secciones
            total_bytes += len(contenido.encode('utf-8'))

    # Escribir archivo consolidado
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(''.join(contenido_completo))

    # Estadísticas
    with open(archivo_salida, 'r', encoding='utf-8') as f:
        lineas = len(f.readlines())

    tamano_kb = total_bytes / 1024
    paginas_est = lineas // 45

    print()
    print("="*70)
    print("[OK] Consolidacion completada!")
    print("="*70)
    print()
    print(f"    Archivo: {os.path.basename(archivo_salida)}")
    print(f"    Tamanio: {tamano_kb:.1f} KB ({total_bytes:,} bytes)")
    print(f"    Lineas:  {lineas:,}")
    print(f"    Paginas: ~{paginas_est} (estimado a 45 lineas/pagina)")
    print()
    print(f"[*] Ubicacion: {archivo_salida}")
    print()

if __name__ == "__main__":
    try:
        consolidar()
    except Exception as e:
        print(f"\n[ERROR] {e}")
        import traceback
        traceback.print_exc()
