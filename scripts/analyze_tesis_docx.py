import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import json

def rgb_to_hex(rgb):
    """Convert RGBColor to hex string"""
    if rgb is None:
        return "Auto"
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def analyze_docx_formatting(file_path):
    """Analyze detailed formatting of a DOCX file"""
    try:
        doc = docx.Document(file_path)

        analysis = {
            "document_properties": {},
            "sections": [],
            "styles_used": set(),
            "formatting_issues": [],
            "recommendations": []
        }

        # Analyze sections
        for idx, section in enumerate(doc.sections):
            section_info = {
                "section_number": idx + 1,
                "page_width": section.page_width.inches if section.page_width else "Unknown",
                "page_height": section.page_height.inches if section.page_height else "Unknown",
                "top_margin": section.top_margin.inches if section.top_margin else "Unknown",
                "bottom_margin": section.bottom_margin.inches if section.bottom_margin else "Unknown",
                "left_margin": section.left_margin.inches if section.left_margin else "Unknown",
                "right_margin": section.right_margin.inches if section.right_margin else "Unknown",
            }
            analysis["sections"].append(section_info)

        # Analyze paragraphs and formatting
        paragraph_analysis = []

        for para_idx, para in enumerate(doc.paragraphs):
            if not para.text.strip():
                continue

            para_info = {
                "paragraph_number": para_idx + 1,
                "text_preview": para.text[:100] + ("..." if len(para.text) > 100 else ""),
                "style_name": para.style.name if para.style else "None",
                "alignment": str(para.alignment) if para.alignment else "LEFT",
                "space_before": para.paragraph_format.space_before.pt if para.paragraph_format.space_before else 0,
                "space_after": para.paragraph_format.space_after.pt if para.paragraph_format.space_after else 0,
                "line_spacing": para.paragraph_format.line_spacing if para.paragraph_format.line_spacing else "Single",
                "first_line_indent": para.paragraph_format.first_line_indent.inches if para.paragraph_format.first_line_indent else 0,
                "left_indent": para.paragraph_format.left_indent.inches if para.paragraph_format.left_indent else 0,
                "runs": []
            }

            # Analyze runs (character formatting)
            for run in para.runs:
                if not run.text.strip():
                    continue

                run_info = {
                    "text_preview": run.text[:50] + ("..." if len(run.text) > 50 else ""),
                    "font_name": run.font.name if run.font.name else "Default",
                    "font_size": run.font.size.pt if run.font.size else "Default",
                    "bold": run.font.bold if run.font.bold is not None else False,
                    "italic": run.font.italic if run.font.italic is not None else False,
                    "underline": run.font.underline if run.font.underline else False,
                    "color": rgb_to_hex(run.font.color.rgb) if run.font.color and run.font.color.rgb else "Auto",
                }
                para_info["runs"].append(run_info)

            analysis["styles_used"].add(para.style.name if para.style else "None")
            paragraph_analysis.append(para_info)

        analysis["paragraph_details"] = paragraph_analysis
        analysis["styles_used"] = list(analysis["styles_used"])

        # Check for APA 7 compliance issues
        section = doc.sections[0]

        # Margin check (APA 7: 1 inch all sides)
        if section.top_margin:
            top_margin_inches = section.top_margin.inches
            if abs(top_margin_inches - 1.0) > 0.1:
                analysis["formatting_issues"].append(f"Top margin is {top_margin_inches:.2f}\" (APA 7 requires 1\")")

        if section.bottom_margin:
            bottom_margin_inches = section.bottom_margin.inches
            if abs(bottom_margin_inches - 1.0) > 0.1:
                analysis["formatting_issues"].append(f"Bottom margin is {bottom_margin_inches:.2f}\" (APA 7 requires 1\")")

        if section.left_margin:
            left_margin_inches = section.left_margin.inches
            if abs(left_margin_inches - 1.0) > 0.1:
                analysis["formatting_issues"].append(f"Left margin is {left_margin_inches:.2f}\" (APA 7 requires 1\")")

        if section.right_margin:
            right_margin_inches = section.right_margin.inches
            if abs(right_margin_inches - 1.0) > 0.1:
                analysis["formatting_issues"].append(f"Right margin is {right_margin_inches:.2f}\" (APA 7 requires 1\")")

        # Font and spacing checks
        for para in paragraph_analysis:
            for run in para["runs"]:
                # Font check (APA 7: Times New Roman 12pt or similar)
                if run["font_name"] not in ["Times New Roman", "Arial", "Calibri", "Georgia"]:
                    analysis["formatting_issues"].append(
                        f"Non-standard font '{run['font_name']}' in paragraph {para['paragraph_number']}"
                    )

                # Font size check
                if isinstance(run["font_size"], (int, float)) and run["font_size"] != 12:
                    if para["style_name"] not in ["Title", "Heading 1", "Heading 2", "Heading 3"]:
                        analysis["formatting_issues"].append(
                            f"Non-standard font size {run['font_size']}pt in paragraph {para['paragraph_number']} (APA 7 recommends 12pt)"
                        )

            # Line spacing check (APA 7: Double spacing)
            if para["line_spacing"] != 2.0 and para["line_spacing"] != "2.0":
                if para["style_name"] not in ["Title", "TOC"]:
                    analysis["formatting_issues"].append(
                        f"Line spacing is {para['line_spacing']} in paragraph {para['paragraph_number']} (APA 7 requires double spacing)"
                    )

        # Generate recommendations
        analysis["recommendations"] = [
            "Use consistent double-spacing (2.0) throughout the document",
            "Ensure all margins are exactly 1 inch",
            "Use Times New Roman 12pt for body text",
            "Heading 1 should be bold, centered",
            "Heading 2 should be bold, left-aligned",
            "Heading 3 should be bold italic, left-aligned",
            "First line of each paragraph should be indented 0.5 inches",
            "Add running head in header (shortened title, all caps, left-aligned)",
            "Add page numbers in header (right-aligned)",
            "Title page should include title (bold), author names, affiliations",
            "Use consistent spacing before/after headings"
        ]

        return analysis

    except Exception as e:
        return {"error": str(e)}

