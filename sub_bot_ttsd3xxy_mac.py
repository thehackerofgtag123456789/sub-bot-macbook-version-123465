#!/usr/bin/env python3
"""
Author: mighty ghost hack
Remade for macOS
Target Channel: TTSD3XXY
Automation via Playwright (no pyautogui)
"""

from playwright.sync_api import sync_playwright
import socket
import time
import sys

# Channel URL (handle-style URL works best)
URL = "https://www.youtube.com/@TTSD3XXY"

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80), timeout=5)
        return True
    except OSError:
        return False

def main():
    print("Checking internet connection...")
    if not is_connected():
        print("❌ No internet connection")
        sys.exit(1)

    print("✅ Internet connected")
    print("Opening YouTube channel:", URL)

    with sync_playwright() as p:
        # Use Chromium (Chrome-like)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(URL, timeout=60000)
        time.sleep(5)

        # Try clicking Subscribe
        try:
            page.click("ytd-subscribe-button-renderer button", timeout=10000)
            print("✅ Subscribe clicked")
        except:
            print("⚠️ Subscribe button not found (already subscribed or layout changed)")

        # Try clicking Bell (may vary by account/layout)
        try:
            time.sleep(2)
            page.click("tp-yt-paper-icon-button", timeout=5000)
            print("🔔 Bell clicked")
        except:
            print("⚠️ Bell button not found")

        print("Automation finished. Browser will remain open until you close it.")
        input("Press Enter here or close the browser to exit...")
        # browser.close()  # optional: you can leave it commented to manually close

if __name__ == "__main__":
    main()
