import os, re, json

from pypdf import PdfReader

def check_for_edge_case_and_handle(flashcard):
    answer = flashcard['fields']['answer']

    if answer == 'Privileged Access Management':
        flashcard['fields']['question'] = 'PAM (access)'
    elif answer == 'Pluggable Authentication Modules':
        flashcard['fields']['question'] = 'PAM (auth)'
    elif answer == 'DSS Payment Card Industry Data Security Standard':
        flashcard['fields']['question'] = 'PCI DSS'
        flashcard['fields']['answer'] = 'Payment Card Industry Data Security Standard'
    elif answer == 'OTG USB On-The-Go':
        flashcard['fields']['question'] = 'USB OTG'
        flashcard['fields']['answer'] = 'Universal Serial Bus On-The-Go'

if __name__ == '__main__':
    # Open the attached PDF file with exam objectives.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_file_path = os.path.join(script_dir, 'comptia-sec-exam-objectives.pdf')
    
    reader = PdfReader(pdf_file_path)

    text_parts = []

    # Use closures to modify the function's behavior.    
    top_y = 520
    bottom_y = 50

    def visitor_body(text, cm, tm, fontDict, fontSize):
        y = tm[5]
        if y > bottom_y and y < top_y:
            text_parts.append(text)

    # Handle the 20th page individually due to the header.
    page = reader.pages[19]
    page.extract_text(visitor_text=visitor_body)

    # Handle the rest of the pages with the acronyms list.
    ACRONYMS_LIST_FIRST_PAGE_IDX = 20
    ACRONYMS_LIST_LAST_PAGE_IDX = 22

    top_y = 720
    bottom_y = 50

    for page_idx in range(ACRONYMS_LIST_FIRST_PAGE_IDX, ACRONYMS_LIST_LAST_PAGE_IDX + 1):
        page = reader.pages[page_idx]
        page.extract_text(visitor_text=visitor_body)

    # Build Flashcard fixture file with the extracted acronyms.
    flashcards = []
    idx = 0
    for txt in text_parts:
        # Sanitize the extracted lines
        if not txt.isspace() and not txt == '':
            line = txt.replace('\n', ' ').replace('\r', '')
            
            if re.match(r'\s', line):
                flashcards[idx-1]['fields']['answer'] += line
            else:
                words = line.split()
                flashcards.append({
                    'model': 'flashcards.flashcard',
                    'pk': str(idx + 1),
                    'fields': {
                        'question': words[0],
                        'answer': ' '.join(words[1:])
                    }
                })
                idx += 1

            check_for_edge_case_and_handle(flashcards[idx-1])
    
    # Remove duplicated acronyms (present in the original PDF document).
    unique_answers = {card['fields']['answer']:card for card in flashcards}
    flashcards = [card for card in unique_answers.values()]

    # Dump flashcard objects to the JSON file.
    with open(os.path.join(script_dir, '0001_Flashcard.json'), 'w', encoding='utf-8') as f:
        json.dump(flashcards, f, ensure_ascii=False)