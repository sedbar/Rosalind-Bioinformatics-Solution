# Rosalind-Bioinformatics-Solution/RNA/rna.py

def dna_to_rna(dna_sequence):
    """
    این تابع یک رشته DNA را به رشته RNA متناظر آن تبدیل می کند.
    کاراکتر 'T' با 'U' جایگزین می شود.
    """
    rna_sequence = dna_sequence.replace('T', 'U')
    return rna_sequence

if __name__ == "__main__":
    # گرفتن ورودی از کاربر (یا استفاده از ورودی نمونه برای تست)
    dna_input = input("لطفاً رشته DNA را وارد کنید: ")
    # dna_input = "GATGGAACTTGACTACGTCTAGGAAC" # می توانید برای تست از این خط استفاده کنید

    rna_output = dna_to_rna(dna_input)
    print(rna_output)