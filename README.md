# UU_PFAS_lab

Repository for PFAS quantitative calculations and analysis from the University of Utrecht Lab.

## Prerequisites & Setup Guide

### 1. Download and Install Python

#### Windows:
1. Visit [python.org](https://www.python.org/downloads/)
2. Click the **Download Python** button (latest stable version)
3. Run the installer executable
4. **Important**: Check the box that says **"Add Python to PATH"** during installation
5. Click **Install Now**
6. Verify installation by opening Command Prompt and typing:
   ```
   python --version
   ```

#### macOS:
1. Visit [python.org](https://www.python.org/downloads/)
2. Download the macOS installer
3. Run the installer and follow the prompts
4. Verify installation by opening Terminal and typing:
   ```
   python3 --version
   ```

#### Linux:
1. Open terminal and run:
   ```
   sudo apt-get update
   sudo apt-get install python3 python3-pip
   ```

---

### 2. Install Anaconda

Anaconda is a distribution that includes Python, conda (package manager), and pre-installed scientific packages.

#### Windows:
1. Visit [anaconda.com/download](https://www.anaconda.com/download)
2. Click **Download** for Windows (Anaconda3 - 64-bit recommended)
3. Run the installer (.exe file)
4. Follow the installation wizard
5. **Recommended**: Check "Add Anaconda3 to my PATH" during installation
6. Click **Install**
7. Verify installation by opening Command Prompt and typing:
   ```
   conda --version
   ```

#### macOS:
1. Visit [anaconda.com/download](https://www.anaconda.com/download)
2. Click **Download** for macOS (64-bit Graphical Installer recommended)
3. Run the installer
4. Follow the prompts
5. Verify installation by opening Terminal and typing:
   ```
   conda --version
   ```

#### Linux:
1. Visit [anaconda.com/download](https://www.anaconda.com/download)
2. Download the Linux installer
3. Open terminal and run:
   ```
   bash ~/Downloads/Anaconda3-latest-Linux-x86_64.sh
   ```
4. Follow the prompts and accept the license

---

### 3. Set Up Git and Link to GitHub

#### Install Git:

**Windows:**
1. Visit [git-scm.com](https://git-scm.com/)
2. Click **Download for Windows**
3. Run the installer and accept default settings
4. Click **Install**

**macOS:**
1. Open Terminal and run:
   ```
   brew install git
   ```
   (If Homebrew is not installed, visit [brew.sh](https://brew.sh/))

**Linux:**
1. Open terminal and run:
   ```
   sudo apt-get install git
   ```

#### Configure Git:
Open Command Prompt/Terminal and run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### Set Up GitHub SSH Key (Optional but Recommended):
1. Open Command Prompt/Terminal
2. Generate SSH key:
   ```
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
3. Press Enter to accept default location
4. Enter a passphrase (or leave blank)
5. Copy the public key:
   - **Windows**: 
     ```
     type %USERPROFILE%\.ssh\id_ed25519.pub
     ```
   - **macOS/Linux**: 
     ```
     cat ~/.ssh/id_ed25519.pub
     ```
6. Visit [github.com/settings/keys](https://github.com/settings/keys)
7. Click **New SSH key** and paste the copied key
8. Click **Add SSH key**

#### Alternative: Use GitHub Desktop (GUI Method):

GitHub Desktop provides a graphical interface for managing Git repositories without using the command line.

**Windows & macOS:**
1. Visit [desktop.github.com](https://desktop.github.com/)
2. Click **Download** for your operating system
3. Run the installer and follow the prompts
4. Launch GitHub Desktop
5. Sign in with your GitHub account:
   - Click **File** → **Options** (Windows) or **GitHub Desktop** → **Preferences** (macOS)
   - Click **Accounts** tab
   - Click **Sign in** and authenticate with your GitHub credentials
6. Configure your Git identity:
   - In Accounts settings, make sure your GitHub username and email are correct

**Linux:**
GitHub Desktop is not officially available for Linux. Use the command-line Git method above or consider using alternative tools like GitKraken.

---

### 4. Download This Repository

#### Method 1: Using GitHub Desktop (Easiest for Beginners):

### 4. Download This Repository

#### Method 1: Using GitHub Desktop (Easiest for Beginners):

1. Open GitHub Desktop (already installed and signed in from Section 3)
2. Click **File** → **Clone Repository** (or **Ctrl+Shift+O** on Windows, **Cmd+Shift+O** on macOS)
3. Click the **URL** tab
4. Paste the repository URL:
   ```
   https://github.com/valeriederijk/UU_PFAS_lab.git
   ```
5. Choose a local path where you want to save the repository
6. Click **Clone**
7. GitHub Desktop will download the repository to your computer
8. You can now open the repository folder and start working with the files

**Syncing with GitHub Desktop:**
- Any changes you make can be committed and pushed to GitHub using the GUI
- Click **Current Branch** to switch branches
- Click **Fetch Origin** to check for updates from the remote repository

#### Method 2: Using Git Command Line (Recommended):

1. Open Command Prompt/Terminal in the folder where you want to clone the repo
2. Run:
   ```
   git clone https://github.com/valeriederijk/UU_PFAS_lab.git
   ```
3. Navigate to the repository:
   ```
   cd UU_PFAS_lab
   ```

#### Method 3: Using HTTPS (If SSH is not configured):
```bash
git clone https://github.com/valeriederijk/UU_PFAS_lab.git
cd UU_PFAS_lab
```

#### Method 4: Download as ZIP (Alternative):
1. Visit the GitHub repository page
2. Click the **Code** button (green button)
3. Select **Download ZIP**
4. Extract the ZIP file to your desired location

---

### 5. Install Project Dependencies

Once you've cloned/downloaded the repository:

1. Open Command Prompt/Terminal in the repository folder
2. Create a conda environment (recommended):
   ```
   conda create -n pfas python=3.9
   conda activate pfas
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

---

## How to Use

This repository contains PFAS quantitative calculations. Key files:
- `Quantitative_calc_PFAS_clean2.ipynb` - Main Jupyter notebook for calculations
- `functions_quantitative.ipynb` - Supporting functions
- `rawdata/` - Input data files
- `results/` - Output results

To run the Jupyter notebook:
```bash
jupyter notebook Quantitative_calc_PFAS_clean2.ipynb
```

---

## Additional Resources

- [Python Documentation](https://docs.python.org/)
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Help](https://docs.github.com/)
- [Jupyter Notebook Guide](https://jupyter-notebook.readthedocs.io/)
