# 🎮 Discord Quest Spoofer (Windows / Linux)

Safely spoofs Discord Quest playtime **without** downloading the game, running Wine, or injecting sketchy JavaScript into Discord's developer console. Works on both Windows and Linux.

> **Tested with:** Arknights: Endfield (`1461154307171811401`)

---

## ⚠️ Why Not JS Injection?

Console scripts that hijack Webpack or spam Discord's internal API are **detectable**. Discord's native scanner compares UI state against actual OS processes — mismatches get flagged. Don't be that guy.

---

## 🧠 How It Works

Discord scans the process list for known game executables. This tool:

1. **Compiles** a standalone binary from Python using PyInstaller.
2. **Renames** it to match the target game's executable (e.g., `Endfield.exe`).
3. **Broadcasts** a legitimate Local RPC handshake to Discord via the standard IPC socket — the same way any real game would.

No memory injection. No Webpack hijacking. The OS-level scanner sees the right process name; Discord's RPC sees a valid handshake. ✅

---

## 📦 Prerequisites

```bash
pip install pypresence pyinstaller
```

---

## 🚀 Usage

### 1. Compile the binary

```bash
pyinstaller --onefile discord_presence.py
```

PyInstaller outputs the binary as `dist/discord_presence` (Linux) or `dist/discord_presence.exe` (Windows). The next step renames it to match the game executable Discord is looking for.

### 2. Rename it to match the game

**Linux:**
```bash
mv dist/discord_presence dist/Endfield.exe
```

**Windows (PowerShell):**
```powershell
Rename-Item dist\discord_presence.exe dist\Endfield.exe
```

> Swap `Endfield.exe` for whatever executable name Discord associates with your target quest/game.

### 3. Run it

**Linux:**
```bash
cd dist && ./Endfield.exe <APPLICATION_ID>
```

**Windows (PowerShell / cmd):**
```powershell
cd dist && .\Endfield.exe <APPLICATION_ID>
```

**Example (Arknights: Endfield):**

```bash
cd dist && ./Endfield.exe 1461154307171811401
```

Discord should now show you as "In-Game" and begin counting playtime toward the quest.  
Press `Ctrl+C` to stop.

---

## 🔍 Finding the Application ID

1. Open Discord → Settings → Game Activity
2. Add the game manually if it doesn't auto-detect
3. The Application ID is visible in the quest details or can be found via [Discord's developer portal](https://discord.com/developers/applications)

---

## 📁 Project Structure

```
.
├── discord_presence.py   # Main RPC spoofer script
├── discord_presence.spec # PyInstaller build spec (generated after first compile)
└── dist/
    └── discord_presence  # Compiled binary — rename to match the target game exe
```

---

## 🛠️ Script Overview

```python
# discord_presence.py
RPC = Presence(client_id)
RPC.connect()
RPC.update(state="In-Game", details="Completing Quest")
```

Connects to Discord's local RPC socket and broadcasts a presence update every 15 seconds — keeping the session alive until interrupted.

---

## 📜 License

Do whatever you want. Just don't blame me if Discord updates their detection. 🤷
