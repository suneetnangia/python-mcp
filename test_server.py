#!/usr/bin/env python3
"""
Test script for the MCP Echo Server
"""

import requests
import json
from datetime import datetime


def test_http_endpoints():
    """Test the HTTP endpoints of the server"""
    base_url = "http://localhost:8000"

    print("Testing HTTP endpoints...")

    # Test root endpoint
    try:
        response = requests.get(f"{base_url}/")
        print(f"✓ Root endpoint: {response.status_code}")
        print(f"  Response: {response.json()}")
    except Exception as e:
        print(f"✗ Root endpoint failed: {e}")

    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        print(f"✓ Health endpoint: {response.status_code}")
        print(f"  Response: {response.json()}")
    except Exception as e:
        print(f"✗ Health endpoint failed: {e}")

    # Test echo endpoint
    try:
        test_data = {
            "message": "Hello from test script!",
            "metadata": {
                "test_run": datetime.now().isoformat(),
                "client": "test_script",
            },
        }

        response = requests.post(
            f"{base_url}/echo",
            json=test_data,
            headers={"Content-Type": "application/json"},
        )
        print(f"✓ Echo endpoint: {response.status_code}")
        print(f"  Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"✗ Echo endpoint failed: {e}")

    # Test raw echo endpoint
    try:
        raw_data = {
            "raw_message": "This is a raw test",
            "timestamp": datetime.now().isoformat(),
        }

        response = requests.post(
            f"{base_url}/echo-raw",
            json=raw_data,
            headers={"Content-Type": "application/json"},
        )
        print(f"✓ Raw echo endpoint: {response.status_code}")
        print(f"  Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"✗ Raw echo endpoint failed: {e}")


def main():
    """Main test function"""
    print("MCP Echo Server Test Script")
    print("=" * 40)

    # Check if server is running
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("Server is running, starting tests...")
            test_http_endpoints()
        else:
            print("Server responded but with error status")
    except requests.exceptions.RequestException:
        print("Server is not running. Please start it first with:")
        print("  python server.py")
        print("\nOr to start it in the background:")
        print("  python server.py &")
        return

    print("\n" + "=" * 40)
    print("Test completed!")


if __name__ == "__main__":
    main()