# Analyze the document
file_path = r"c:\Users\Alejandro\Documents\Ivan\lourdes\TESIS_COMPLETA_APA7.docx"
analysis = analyze_docx_formatting(file_path)

# Print formatted output
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 80)
print("TESIS DOCUMENT ANALYSIS - APA 7 PROFESSIONAL REVIEW")
print("=" * 80)

if "error" in analysis:
    print(f"\nERROR: {analysis['error']}")
else:
    # Document Properties
    print("\n[DOCUMENT STRUCTURE]")
    print("-" * 80)
    for section in analysis["sections"]:
        print(f"\nSection {section['section_number']}:")
        print(f"  Page Size: {section['page_width']}\" x {section['page_height']}\"")
        print(f"  Margins: T:{section['top_margin']}\" B:{section['bottom_margin']}\" L:{section['left_margin']}\" R:{section['right_margin']}\"")

    # Styles Used
    print("\n\n[STYLES DETECTED]")
    print("-" * 80)
    for style in sorted(analysis["styles_used"]):
        print(f"  - {style}")

    # Summary Statistics
    print("\n\n[DOCUMENT STATISTICS]")
    print("-" * 80)
    print(f"  Total paragraphs: {len(analysis['paragraph_details'])}")
    print(f"  Total styles used: {len(analysis['styles_used'])}")
    print(f"  Total formatting issues: {len(analysis['formatting_issues'])}")

    # Formatting Issues Summary
    print("\n\n[FORMATTING ISSUES SUMMARY]")
    print("-" * 80)

    # Count issue types
    spacing_issues = [i for i in analysis["formatting_issues"] if "spacing" in i.lower()]
    font_issues = [i for i in analysis["formatting_issues"] if "font" in i.lower()]
    margin_issues = [i for i in analysis["formatting_issues"] if "margin" in i.lower()]

    print(f"  Line spacing issues: {len(spacing_issues)}")
    print(f"  Font-related issues: {len(font_issues)}")
    print(f"  Margin issues: {len(margin_issues)}")

    # Show first 30 issues
    print("\n\n[FIRST 30 FORMATTING ISSUES]")
    print("-" * 80)
    if analysis["formatting_issues"]:
        for idx, issue in enumerate(analysis["formatting_issues"][:30], 1):
            print(f"  {idx}. {issue}")
        if len(analysis["formatting_issues"]) > 30:
            print(f"\n  ... and {len(analysis['formatting_issues']) - 30} more issues")
    else:
        print("  OK No major formatting issues detected")

    # Detailed Paragraph Analysis (first 25 paragraphs)
    print("\n\n[PARAGRAPH-BY-PARAGRAPH ANALYSIS (First 25)]")
    print("-" * 80)
    for para in analysis["paragraph_details"][:25]:
        print(f"\n[Para {para['paragraph_number']}] Style: {para['style_name']}")
        print(f"  Text: {para['text_preview']}")
        print(f"  Alignment: {para['alignment']}")
        print(f"  Spacing: Before={para['space_before']}pt, After={para['space_after']}pt, Line={para['line_spacing']}")
        print(f"  Indent: First={para['first_line_indent']}\", Left={para['left_indent']}\"")
        if para["runs"]:
            print(f"  Font Details:")
            for run in para["runs"][:2]:  # Show first 2 runs
                print(f"    - {run['font_name']} {run['font_size']}pt, Bold:{run['bold']}, Italic:{run['italic']}, Color:{run['color']}")

    if len(analysis["paragraph_details"]) > 25:
        print(f"\n  ... and {len(analysis['paragraph_details']) - 25} more paragraphs")

    # Recommendations
    print("\n\n[RECOMMENDATIONS FOR PROFESSIONAL APA 7 FORMATTING]")
    print("-" * 80)
    for idx, rec in enumerate(analysis["recommendations"], 1):
        print(f"  {idx}. {rec}")

    # Overall Assessment
    print("\n\n[OVERALL ASSESSMENT]")
    print("-" * 80)

    total_issues = len(analysis["formatting_issues"])
    total_paras = len(analysis["paragraph_details"])

    if total_issues == 0:
        print("  STATUS: EXCELLENT - Document meets APA 7 standards")
        rating = 10
    elif total_issues < total_paras * 0.1:
        print("  STATUS: GOOD - Minor formatting adjustments needed")
        rating = 8
    elif total_issues < total_paras * 0.3:
        print("  STATUS: FAIR - Moderate formatting issues present")
        rating = 6
    elif total_issues < total_paras * 0.5:
        print("  STATUS: NEEDS WORK - Significant formatting problems")
        rating = 4
    else:
        print("  STATUS: CRITICAL - Major reformatting required")
        rating = 2

    print(f"  RATING: {rating}/10")
    print(f"  ISSUES/PARAGRAPH RATIO: {total_issues/total_paras:.2f}")

print("\n" + "=" * 80)
