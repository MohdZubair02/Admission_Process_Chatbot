import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Download the NLTK dependency (only needed once)
nltk.download('punkt')

pairs = [
    # Greetings
    (r"hi|hello|hey|greetings", ["Hello! How can I assist you with admissions?"]),
    (r"good (morning|afternoon|evening)", ["Good %1! How can I help you?"]),
    (r"how are you\??", ["I'm just a bot, but I'm here to help! How can I assist?"]),
    
    # Program Details
    (r"(what|which) programs (do you offer|are available)\??",
    [
        "We offer the following programs:\n- Bachelor of Science (B.Sc.)\n- Bachelor of Arts (B.A.)\n- Master of Science (M.Sc.)\n- Master of Arts (M.A.)\n- Ph.D. programs."
    ]),
    (r"do you have (engineering|business|arts|science) programs\??",
    [
        "Yes, we offer programs in %1. You can contact our admissions office for more details."
    ]),
    (r"what undergraduate programs do you offer\??",
    [
        "Our undergraduate programs include:\n- Computer Science\n- Business Administration\n- Mechanical Engineering\n- Fine Arts\n- Biotechnology."
    ]),
    (r"what postgraduate programs are available\??",
    [
        "Our postgraduate programs include:\n- Data Science\n- Business Analytics\n- Civil Engineering\n- Digital Marketing\n- Microbiology."
    ]),
    (r"what is the duration of the (undergraduate|postgraduate|ph.d.) program\??",
    [
        "The duration of the %1 program is:\n- Undergraduate: 3-4 years\n- Postgraduate: 1-2 years\n- Ph.D.: 4-6 years"
    ]),
    
    # Admission Process
    (r"(how do I|steps to|guide to) apply for admission\??",
    [
        "To apply for admission:\n1. Visit our website.\n2. Choose your program.\n3. Fill out the online application form.\n4. Submit the required documents.\n5. Pay the application fee."
    ]),
    (r"do you accept (online|digital) applications\??",
    [
        "Yes, all applications are processed online. Please visit our admissions portal to apply."
    ]),
    (r"what documents (are needed|do I need) for application\??",
    [
        "Required documents include:\n- Academic transcripts\n- ID proof\n- Recommendation letters\n- Statement of Purpose\n- Resume (for postgraduate programs)."
    ]),
    (r"do I need to take an entrance exam\??",
    [
        "Some programs may require an entrance exam. Please check the specific program page for detailed requirements."
    ]),
    (r"what is the application fee\??",
    [
        "The application fee is:\n- Undergraduate: ₹7,75,000\n- Postgraduate: ₹4,00,000\n- Ph.D.: ₹10,00,000."
    ]),
    
    # Eligibility and Requirements
    (r"(what are|tell me about|list) eligibility criteria\??",
    [
        "Eligibility criteria:\n- Undergraduate: High school diploma.\n- Postgraduate: Bachelor's degree with a minimum of 50% marks.\n- Ph.D.: Master's degree with research experience."
    ]),
    (r"can I apply with (low grades|a gap year|work experience)\??",
    [
        "Eligibility depends on your profile. Please contact the admissions office for personalized guidance."
    ]),
    (r"what are the requirements for international students\??",
    [
        "International students need:\n- Valid passport\n- Proof of English proficiency (TOEFL/IELTS)\n- Academic transcripts\n- Financial proof for tuition and living expenses."
    ]),
    (r"can I apply for a program without an IELTS score\??",
    [
        "In some cases, alternative English proficiency tests or proof of prior education in English may be accepted. Please contact the admissions office for specific guidelines."
    ]),
    
    # Scholarships and Financial Aid
    (r"do you offer scholarships\??",
    [
        "Yes, we offer merit-based and need-based scholarships. Please visit our scholarships page or contact the admissions office."
    ]),
    (r"what scholarships are available\??",
    [
        "We offer a range of scholarships, including:\n- Merit-based Scholarships\n- Need-based Scholarships\n- Sports Scholarships\n- Scholarships for International Students."
    ]),
    (r"how can I apply for a scholarship\??",
    [
        "You can apply for scholarships during your program application by filling out the scholarship section."
    ]),
    (r"are there scholarships for (international students|working professionals)\??",
    [
        "Yes, we have scholarships for %1. Check the scholarships page for more details."
    ]),
    (r"can I apply for financial aid\??",
    [
        "Yes, financial aid options are available for eligible students. Please check the financial aid section on our website for details."
    ]),
    
    # Application Deadlines
    (r"(what|tell me about|provide) (the|your)? application deadlines\??",
    [
        "Application deadlines are as follows:\n- Undergraduate: July 15, 2024\n- Postgraduate: June 30, 2024\n- Ph.D.: September 1, 2024."
    ]),
    (r"can I still apply for (undergraduate|postgraduate|ph.d.) programs\??",
    [
        "The deadline for %1 programs is as follows:\n- Undergraduate: July 15, 2024\n- Postgraduate: June 30, 2024\n- Ph.D.: September 1, 2024."
    ]),
    (r"when does the admission process start\??",
    [
        "Admissions for the next session begin on April 1, 2024. Early applications are encouraged."
    ]),

    # Campus and Accommodation Information
    (r"(what can you tell me|tell me about) the campus\??",
    [
        "Our campus is located in a beautiful setting with state-of-the-art facilities, libraries, laboratories, and sports complexes."
    ]),
    (r"(where is|location of) your campus\??",
    [
        "Our campus is located at 123 University Avenue, Cityname, Country."
    ]),
    (r"do you have (hostels|accommodation)\??",
    [
        "Yes, we have on-campus hostels for students. Both shared and single rooms are available."
    ]),
    (r"what is the fee for hostel accommodation\??",
    [
        "Hostel fees start at $300/month for shared rooms and $500/month for single rooms."
    ]),

    # Extracurricular and Student Life
    (r"(what|tell me about) extracurricular activities\??",
    [
        "We offer a range of extracurricular activities, including sports, cultural clubs, and technical societies."
    ]),
    (r"do you have sports facilities\??",
    [
        "Yes, we have sports facilities for basketball, football, swimming, and more."
    ]),
    (r"do you provide transportation\??",
    [
        "Yes, we have a well-connected campus shuttle service."
    ]),
    (r"can I join a student club\??",
    [
        "Absolutely! We have various student clubs for different interests including sports, music, and social causes."
    ]),

    # Contact Information
    (r"(how can I|where can I|ways to) contact the admissions office\??",
    [
        "You can reach us at:\n- Phone: +91-234-567-8901\n- Email: admissions@coeruniversity.ac.in\n- Office Hours: Monday to Friday, 9 AM to 5 PM."
    ]),
    (r"(what is|give me) (your|the) (phone number|email address)\??",
    [
        "Our phone number is +91-234-567-8901, and our email address is admissions@coeruniversity.ac.in."
    ]),

    # FAQ and Generic Responses
    (r"(thank you|thanks)", ["You're welcome! Let me know if you have more questions."]),
    (r"(bye|quit|exit)", ["Goodbye! Have a great day!"]),
    (r"(.*)", ["I'm sorry, I didn't understand that. Could you please rephrase your question?"])
    
]

