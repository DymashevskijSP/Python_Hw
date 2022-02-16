from pdflatex import PDFLaTeX
import subprocess


def get_max_line_size(current, index, array):
    if index == len(array):
        return current
    return max(len(array[index]), get_max_line_size(current, index + 1, array))


def printline(fout, line, index, left):
    if index < len(line):
        fout.write(line[index])
    if left == 1:
        fout.write("\\\\ \n")
        return
    fout.write("&")
    printline(fout, line, index + 1, left - 1)


def write_begin(fout):
    fout.write("\\documentclass[a4paper, 12pt]{article}\n")
    fout.write("\\begin{document}\n")


def write_table_latex(fout, array):
    fout.write("\\begin{center}\n")
    fout.write("\\begin{tabular}{")
    line_size = get_max_line_size(1, 0, array)
    fout.write("c " * line_size)
    fout.write("}\n")
    for line in array:
        printline(fout, line, 0, line_size)
    fout.write("\\end{tabular}\n")
    fout.write("\\end{center}\n")


def write_end(fout):
    fout.write("\\end{document}")


def generate_pdf(array):
    with open("artifacts/table.tex", "w") as fout:
        write_begin(fout)
        write_table_latex(fout, array)
        write_end(fout)
    with open("artifacts/table.pdf", "wb") as out_pdf:
        out_pdf.write(
            PDFLaTeX.from_texfile('artifacts/table.tex').create_pdf()[0])



def write_full():
    with open("table.tex", "w") as fout:
        write_begin(fout)
        write_table_latex(fout, [["1", "2", "3"], ["2", "3"], ["3"]])
        write_end(fout)
    subprocess.call(executable="rm", args=(" ", "table.tex"))

write_full()
