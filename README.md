# IntelStream Auditor 

A lightweight, terminal-based cyber utility suite designed for Open-Source Intelligence (OSINT) footprinting, live telemetry system log monitoring, and Layer 4 network interface auditing. Built entirely in Python using native low-level socket handling and optimized web request pipelines.

## 🛠️ Features

* **Target Username OSINT Tracker:** Performs automated footprint mapping across popular public platforms (GitHub, GitLab, Reddit, LeetCode, Twitch) utilizing custom anti-fingerprinting HTTP headers and explicit redirect safety configurations.
* **Live Automated Log Monitor:** Emulates low-level system log trailing using non-blocking pointer shifting (`f.seek`). Actively streams and categorizes events (`[INFO]`, `[ALERT]`) based on real-time signature watchlists.
* **Layer 4 Remote Port Scanner:** Leverages raw `socket` architecture to run non-blocking multi-port connectivity audits against targeted hostnames or IP addresses with dynamic latency safety controls.

## 🚀 Quick Start

### Prerequisites
Ensure you have Python 3.x installed along with the `requests` library:
```bash
pip install requests
