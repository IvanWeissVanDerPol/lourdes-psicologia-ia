#!/usr/bin/env python3
"""
Script para dividir el proyecto en secciones individuales
y luego consolidarlas en un documento final
"""

import os
import re

# Definir las secciones del proyecto
SECCIONES = [
    ("00_portada.md", "Portada"),
    ("01_indice.md", "Índice"),
    ("02_resumen.md", "1. RESUMEN"),
    ("03_palabras_clave.md", "2. PALABRAS CLAVE"),
    ("04_introduccion.md", "3. INTRODUCCIÓN"),
    ("05_politicas_institucionales.md", "4. POLÍTICAS INSTITUCIONALES"),
    ("06_fundamentacion_teorica.md", "5. FUNDAMENTACIÓN TEÓRICA"),
    ("07_planteamiento_problema.md", "6. PLANTEAMIENTO DEL PROBLEMA"),
    ("08_hipotesis.md", "7. HIPÓTESIS"),
    ("09_objetivos.md", "8. OBJETIVOS DEL PROYECTO"),
    ("10_variables.md", "9. VARIABLES DE ESTUDIO"),
    ("11_metodologia.md", "10. METODOLOGÍA"),
    ("12_estrategia_implementacion.md", "11. ESTRATEGIA DE IMPLEMENTACIÓN"),
    ("13_descripcion_sesiones.md", "12. DESCRIPCIÓN DETALLADA DE LAS SESIONES"),
    ("14_cronograma.md", "13. PLAN DE TRABAJO Y CRONOGRAMA"),
    ("15_presupuesto.md", "14. PRESUPUESTO Y RECURSOS"),
    ("16_aspectos_eticos.md", "15. ASPECTOS ÉTICOS"),
    ("17_analisis_datos.md", "16. PLAN DE ANÁLISIS DE DATOS"),
    ("18_resultados_esperados.md", "17. RESULTADOS ESPERADOS"),
    ("19_limitaciones.md", "18. LIMITACIONES DEL ESTUDIO"),
    ("20_aportes.md", "19. APORTES Y RELEVANCIA DEL ESTUDIO"),
    ("21_referencias.md", "20. REFERENCIAS BIBLIOGRÁFICAS"),
    ("22_anexos.md", "21. ANEXOS"),
]

def consolidar_proyecto(carpeta_secciones, archivo_salida):
    """Consolida todas las secciones en un documento final"""

    print(f"📚 Consolidando proyecto desde: {carpeta_secciones}")
    print(f"📄 Archivo de salida: {archivo_salida}\n")

    contenido_completo = []
    secciones_encontradas = 0
    secciones_faltantes = []

    for archivo, nombre_seccion in SECCIONES:
        ruta_completa = os.path.join(carpeta_secciones, archivo)

        if os.path.exists(ruta_completa):
            print(f"✅ Leyendo: {archivo}")
            with open(ruta_completa, 'r', encoding='utf-8') as f:
                contenido = f.read()
                contenido_completo.append(contenido)
                contenido_completo.append("\n\n---\n\n")  # Separador entre secciones
                secciones_encontradas += 1
        else:
            print(f"⚠️  Falta: {archivo} ({nombre_seccion})")
            secciones_faltantes.append(nombre_seccion)

    # Escribir archivo consolidado
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(''.join(contenido_completo))

    print(f"\n✅ Consolidación completada!")
    print(f"📊 Secciones procesadas: {secciones_encontradas}/{len(SECCIONES)}")

    if secciones_faltantes:
        print(f"\n⚠️  Secciones faltantes ({len(secciones_faltantes)}):")
        for seccion in secciones_faltantes:
            print(f"   - {seccion}")

    # Estadísticas del archivo
    tamano = os.path.getsize(archivo_salida)
    with open(archivo_salida, 'r', encoding='utf-8') as f:
        lineas = len(f.readlines())

    print(f"\n📈 Estadísticas del documento final:")
    print(f"   - Tamaño: {tamano:,} bytes ({tamano/1024:.1f} KB)")
    print(f"   - Líneas: {lineas:,}")
    print(f"   - Páginas estimadas: {lineas // 45} (aprox. 45 líneas/página)")

def crear_plantilla_seccion(nombre_archivo, titulo_seccion):
    """Crea una plantilla vacía para una sección"""
    plantilla = f"""# {titulo_seccion}

## [Completar esta sección]

*Esta sección está pendiente de desarrollo.*

---

**Contenido a incluir:**
- [Descripción de lo que debe contener]
- [Puntos clave a desarrollar]
- [Referencias o consideraciones importantes]

---
"""
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(plantilla)
    print(f"📝 Plantilla creada: {nombre_archivo}")

def verificar_estructura(carpeta_secciones):
    """Verifica qué secciones existen y cuáles faltan"""
    print("🔍 Verificando estructura del proyecto...\n")

    existentes = []
    faltantes = []

    for archivo, nombre_seccion in SECCIONES:
        ruta_completa = os.path.join(carpeta_secciones, archivo)
        if os.path.exists(ruta_completa):
            tamano = os.path.getsize(ruta_completa)
            existentes.append((archivo, nombre_seccion, tamano))
        else:
            faltantes.append((archivo, nombre_seccion))

    print(f"✅ Secciones existentes ({len(existentes)}):")
    for archivo, nombre, tamano in existentes:
        print(f"   {archivo:40} {tamano:>8,} bytes - {nombre}")

    if faltantes:
        print(f"\n⚠️  Secciones faltantes ({len(faltantes)}):")
        for archivo, nombre in faltantes:
            print(f"   {archivo:40} - {nombre}")

    return len(existentes), len(faltantes)

if __name__ == "__main__":
    import sys

    # Rutas
    carpeta_base = os.path.dirname(os.path.abspath(__file__))
    archivo_salida = os.path.join(os.path.dirname(carpeta_base), "PROYECTO_FINAL_CONSOLIDADO.md")

    print("="*70)
    print("  GESTOR DE PROYECTO DE INVESTIGACIÓN")
    print("="*70)
    print()

    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "verificar":
            existentes, faltantes = verificar_estructura(carpeta_base)
            print(f"\n📊 Total: {existentes} completas, {faltantes} pendientes")

        elif comando == "consolidar":
            consolidar_proyecto(carpeta_base, archivo_salida)
            print(f"\n✅ Documento consolidado guardado en:")
            print(f"   {archivo_salida}")

        elif comando == "crear-plantillas":
            print("📝 Creando plantillas para secciones faltantes...\n")
            count = 0
            for archivo, nombre_seccion in SECCIONES:
                ruta_completa = os.path.join(carpeta_base, archivo)
                if not os.path.exists(ruta_completa):
                    crear_plantilla_seccion(ruta_completa, nombre_seccion)
                    count += 1
            print(f"\n✅ {count} plantillas creadas")
        else:
            print(f"❌ Comando desconocido: {comando}")
            print("\nComandos disponibles:")
            print("  verificar         - Verifica qué secciones existen")
            print("  consolidar        - Consolida todas las secciones en un documento")
            print("  crear-plantillas  - Crea plantillas para secciones faltantes")
    else:
        print("Uso: python dividir_proyecto.py [comando]")
        print("\nComandos:")
        print("  verificar         - Verifica qué secciones existen")
        print("  consolidar        - Consolida todas las secciones en un documento")
        print("  crear-plantillas  - Crea plantillas para secciones faltantes")
        print("\nEjemplo:")
        print("  python dividir_proyecto.py verificar")
        print("  python dividir_proyecto.py consolidar")
