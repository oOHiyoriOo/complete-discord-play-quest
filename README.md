# 🎮 Discord Quest Spoofer (Linux/Ubuntu)

Safely spoofs Discord Quest playtime on Linux **without** downloading the game, running Wine, or injecting sketchy JavaScript into Discord's developer console.

> **Tested with:** Arknights: Endfield (`1461154307171811401`)

---

## ⚠️ Why Not JS Injection?

Console scripts that hijack Webpack or spam Discord's internal API are **detectable**. Discord's native scanner compares UI state against actual OS processes — mismatches get flagged. Don't be that guy.

---

## 🧠 How It Works

Discord's Linux client scans the process list for known game executables. This tool:

1. **Compiles** a native Linux ELF binary from Python using PyInstaller.
2. **Renames** it to match the target game's executable (e.g., `Endfield.exe`).
3. **Broadcasts** a legitimate Local RPC handshake to Discord via the standard IPC socket — the same way any real game would.

No Wine. No memory injection. No Webpack hijacking. The OS-level scanner sees the right process name; Discord's RPC sees a valid handshake. ✅

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

### 2. Rename it to match the game

```bash
mv dist/discord_presence dist/Endfield.exe
```

> Swap `Endfield.exe` for whatever executable name Discord associates with your target quest/game.

### 3. Run it

```bash
cd dist && ./Endfield.exe <APPLICATION_ID>
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
├── discord_presence.spec # PyInstaller build spec
└── dist/
    └── Endfield.exe      # Compiled native Linux binary (rename as needed)
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
