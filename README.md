# 🚀 CommonChat AI

A beautiful, private AI chat application built with Streamlit and powered by Ollama. Experience intelligent conversations with a clean, modern interface that keeps your data completely local and secure.

![CommonChat AI](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 🔐 **100% Private**: All conversations stay on your local machine
- ⚡ **Fast & Responsive**: Real-time streaming responses
- 🎨 **Beautiful UI**: Clean, modern dark blue theme
- 🤖 **Multiple Models**: Support for various Ollama models
- 🎛️ **Customizable**: Adjustable temperature and model settings
- 📱 **Responsive Design**: Works great on all screen sizes

## 🖼️ Screenshots

### Main Interface
![CommonChat AI Interface](/image.png)



## 🚀 Quick Start

### Prerequisites

Before running CommonChat AI, make sure you have:

1. **Python 3.8+** installed
2. **Ollama** installed and running
3. At least one Ollama model downloaded

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/hari7261/CommonChat-AI.git
cd CommonChat-AI
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Install and setup Ollama**
```bash
# Install Ollama (visit https://ollama.ai for installation instructions)
# Download a model (e.g., gemma3)
ollama pull gemma3
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser** and navigate to `http://localhost:8501`

## 🔧 Configuration

### Available Models

The application supports various Ollama models:
- `gemma3` (default)
- `llama3`
- `mistral`
- `codellama`

### Temperature Settings

Adjust the creativity of responses:
- **0.0-0.3**: More focused and deterministic
- **0.4-0.7**: Balanced (default: 0.7)
- **0.8-1.0**: More creative and random

## 📁 Project Structure

```
CommonChat-AI/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── LICENSE            # MIT License
├── .gitignore         # Git ignore rules
└── docs/              # Additional documentation
    └── SETUP.md       # Detailed setup guide
```

## 🛠️ Development

### Local Development

1. **Fork the repository**
2. **Create a feature branch**
```bash
git checkout -b feature/your-feature-name
```

3. **Make your changes**
4. **Test thoroughly**
5. **Commit and push**
```bash
git commit -m "Add your feature description"
git push origin feature/your-feature-name
```

6. **Create a Pull Request**

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Keep functions small and focused

## 🔒 Privacy & Security

CommonChat AI is designed with privacy as a core principle:

- **No Data Collection**: We don't collect or store any personal data
- **Local Processing**: All AI processing happens on your machine
- **No External Calls**: Except for Ollama, no external services are used
- **Open Source**: Complete transparency with open-source code

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Report Bugs**: Use the issue tracker to report bugs
2. **Suggest Features**: Propose new features via issues
3. **Submit PRs**: Help improve the code
4. **Documentation**: Help improve our docs
5. **Testing**: Help test on different platforms

### Contributors

- **[@hari7261](https://github.com/hari7261)** - Creator & Maintainer

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[Ollama](https://ollama.ai)** - For providing excellent local AI models
- **[Streamlit](https://streamlit.io)** - For the amazing web app framework
- **[Inter Font](https://fonts.google.com/specimen/Inter)** - For the beautiful typography

## 📧 Support

Need help? Here's how to get support:

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and community chat
- **Email**: [Your email if you want to provide it]

## 🌟 Star History

If you found this project helpful, please consider giving it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=hari7261/CommonChat-AI&type=Date)](https://star-history.com/#hari7261/CommonChat-AI&Date)

---

Made with ❤️ by [Hariom](https://github.com/hari7261)
