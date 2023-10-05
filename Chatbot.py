import openai
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

def get_openai_response(prompt):
    """Call OpenAI API and get response."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are meeting someone new."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def format_prompt(background, goal, time): 
    main_propmot =  "Based on background of this person: " + background + '-----------' + "and the " + goal + " for this " + time + " meeting, please come up with 5 questions we can discuss. Ask questions based on their relevant job experience and be specific."
    format = "Put the questions in just question formats and no other things"
    return main_propmot + format

def main():
    st.title("💬 Meeting Prep")
    st.caption("use your all the info to help you prep for the meeting")


    connection_background = st.text_area(
    "Your connection's linkedin background")

    your_goals = st.text_area(
    "Your goals")

    time_option = st.selectbox(
    'How long is the meeting?',
    ('30min', '60min'))

    print(connection_background)
    print(format_prompt(background=connection_background, goal=your_goals, time=time_option))
    
    if st.button("Prep it!"):
        if connection_background and your_goals and time_option:
            response = get_openai_response(format_prompt(background=connection_background, goal=your_goals, time=time_option))
            st.subheader("Questions:")
            st.subheader(response)
            # for res in response: 
            #     st.subheader(res, divider='rainbow')

        else:
            st.warning("Please enter a prompt.")

if __name__ == "__main__":
    main()
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     openai.api_key = openai_api_key
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message
#     st.session_state.messages.append(msg)
#     st.chat_message("assistant").write(msg.content)