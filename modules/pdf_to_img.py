import fitz  # PyMuPDF
from PIL import Image

def convert_pdf_page_to_pil_image(pdf_data):
    """
    Convert a specific page from a PDF to a PIL image.

    Args:
        pdf_data (dict): A dictionary containing 'page' (page number) and 'source' (PDF file path) keys.

    Returns:
        PIL.Image.Image: The converted image.
    """
    page_number = pdf_data.get('page', 0)
    pdf_source = pdf_data.get('source')

    if not pdf_source:
        raise ValueError("Source PDF file path is missing.")

    try:
        pdf_document = fitz.open(pdf_source)
        if 0 <= page_number < pdf_document.page_count:
            pdf_page = pdf_document[page_number]
            image = pdf_page.get_pixmap()
            pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
            return pil_image
        else:
            raise ValueError("Invalid page number.")
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if pdf_document:
            pdf_document.close()


def remove_duplicate_dict(list_of_dict):
    unique_dictionaries = []
    seen = set()  # Keep track of seen dictionaries

    for d in list_of_dict:
        # Convert the dictionary to a frozenset to make it hashable
        frozen_d = frozenset(d.items())
        
        if frozen_d not in seen:
            seen.add(frozen_d)
            unique_dictionaries.append(d)

    return unique_dictionaries
