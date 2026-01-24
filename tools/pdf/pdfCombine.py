import sys
import os

def install_and_import():
    try:
        from PyPDF2 import PdfMerger
        return PdfMerger
    except ImportError:
        print("PyPDF2 is not installed. Attempting to install...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
            from PyPDF2 import PdfMerger
            return PdfMerger
        except Exception as e:
            print(f"Failed to install PyPDF2: {e}")
            print("Please run: pip install PyPDF2")
            sys.exit(1)

def combine_pdfs(pdf_list):
    if len(pdf_list) < 2:
        print("Usage: python3 pdfCombine.py <pdf1> <pdf2> [others...]")
        print("Error: Please provide at least 2 PDF files.")
        sys.exit(1)

    PdfMerger = install_and_import()
    merger = PdfMerger()
    
    # Determine output directory from the first PDF
    first_pdf_path = pdf_list[0]
    # Use absolute path to ensure we get the correct directory
    abs_first_path = os.path.abspath(first_pdf_path)
    output_dir = os.path.dirname(abs_first_path)
    output_path = os.path.join(output_dir, "combined.pdf")

    print(f"Merging {len(pdf_list)} files...")
    
    try:
        for pdf in pdf_list:
            if not os.path.exists(pdf):
                print(f"Error: File not found: {pdf}")
                # Close properly before exiting
                merger.close()
                sys.exit(1)
            print(f"Adding: {pdf}")
            merger.append(pdf)

        merger.write(output_path)
        print(f"Success! Combined PDF saved to: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        merger.close()

if __name__ == "__main__":
    combine_pdfs(sys.argv[1:])
