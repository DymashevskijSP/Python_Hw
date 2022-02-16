from pdflatex import PDFLaTeX
import subprocess


def get_max_line_size(current, index, array):
    if index == len(array):
        return current
    return max(len(array[index]), get_max_line_size(current, index + 1, array))


def printline(line, index, left):
    if index < len(line):
        if left == 1:
            return line[index] + "\\\\ \n"
        return line[index]+"&" + printline(line, index + 1, left - 1)
    if left == 1:
        return "\\\\ \n"
    return "&" + printline(line, index + 1, left - 1)


def write_begin():
    return "\\documentclass[a4paper, 12pt]{article}\n \\begin{document}\n"


def write_lines(array, line_size, index):
    if index == len(array):
        return ""
    return printline(array[index], index, line_size) + write_lines(array, line_size, index + 1)


def write_table_latex(array):
    line_size = get_max_line_size(1, 0, array)
    return "\\begin{center}\n" + "\\begin{tabular}{" + "c " * line_size + "}\n" + write_lines(array, line_size,
                                                                                              0) + "\\end{tabular}\n" + "\\end{center}\n"


def write_end():
    return "\\end{document}"


def create_all_tex(array):
    return write_begin() + write_table_latex(array) + write_end()


def generate_pdf(array):
    with open("artifacts/table.tex", "w") as fout:
        fout.write(create_all_tex(array))
    with open("artifacts/table.pdf", "wb") as out_pdf:
        out_pdf.write(
            PDFLaTeX.from_texfile('artifacts/table.tex').create_pdf()[0])


def write_full(array):
    with open("artifacts/table.tex", "w") as fout:
        fout.write(create_all_tex(array))


write_full([["1", "2", "3"], ["2", "3"], ["3"]])
