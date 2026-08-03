from docx import Document

doc = Document(r'PROYECTO_FINAL_INVESTIGACION_APA7.docx')
sections = []

for p in doc.paragraphs[:200]:
    if 'Heading 1' in p.style.name and p.text.strip():
        sections.append(p.text.strip())

print("MAJOR SECTIONS (Heading 1):")
for i, section in enumerate(sections[:20], 1):
    print(f"{i}. {section}")
