# ----------------------------------------
# Simple Chatbot Using Function
# ----------------------------------------

#Function
def chat(user_input):
    user_input = user_input.lower()

    # Responses limit based according to insturctions
    if user_input in ['hello', 'hi','hey','hii']:
        return 'Hi! How are you? 😊'
    
    elif user_input == 'how are you':
        return'I am Fine, thanks! what about you?😌'
    
    elif user_input in ['i am fine','i am good','i am great']:
        return 'Happy to hear that!😍👌'
    
    elif user_input =='what about you':
        return 'I am doing great, chatting with you! 👍'
    
    elif user_input== 'how was your day':
        return 'My day has been wonderful! How about yours?🤌☀️'
    
    elif user_input == 'what is your current role':
        return 'I am a chatbot! Are you a student, professional or other?'
    
    elif user_input in ['student','professional','other']:
        return f'Nice! Being a {user_input} is awesome!🙌 '
    
    elif user_input == 'bye':
        return 'Goodbye! Have a nice day!💫❤️'
    
    else:
        return 'Sorry! I do not understand that. Can you ask something else?'
    
# main loop
def chatbot():
        print('Chatbot: Hello! lets chat. Type bye to exit')

        while True:
            user_input = input('You: ')
            reply = chat(user_input)
            print('Chatbot: ',reply)

            if user_input.lower() == 'bye':
                break

# start call function
chatbot()            
