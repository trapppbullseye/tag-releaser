#!/usr/bin/env python3
"""Auto-tag and release on version bump"""
import argparse
def main():
 p=argparse.ArgumentParser(description="Auto-tag and release on version bump")
 p.add_argument("--version",action="store_true")
 args=p.parse_args()
 if args.version:print("tag-releaser v0.1.0");return
 print(f"[12:00] tag-releaser ready")
if __name__=="__main__":main()
