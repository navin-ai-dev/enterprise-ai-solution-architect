from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    PageBreak,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(results):

    filename = "enterprise_solution_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Enterprise AI Solution Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(Spacer(1, 12))

    sections = {

    "Requirement Analysis":
    results["requirements"],

    "User Stories":
    results["stories"],

    "API Design":
    results["api"],

    "Architecture Diagram":
    results["architecture"]
}

    for heading, content in sections.items():

        elements.append(
            Paragraph(
                heading,
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                content.replace("\n", "<br/>"),
                styles["BodyText"]
            )
        )

        elements.append(PageBreak())

    doc.build(elements)

    return filename