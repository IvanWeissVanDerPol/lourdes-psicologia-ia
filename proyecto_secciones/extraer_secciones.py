#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para extraer secciones del proyecto existente y crear archivos individuales
"""

import os
import re
import sys

# Fix para Windows console
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

def extraer_secciones(archivo_fuente, carpeta_destino):
    """Extrae secciones del archivo fuente y crea archivos individuales"""

    print(f"[*] Leyendo archivo fuente: {archivo_fuente}\n")

    with open(archivo_fuente, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Definir los patrones de secciones con sus archivos de destino
    secciones = [
        (r'# 1\. RESUMEN.*?(?=# 2\.|---\n\n# 2\.)', '02_resumen.md', '1. RESUMEN'),
        (r'# 2\. PALABRAS CLAVE.*?(?=---\n\n# 3\.)', '03_palabras_clave.md', '2. PALABRAS CLAVE'),
        (r'# 3\. INTRODUCCIÓN.*?(?=---\n\n# 4\.)', '04_introduccion.md', '3. INTRODUCCION'),
        (r'# 4\. POLÍTICAS INSTITUCIONALES.*?(?=---\n\n# 5\.)', '05_politicas_institucionales.md', '4. POLITICAS'),
        (r'# 5\. FUNDAMENTACIÓN TEÓRICA.*?(?=---\n\n# 6\.)', '06_fundamentacion_teorica.md', '5. FUNDAMENTACION'),
        (r'# 6\. PLANTEAMIENTO DEL PROBLEMA.*?(?=---\n\n# 7\.)', '07_planteamiento_problema.md', '6. PROBLEMA'),
        (r'# 7\. HIPÓTESIS.*?(?=---\n\n# 8\.)', '08_hipotesis.md', '7. HIPOTESIS'),
        (r'# 8\. OBJETIVOS DEL PROYECTO.*?(?=---\n\n\*\[Continúa|$)', '09_objetivos.md', '8. OBJETIVOS'),
    ]

    secciones_creadas = 0

    for patron, archivo_destino, nombre_seccion in secciones:
        match = re.search(patron, contenido, re.DOTALL)

        if match:
            texto_seccion = match.group(0)
            # Limpiar el final
            texto_seccion = texto_seccion.rstrip()
            texto_seccion = re.sub(r'\n---\s*$', '', texto_seccion)

            ruta_completa = os.path.join(carpeta_destino, archivo_destino)

            with open(ruta_completa, 'w', encoding='utf-8') as f:
                f.write(texto_seccion)
                f.write("\n\n---\n")

            tamano = os.path.getsize(ruta_completa)
            print(f"[OK] Creado: {archivo_destino:40} ({tamano:>6,} bytes)")
            secciones_creadas += 1
        else:
            print(f"[!] No encontrado: {nombre_seccion}")

    print(f"\n[OK] Total de secciones extraidas: {secciones_creadas}")

    return secciones_creadas

if __name__ == "__main__":
    carpeta_base = os.path.dirname(os.path.abspath(__file__))
    archivo_fuente1 = os.path.join(os.path.dirname(carpeta_base), "PROYECTO_COMPLETO_FINAL.md")
    archivo_fuente2 = os.path.join(os.path.dirname(carpeta_base), "PROYECTO_COMPLETO_FINAL_PARTE2.md")

    print("="*70)
    print("  EXTRACTOR DE SECCIONES DEL PROYECTO")
    print("="*70)
    print()

    if os.path.exists(archivo_fuente1):
        print("[*] Extrayendo desde PROYECTO_COMPLETO_FINAL.md...")
        extraer_secciones(archivo_fuente1, carpeta_base)
    else:
        print(f"[ERROR] No se encontro: {archivo_fuente1}")

    if os.path.exists(archivo_fuente2):
        print(f"\n[*] Extrayendo desde PROYECTO_COMPLETO_FINAL_PARTE2.md...")
        # Extraer sección 9 (Variables)
        with open(archivo_fuente2, 'r', encoding='utf-8') as f:
            contenido = f.read()
        match = re.search(r'# 9\. VARIABLES DE ESTUDIO.*', contenido, re.DOTALL)
        if match:
            ruta = os.path.join(carpeta_base, "10_variables.md")
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(match.group(0))
                f.write("\n\n---\n")
            tamano = os.path.getsize(ruta)
            print(f"[OK] Creado: 10_variables.md ({tamano:,} bytes)")

    print("\n" + "="*70)
    print("[OK] Extraccion completada")
    print("="*70)
