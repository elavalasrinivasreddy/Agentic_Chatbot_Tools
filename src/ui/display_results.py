import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

class DisplayResults:
    def __init__(self,use_case,workflow,user_input):
        self.use_case = use_case
        self.workflow = workflow
        self.user_input = user_input

    def display(self, messages):
        use_case = self.use_case
        workflow = self.workflow
        
        full_response = ""
        if use_case == "Chatbot":
            # Stream the response from the workflow
            for event in workflow.stream({"messages": messages}):
                for value in event.values():
                    if 'messages' in value:
                        response_msg = value['messages']
                        if isinstance(response_msg, list):
                            response_msg = response_msg[-1]
                        
                        # Use a context manager for the assistant message
                        with st.chat_message("assistant"):
                            message_placeholder = st.empty()
                            full_response += response_msg.content
                            message_placeholder.markdown(full_response)
            
            return full_response

        elif use_case == "Chatbot with Web Search": # display the tool message if any
            # Stream the response from the workflow
            for event in workflow.stream({"messages": messages}):
                for value in event.values():
                    if 'messages' in value:
                        response_msg = value['messages']
                        if isinstance(response_msg, list):
                            response_msg = response_msg[-1]
                        
                        # displaying tool message if any
                        # if isinstance(response_msg, ToolMessage):
                        #     with st.chat_message("tool"):
                        #         st.markdown(response_msg.content)

                        # Use a context manager for the assistant message
                        if isinstance(response_msg, AIMessage):
                            with st.chat_message("assistant"):
                                message_placeholder = st.empty()
                                full_response += response_msg.content
                                message_placeholder.markdown(full_response)
                        
            return full_response
        