# Create the chatbot instance
chatbot = Chat(pairs, reflections)

# Function to handle the user input and chatbot response
def send_message(event=None):  # Added `event` parameter for key binding
    user_input = user_input_box.get()
    if user_input.strip():
        chat_history.insert(tk.END, f"You: {user_input}\n")
        user_input_box.delete(0, tk.END)

        if user_input.lower() in ['bye', 'quit']:
            chat_history.insert(tk.END, "ChatBot: Goodbye! Have a great day!\n")
            root.destroy()
        else:
            response = chatbot.respond(user_input)
            chat_history.insert(tk.END, f"ChatBot: {response}\n")
                    
        # Scroll to the last message
        chat_history.see(tk.END)

# Adjust the size of the input box dynamically based on the window size
def adjust_input_box(event):
    new_width = int(event.width / 10)  # Adjust width dynamically
    user_input_box.config(width=new_width)

# Setting up the graphical interface using Tkinter
root = tk.Tk()
root.title("Admission Chatbot")
root.geometry("500x600")

# Bind the resize event to dynamically adjust input box
root.bind("<Configure>", adjust_input_box)

# Chat history display (scrollable text area)
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='normal', height=30, width=58)
chat_history.pack(pady=10, fill=tk.BOTH, expand=True)

# Bottom frame to hold the input box and button
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# User input field
user_input_box = tk.Entry(bottom_frame, width=50)
user_input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
user_input_box.bind("<Return>", send_message)  # Bind the Enter key to `send_message`

# Send button
send_button = tk.Button(bottom_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=5)

# Run the Tkinter event loop
root.mainloop()
