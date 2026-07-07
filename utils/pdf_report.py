from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(report_text):

    filename = "Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Heading1"]
        )
    )

    story.append(Spacer(1,20))

    for line in report_text.split("\n"):

        story.append(
            Paragraph(
                line,
                styles["BodyText"]
            )
        )

    doc.build(story)

    return filename