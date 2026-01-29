"""
Parser de Conversaciones de WhatsApp

Este modulo procesa exports de WhatsApp y los estructura
para analisis posterior con IA.

Uso:
    from analysis.whatsapp_parser import parse_whatsapp_export

    mensajes = parse_whatsapp_export("chat.txt")
    for msg in mensajes:
        print(f"{msg['sender']}: {msg['content']}")
"""

import re
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass


@dataclass
class WhatsAppMessage:
    """Representa un mensaje individual de WhatsApp"""
    timestamp: datetime
    sender: str
    content: str
    is_media: bool = False
    is_system: bool = False


def parse_whatsapp_export(
    file_path: str,
    client_name: Optional[str] = None,
    therapist_name: Optional[str] = None,
) -> List[Dict]:
    """
    Parsea un archivo de export de WhatsApp.

    Args:
        file_path: Ruta al archivo .txt exportado de WhatsApp
        client_name: Nombre del cliente (para identificar mensajes)
        therapist_name: Nombre del terapeuta (para identificar mensajes)

    Returns:
        Lista de diccionarios con los mensajes parseados

    Ejemplo:
        >>> mensajes = parse_whatsapp_export("chat.txt", client_name="Juan")
        >>> print(len(mensajes))
        150
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")

    # Leer archivo
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    messages = []

    # Patrones de WhatsApp (varian segun idioma/region)
    # Formato comun: "DD/MM/YYYY, HH:MM - Nombre: Mensaje"
    # o: "DD/MM/YY, HH:MM - Nombre: Mensaje"
    # o: "[YYYY-MM-DD, HH:MM:SS] Nombre: Mensaje" (formato con corchetes)
    patterns = [
        # Formato con corchetes ISO: [2025-01-22, 17:48:39] Sender: Message
        r"^\[?(\d{4}-\d{2}-\d{2}),?\s+(\d{2}:\d{2}:\d{2})\]?\s*([^:]+):\s*(.+)",
        # Formato con ano de 4 digitos
        r"(\d{1,2}/\d{1,2}/\d{4}),?\s+(\d{1,2}:\d{2})\s*-\s*([^:]+):\s*(.+)",
        # Formato con ano de 2 digitos
        r"(\d{1,2}/\d{1,2}/\d{2}),?\s+(\d{1,2}:\d{2})\s*-\s*([^:]+):\s*(.+)",
        # Formato con AM/PM
        r"(\d{1,2}/\d{1,2}/\d{2,4}),?\s+(\d{1,2}:\d{2}\s*(?:AM|PM|a\.m\.|p\.m\.))\s*-\s*([^:]+):\s*(.+)",
    ]

    # Patron para mensajes de sistema
    system_pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}),?\s+(\d{1,2}:\d{2})\s*-\s*(.+)"

    lines = content.split("\n")
    current_message = None

    # Unicode characters to strip (LTR mark, RTL mark, etc.)
    unicode_control_chars = '\u200e\u200f\u202a\u202b\u202c\u202d\u202e\ufeff'

    for line in lines:
        # Strip whitespace and Unicode control characters
        line = line.strip()
        line = line.lstrip(unicode_control_chars)
        if not line:
            continue

        matched = False

        # Intentar cada patron
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                # Guardar mensaje anterior si existe
                if current_message:
                    messages.append(current_message)

                date_str, time_str, sender, msg_content = match.groups()
                sender = sender.strip()

                # Detectar mensajes de sistema
                is_system = any(keyword in msg_content.lower() for keyword in [
                    "creó el grupo",
                    "created group",
                    "añadió",
                    "added",
                    "salió",
                    "left",
                    "eliminó",
                    "removed",
                    "cambió",
                    "changed",
                ])

                # Detectar mensajes de media
                is_media = any(keyword in msg_content.lower() for keyword in [
                    "<multimedia omitido>",
                    "<media omitted>",
                    "imagen omitida",
                    "video omitido",
                    "audio omitido",
                    "sticker omitido",
                    "<attached:",  # Formato con archivos adjuntos
                ])

                # Detectar tipo de media si es attached (handle Unicode LTR mark)
                media_type = None
                content_lower = msg_content.lower()
                # Check for attached with or without special Unicode characters
                has_attached = "attached:" in content_lower or ".opus" in content_lower or ".jpg" in content_lower or ".webp" in content_lower or ".mp4" in content_lower

                if has_attached:
                    is_media = True
                    if "-audio-" in content_lower or ".opus" in content_lower:
                        media_type = "audio"
                    elif "-photo-" in content_lower or ".jpg" in content_lower or ".jpeg" in content_lower:
                        media_type = "photo"
                    elif "-sticker-" in content_lower or ".webp" in content_lower:
                        media_type = "sticker"
                    elif "-video-" in content_lower or ".mp4" in content_lower:
                        media_type = "video"
                    else:
                        media_type = "other"

                # Parsear timestamp
                try:
                    # Detectar formato ISO (YYYY-MM-DD) vs europeo (DD/MM/YYYY)
                    if "-" in date_str and len(date_str.split("-")[0]) == 4:
                        # Formato ISO: 2025-01-22
                        date_format = "%Y-%m-%d"
                        # Tiempo puede ser HH:MM:SS o HH:MM
                        time_format = "%H:%M:%S" if time_str.count(":") == 2 else "%H:%M"
                        datetime_str = f"{date_str} {time_str}"
                        timestamp = datetime.strptime(datetime_str, f"{date_format} {time_format}")
                    else:
                        # Formato europeo
                        if len(date_str.split("/")[-1]) == 2:
                            date_format = "%d/%m/%y"
                        else:
                            date_format = "%d/%m/%Y"

                        # Limpiar time_str de AM/PM si existe
                        time_clean = re.sub(r"\s*(AM|PM|a\.m\.|p\.m\.)", "", time_str).strip()
                        datetime_str = f"{date_str} {time_clean}"
                        timestamp = datetime.strptime(datetime_str, f"{date_format} %H:%M")
                except ValueError:
                    timestamp = None

                current_message = {
                    "timestamp": timestamp.isoformat() if timestamp else None,
                    "date": date_str,
                    "time": time_str,
                    "sender": sender,
                    "content": msg_content.strip(),
                    "is_media": is_media,
                    "media_type": media_type if is_media else None,
                    "is_system": is_system,
                    "role": _identify_role(sender, client_name, therapist_name),
                }

                matched = True
                break

        # Si no matcheo ningun patron, es continuacion del mensaje anterior
        if not matched and current_message:
            current_message["content"] += "\n" + line

    # Agregar ultimo mensaje
    if current_message:
        messages.append(current_message)

    return messages


def _identify_role(
    sender: str,
    client_name: Optional[str],
    therapist_name: Optional[str]
) -> str:
    """Identifica si el mensaje es del cliente, terapeuta, o desconocido"""
    sender_lower = sender.lower()

    if client_name and client_name.lower() in sender_lower:
        return "client"
    if therapist_name and therapist_name.lower() in sender_lower:
        return "therapist"
    return "unknown"


def filter_messages(
    messages: List[Dict],
    exclude_media: bool = True,
    exclude_system: bool = True,
    only_client: bool = False,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
) -> List[Dict]:
    """
    Filtra mensajes segun criterios.

    Args:
        messages: Lista de mensajes parseados
        exclude_media: Excluir mensajes de media
        exclude_system: Excluir mensajes de sistema
        only_client: Solo mensajes del cliente
        date_from: Fecha minima (formato DD/MM/YYYY)
        date_to: Fecha maxima (formato DD/MM/YYYY)

    Returns:
        Lista filtrada de mensajes
    """
    filtered = messages.copy()

    if exclude_media:
        filtered = [m for m in filtered if not m.get("is_media", False)]

    if exclude_system:
        filtered = [m for m in filtered if not m.get("is_system", False)]

    if only_client:
        filtered = [m for m in filtered if m.get("role") == "client"]

    # Filtrado por fecha (simplificado)
    if date_from or date_to:
        # Implementar si es necesario
        pass

    return filtered


def get_conversation_stats(messages: List[Dict]) -> Dict:
    """
    Genera estadisticas de la conversacion.

    Args:
        messages: Lista de mensajes parseados

    Returns:
        Diccionario con estadisticas
    """
    if not messages:
        return {"error": "No hay mensajes"}

    total = len(messages)
    by_sender = {}
    by_role = {"client": 0, "therapist": 0, "unknown": 0}
    media_count = 0
    media_by_type = {"audio": 0, "photo": 0, "sticker": 0, "video": 0, "other": 0}
    system_count = 0
    total_words = 0

    for msg in messages:
        sender = msg.get("sender", "unknown")
        role = msg.get("role", "unknown")
        content = msg.get("content", "")

        by_sender[sender] = by_sender.get(sender, 0) + 1
        by_role[role] = by_role.get(role, 0) + 1

        if msg.get("is_media"):
            media_count += 1
            media_type = msg.get("media_type", "other")
            if media_type in media_by_type:
                media_by_type[media_type] += 1
            else:
                media_by_type["other"] += 1
        if msg.get("is_system"):
            system_count += 1

        total_words += len(content.split())

    return {
        "total_messages": total,
        "by_sender": by_sender,
        "by_role": by_role,
        "media_messages": media_count,
        "media_by_type": media_by_type,
        "system_messages": system_count,
        "total_words": total_words,
        "avg_words_per_message": round(total_words / total, 1) if total > 0 else 0,
    }


def format_for_analysis(
    messages: List[Dict],
    include_timestamps: bool = False,
    max_messages: Optional[int] = None,
) -> str:
    """
    Formatea mensajes para enviar a la IA.

    Args:
        messages: Lista de mensajes parseados
        include_timestamps: Incluir fecha/hora
        max_messages: Limitar cantidad de mensajes

    Returns:
        Texto formateado para analisis
    """
    filtered = filter_messages(messages, exclude_media=True, exclude_system=True)

    if max_messages:
        filtered = filtered[-max_messages:]  # Ultimos N mensajes

    lines = []
    for msg in filtered:
        role = msg.get("role", "unknown")
        sender = msg.get("sender", "???")
        content = msg.get("content", "")

        # Usar etiquetas claras
        if role == "client":
            label = "CLIENTE"
        elif role == "therapist":
            label = "TERAPEUTA"
        else:
            label = sender

        if include_timestamps:
            ts = msg.get("date", "") + " " + msg.get("time", "")
            lines.append(f"[{ts}] {label}: {content}")
        else:
            lines.append(f"{label}: {content}")

    return "\n".join(lines)


# CLI simple para testing
if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) < 2:
        print("Uso: python whatsapp_parser.py <archivo_export.txt> [nombre_cliente]")
        print("Ejemplo: python whatsapp_parser.py chat.txt 'Juan Perez'")
        sys.exit(1)

    file_path = sys.argv[1]
    client_name = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        print(f"Parseando: {file_path}")
        if client_name:
            print(f"Cliente: {client_name}")

        messages = parse_whatsapp_export(file_path, client_name=client_name)

        print(f"\nMensajes encontrados: {len(messages)}")

        stats = get_conversation_stats(messages)
        print(f"\nEstadisticas:")
        print(json.dumps(stats, indent=2, ensure_ascii=False))

        print(f"\nPrimeros 5 mensajes:")
        for msg in messages[:5]:
            print(f"  [{msg.get('date')}] {msg.get('sender')}: {msg.get('content')[:50]}...")

        # Guardar resultado
        output_file = Path(file_path).stem + "_parsed.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)

        print(f"\nResultado guardado en: {output_file}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
