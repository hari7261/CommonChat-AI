# Contributing to CommonChat AI

First off, thank you for considering contributing to CommonChat AI! It's people like you that make CommonChat AI such a great tool.

## 🤝 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## 🐛 How to Report Bugs

Before creating bug reports, please check the existing issues as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

### Bug Report Template
```
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS Big Sur]
 - Python Version: [e.g. 3.9.0]
 - Streamlit Version: [e.g. 1.28.0]
 - Ollama Version: [e.g. 0.1.7]

**Additional context**
Add any other context about the problem here.
```

## 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Clear title** and description of the enhancement
- **Step-by-step description** of the suggested enhancement
- **Explain why this enhancement would be useful**
- **Include screenshots** or mockups if applicable

## 🔧 Development Process

### Setting Up Development Environment

1. **Fork the repository**
2. **Clone your fork**
```bash
git clone https://github.com/hari7261/CommonChat-AI.git
cd CommonChat-AI
```

3. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate  # Windows
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Create a feature branch**
```bash
git checkout -b feature/amazing-feature
```

### Making Changes

1. **Make your changes** in your feature branch
2. **Follow the coding standards** (see below)
3. **Test your changes** thoroughly
4. **Add or update documentation** as needed

### Coding Standards

- **Follow PEP 8** for Python code style
- **Use meaningful variable names**
- **Add comments** for complex logic
- **Keep functions small** and focused
- **Use type hints** where appropriate

Example:
```python
def calculate_temperature_emoji(temperature: float) -> str:
    """
    Return appropriate emoji based on temperature value.
    
    Args:
        temperature: Float between 0.0 and 1.0
        
    Returns:
        Emoji string representing temperature level
    """
    if temperature < 0.3:
        return "🧊"
    elif temperature < 0.7:
        return "❄️"
    else:
        return "🔥"
```

### Testing

Before submitting your changes:

1. **Test the application** manually
2. **Test with different models** if applicable
3. **Test on different screen sizes** for UI changes
4. **Verify no console errors** in browser

### Submitting Changes

1. **Commit your changes**
```bash
git add .
git commit -m "Add amazing feature

- Detailed description of what was added
- Why it was added
- Any breaking changes"
```

2. **Push to your fork**
```bash
git push origin feature/amazing-feature
```

3. **Create a Pull Request**
   - Use a clear, descriptive title
   - Include a detailed description
   - Reference any related issues
   - Include screenshots for UI changes

### Pull Request Template
```
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
- [ ] Manual testing
- [ ] Different models tested
- [ ] Different browsers tested
- [ ] Mobile responsiveness checked

## Screenshots (if applicable)
[Add screenshots here]

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
```

## 📋 Project Areas for Contribution

### High Priority
- **Performance optimizations**
- **Mobile responsiveness improvements**
- **Accessibility features**
- **Error handling enhancements**

### Medium Priority
- **Additional model support**
- **UI/UX improvements**
- **Documentation improvements**
- **Testing framework**

### Ideas for New Features
- **Chat history export/import**
- **Theme customization**
- **Keyboard shortcuts**
- **Chat search functionality**
- **Multi-language support**

## 🎨 UI/UX Guidelines

When contributing to the user interface:

- **Maintain the dark blue theme**
- **Ensure responsive design**
- **Keep accessibility in mind**
- **Test on multiple screen sizes**
- **Use consistent spacing and typography**

## 📚 Documentation Contributions

Documentation improvements are always welcome:

- **Fix typos or grammar**
- **Add missing information**
- **Improve explanations**
- **Add examples**
- **Update outdated information**

## 🏷️ Issue Labels

We use the following labels to categorize issues:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed
- `question` - Further information is requested

## 🎉 Recognition

Contributors will be:
- **Listed in the README**
- **Mentioned in release notes**
- **Given credit in the project**

## 📞 Questions?

Don't hesitate to ask questions:

- **Create an issue** with the `question` label
- **Join our discussions** in GitHub Discussions
- **Check existing issues** and discussions first

## 📄 License

By contributing to CommonChat AI, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to CommonChat AI! 🚀
