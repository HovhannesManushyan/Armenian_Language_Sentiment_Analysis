from tika import parser
import re
import os


class PDFextract:

    # extracting data from pdf file
    def extract_pdf_text(self, file_path):
        text = parser.from_file(file_path)["content"]
        return text

    # cleaning the string
    def pdf_preprocessing(self, text):
        # remove all non-armenian letters more than one spaces and split by :
        text = re.sub(u"[^\u0530-\u058f:\s]", "", text)
        text = text.replace("\n", "")
        text = re.sub("  +", " ", text)
        text = text.replace(":", "։")
        text = text.split("։")
        return text

    # writing data to the txt file
    def write_in_file(self, my_list, current_txt_heading):

        # check if text is more than 100 lines
        if len(my_list) > 100:
            # check if the biggest line is at least 30 characters
            if len(max(my_list, key=len)) > 30:
                with open(current_txt_heading, "w", encoding="utf-8") as f1:
                    for list_item in my_list:
                        f1.write(list_item + "\n")


# list all names from pdfs/ folder
list_of_pdfs = [file for file in os.listdir("pdfs/") if file.endswith(".pdf")]

pdf = PDFextract()


for current_name in list_of_pdfs:

    current_pdf = "pdfs/" + current_name[0:-4] + ".pdf"
    current_txt = "cors/" + current_name[0:-4] + ".cor"
    current_text = pdf.extract_pdf_text(current_pdf)

    # check if the text is not empty
    if current_text:
        pdf.write_in_file(pdf.pdf_preprocessing(current_text), current_txt)