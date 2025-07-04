# 🛠️ Detailed Setup Guide

This guide will walk you through setting up CommonChat AI step by step.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **Python**: Version 3.8 or higher
- **RAM**: Minimum 4GB (8GB+ recommended for larger models)
- **Storage**: At least 2GB free space for models

### Required Software

#### 1. Python Installation
If you don't have Python installed:

**Windows:**
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify installation: `python --version`

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python

# Or download from python.org
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip
```

#### 2. Ollama Installation

**Windows:**
1. Download Ollama from [ollama.ai](https://ollama.ai)
2. Run the installer
3. Open Command Prompt and verify: `ollama --version`

**macOS:**
```bash
# Using Homebrew
brew install ollama

# Or download from ollama.ai
```

**Linux:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

## 🚀 Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/hari7261/CommonChat-AI.git
cd CommonChat-AI
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Ollama Models

#### Download Models
```bash
# Download Gemma3 (default model)
ollama pull gemma3

# Optional: Download other models
ollama pull llama3
ollama pull mistral
ollama pull codellama
```

#### Verify Models
```bash
ollama list
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 🔧 Configuration

### Model Configuration
Edit the model list in `app.py` if you want to add or remove models:
```python
model_name = st.selectbox(
    "",
    ["gemma3", "llama3", "mistral", "codellama", "your-custom-model"],
    index=0,
    help="Choose AI model"
)
```

### Streamlit Configuration
Create `.streamlit/config.toml` for custom Streamlit settings:
```toml
[server]
port = 8501
headless = true

[theme]
primaryColor = "#667eea"
backgroundColor = "#0f1419"
secondaryBackgroundColor = "#1a202c"
textColor = "#e2e8f0"
```

## 🐛 Troubleshooting

### Common Issues

#### Issue: "ollama command not found"
**Solution:**
- Ensure Ollama is properly installed
- Restart your terminal/command prompt
- Check if Ollama is in your PATH

#### Issue: "No module named 'streamlit'"
**Solution:**
```bash
pip install streamlit
# or
pip install -r requirements.txt
```

#### Issue: "Connection refused" when trying to connect to Ollama
**Solution:**
1. Start Ollama service:
```bash
ollama serve
```
2. Verify Ollama is running:
```bash
ollama list
```

#### Issue: Model not found
**Solution:**
```bash
# Download the missing model
ollama pull model-name
```

#### Issue: Slow responses
**Solutions:**
- Use a smaller model (e.g., `gemma3` instead of `llama3`)
- Reduce temperature setting
- Ensure sufficient RAM available
- Close other resource-intensive applications

### Performance Optimization

#### For Better Performance:
1. **Use SSD storage** for faster model loading
2. **Allocate more RAM** to Ollama
3. **Use GPU acceleration** if available
4. **Choose appropriate model size** for your hardware

#### Model Size Recommendations:
- **4GB RAM**: Use 7B parameter models or smaller
- **8GB RAM**: Use 13B parameter models
- **16GB+ RAM**: Use larger models for better quality

## 🔒 Security Considerations

### Local-Only Setup
- All processing happens locally
- No data is sent to external servers
- Models run entirely on your machine

### Network Configuration
- Application runs on localhost by default
- To make accessible on network, modify Streamlit config
- **Warning**: Only expose to trusted networks

## 📱 Mobile Access

To access CommonChat AI from mobile devices on the same network:

1. Find your computer's IP address:
```bash
# Windows
ipconfig

# macOS/Linux
ifconfig
```

2. Run Streamlit with network access:
```bash
streamlit run app.py --server.address 0.0.0.0
```

3. Access from mobile: `http://YOUR_IP_ADDRESS:8501`

## 🆕 Updates

### Updating CommonChat AI
```bash
git pull origin main
pip install -r requirements.txt
```

### Updating Ollama Models
```bash
ollama pull model-name
```

## 💡 Tips & Best Practices

1. **Regular Updates**: Keep Ollama and models updated
2. **Model Management**: Remove unused models to save space
3. **Performance Monitoring**: Monitor system resources during use
4. **Backup**: Consider backing up your chat history if needed
5. **Customization**: Modify the UI/UX to your preferences

## 📞 Support

If you encounter issues not covered here:

1. Check the [GitHub Issues](https://github.com/hari7261/CommonChat-AI/issues)
2. Search existing issues for solutions
3. Create a new issue with:
   - Your operating system
   - Python version
   - Error messages
   - Steps to reproduce

---

Happy chatting! 🚀
