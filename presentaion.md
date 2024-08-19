# BookAI: Automated Book Generation System

## Overview
BookAI is a sophisticated web application designed to automate the creation of detailed books on various topics. Leveraging advanced AI models from OpenAI and Together, BookAI allows users to generate comprehensive content in multiple languages, which can then be downloaded or saved as PDF documents. The system also includes features for user authentication, API key management, and image generation using AI.

## Key Features

### 1. **AI-Powered Book Generation**
- **Multi-API Support**: Utilizes both OpenAI and Together APIs for generating book content.
- **Language Support**: Capable of generating books in multiple languages.
- **Progress Tracking**: Real-time progress updates during book generation.

### 2. **PDF Generation and Management**
- **Dynamic PDF Creation**: Converts generated text into downloadable PDF format.
- **Database Storage**: Stores metadata of generated PDFs in an SQLite database.
- **User-Specific Downloads**: Allows users to download their previously generated PDFs.

### 3. **API Key Management**
- **Secure API Key Generation**: Generates and manages API keys for secure access.
- **Database Integration**: Stores API keys in a secure SQLite database.

### 4. **User Authentication**
- **Firebase Integration**: Uses Firebase for user registration and authentication.
- **Secure Token Handling**: Manages user sessions securely using Firebase tokens.

### 5. **Image Generation**
- **AI-Based Image Creation**: Uses AI to generate images based on user prompts.
- **Base64 Encoding**: Returns images in a base64 encoded format for easy embedding.

## Technical Architecture

### **Frontend**
- **Flask Templates**: Utilizes Flask's templating engine for rendering HTML pages.
- **AJAX/Fetch API**: Handles asynchronous requests for book generation and progress tracking.

### **Backend**
- **Flask Framework**: Python-based web framework for handling HTTP requests.
- **AsyncIO**: Asynchronous I/O for efficient handling of concurrent tasks.
- **SQLite Database**: Lightweight, serverless database for storing PDF metadata and API keys.

### **AI Integration**
- **OpenAI API**: For generating detailed text content.
- **Together API**: Alternative API for text generation with different models.
- **GetImg.ai API**: For generating images based on textual prompts.

### **Security**
- **Firebase Authentication**: Secure user authentication and session management.
- **API Key Security**: Secure handling and storage of API keys.

## Installation and Setup

### **Prerequisites**
- Python 3.7+
- Flask
- OpenAI Python client
- Together Python client
- Firebase Admin SDK
- SQLite

### **Environment Variables**
- `OPENAI_API_KEY`
- `TOGETHER_API_KEY`
- `GETIMG_API_KEY`

### **Running the Application**
```bash
# Clone the repository
git clone https://github.com/your-repo/BookAI.git
cd BookAI

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export OPENAI_API_KEY='your-openai-key'
export TOGETHER_API_KEY='your-together-key'
export GETIMG_API_KEY='your-getimg-key'

# Run the application
python app.py
```

## Future Enhancements
- **Enhanced User Interface**: Improved frontend with better user experience.
- **More Language Support**: Expansion to more languages for book generation.
- **Advanced Image Generation**: Integration with more advanced image generation models.
- **User Roles and Permissions**: Role-based access control for API usage.

## Conclusion
BookAI represents a cutting-edge solution for automated book generation, combining powerful AI models with robust backend services. Its ability to generate detailed, multilingual content and manage user interactions securely makes it a valuable tool for authors, educators, and content creators.
