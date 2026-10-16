"""
Campus Safety Guide AI Agent - Web Application Backend
CIE-3 Generative AI, LLM & Agentic AI Assignment
"""
import os
import sys
import uuid
import datetime
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from rag_engine import CampusSafetyRAG
# Load environment variables (.env if present)
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'campus-safety-agent-cie3-key-2026')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KB_DIR = os.path.join(BASE_DIR, 'knowledge_base')
# Initialize RAG Engine
rag_engine = CampusSafetyRAG(KB_DIR)
# In-memory session store (transient, no sensitive user data stored)
sessions = {}
@app.route('/')
def index():
    """Serves the Campus Safety Guide AI Dashboard."""
    return render_template('index.html')
@app.route('/api/status', methods=['GET'])
def get_status():
    """Returns the operational status, active mode, and knowledge base stats."""
    has_gemini = bool(os.getenv("GEMINI_API_KEY", "").strip())
    has_openai = bool(os.getenv("OPENAI_API_KEY", "").strip())
