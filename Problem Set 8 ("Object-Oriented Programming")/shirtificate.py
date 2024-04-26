from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Set font
        self.set_font("helvetica", "B", 34)
        # Move cursor
        self.cell(80)
        # Print title
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C", new_x="LMARGIN", new_y="NEXT")
        # line break
        self.ln(20)

name = input("Your name: ")

pdf = PDF()
pdf.add_page()
pdf.set_x(0)
pdf.image("shirtificate.png")
pdf.set_font("helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
s = f"{name} took CS50"
width = pdf.get_string_width(s)
x = (210 - width) / 2
pdf.set_x(x)
pdf.cell(50, -260, s)


pdf.output("shirtificate.pdf")

"""


self.set_font("helvetica", "B", 15)
        # Calculating width of title and setting cursor position:
        width = pdf.get_string_width(self.title) + 6
        self.set_x((210 - width) / 2)
        # Setting colors for frame, background and text:
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        # Setting thickness of the frame (1 mm)
        self.set_line_width(1)
        # Printing title:
        self.cell(
            width,
            9,
            self.title,
            border=1,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
            fill=True,
        )

"""