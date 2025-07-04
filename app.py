import streamlit as st
import ollama
import time

# Configure page
st.set_page_config(
    page_title="CommonChat AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful dark blue theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a202c 50%, #2d3748 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* Title styling */
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 8px rgba(102, 126, 234, 0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #a0aec0;
        font-size: 1.1rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #1a202c 0%, #2d3748 100%);
        border-right: 2px solid #4a5568;
    }
    
    .sidebar-title {
        color: #667eea;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Custom slider styling */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSlider > div > div > div > div > div {
        background: #667eea;
        border: 2px solid #4a5568;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background: #2d3748;
        border: 1px solid #4a5568;
        border-radius: 8px;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background: rgba(45, 55, 72, 0.6);
        border: 1px solid #4a5568;
        border-radius: 12px;
        margin: 0.5rem 0;
        backdrop-filter: blur(10px);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        max-width: 85%;
    }
    
    /* User message */
    .stChatMessage[data-testid="user-message"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin-left: auto;
    }
    
    /* Assistant message */
    .stChatMessage[data-testid="assistant-message"] {
        background: rgba(26, 32, 44, 0.8);
        border-left: 3px solid #667eea;
        margin-right: auto;
    }
    
    /* Chat input styling */
    .stChatInput > div {
        background: #2d3748;
        border: 2px solid #4a5568;
        border-radius: 25px;
        backdrop-filter: blur(10px);
    }
    
    .stChatInput input {
        background: transparent;
        color: #e2e8f0;
        font-size: 1rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }
    
    /* Info box styling */
    .info-box {
        background: rgba(26, 32, 44, 0.8);
        border: 1px solid #4a5568;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    
    /* Custom metrics */
    .metric-card {
        background: rgba(45, 55, 72, 0.6);
        border: 1px solid #4a5568;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    
    /* Animated gradient background for chat area */
    .chat-container {
        background: rgba(26, 32, 44, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(102, 126, 234, 0.2);
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a202c;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title with custom styling
st.markdown('<h1 class="main-title">🚀 CommonChat AI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Private, Intelligent Conversation Partner</p>', unsafe_allow_html=True)

# Enhanced sidebar with clean design
with st.sidebar:
    st.markdown('<h2 class="sidebar-title">⚙️ Settings</h2>', unsafe_allow_html=True)
    
    # Temperature control
    st.markdown("**Temperature**")
    temperature = st.slider(
        "",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Controls creativity"
    )
    
    # Model selection
    st.markdown("**Model**")
    model_name = st.selectbox(
        "",
        ["gemma3", "llama3", "mistral", "codellama"],
        index=0,
        help="Choose AI model"
    )
    
    st.markdown("---")
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    
    # Simple info
    st.markdown("""
    <div class='info-box'>
        <p style='margin: 0; color: #a0aec0; font-size: 0.9rem; text-align: center;'>
            🔐 Private & Local<br>
            ⚡ Fast & Responsive
        </p>
    </div>
    """, unsafe_allow_html=True)

# Main chat area with clean design
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# Display welcome message if no chat history
if not st.session_state.messages:
    st.markdown("""
    <div style='text-align: center; padding: 2rem; color: #a0aec0;'>
        <h3 style='color: #667eea;'>👋 Welcome to CommonChat AI</h3>
        <p>Start a conversation by typing your message below.</p>
    </div>
    """, unsafe_allow_html=True)

# Display chat messages with clean styling
for i, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        if message["role"] == "user":
            st.markdown(message['content'])
        else:
            st.markdown(message['content'])

st.markdown('</div>', unsafe_allow_html=True)

# Clean chat input
if prompt := st.chat_input("💭 What's on your mind?", key="chat_input"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Add thinking indicator
        with st.spinner("Thinking..."):
            try:
                # Stream the response from Ollama
                response = ollama.chat(
                    model=model_name,
                    messages=st.session_state.messages,
                    stream=True,
                    options={
                        'temperature': temperature,
                        'top_p': 0.9,
                        'top_k': 40
                    }
                )
                
                # Clean streaming
                for chunk in response:
                    if 'message' in chunk and 'content' in chunk['message']:
                        full_response += chunk['message']['content']
                        message_placeholder.markdown(full_response + "▊")
                
                # Final message without cursor
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                error_message = f"Error: {str(e)}"
                message_placeholder.markdown(error_message)
                full_response = error_message
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Simple footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #718096; font-size: 0.9rem; padding: 1rem;'>
    <p><strong>CommonChat AI</strong> - Powered by Ollama</p>
</div>
""", unsafe_allow_html=True)