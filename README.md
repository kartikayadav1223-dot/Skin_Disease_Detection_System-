# Skin Disease Detection System

A comprehensive medical diagnostic platform powered by Django and AI.

## Features
- **AI Skin Analysis**: Instant diagnosis with confidence scores and multi-model consensus.
- **AI DermaAssistant**: Voice-enabled (TTS/STT) medical chat assistant.
- **Doctor Portal**: Verification system and appointment scheduling.
- **Billing System**: Automated medical invoicing with payment simulation.
- **Admin Dashboard**: System-wide statistics and data management.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd skin_detection_project
   ```

2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Start Application**:
   ```bash
   python manage.py runserver
   ```

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Bootstrap 5, Vanilla JS, Web Speech API
- **AI Model**: TensorFlow/Keras (Simulated CNN)
- **Database**: SQLite3 (Local) / Ready for MySQL

## Credits
Developed for Advanced Medical Diagnostics and Skin Health Awareness.
