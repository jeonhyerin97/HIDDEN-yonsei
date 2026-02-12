# -*- coding: utf-8 -*-
"""
Netlify 배포용 폴더 생성 스크립트
웹사이트에 필요한 파일들만 deploy 폴더로 복사합니다.
"""

import os
import shutil

# 현재 디렉토리
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPLOY_DIR = os.path.join(BASE_DIR, "deploy")

# 복사할 파일/폴더 목록
FILES_TO_COPY = [
    "index.html",
    "about.html",
    "projects.html",
    "drawings.html",
    "graphics.html",
    "exhibition.html",
    "study.html",
    "styles.css",
    "script.js",
    "CNAME",
    "tabs_config.json",
    "about_data.json",
    "home_data.json",
]

FOLDERS_TO_COPY = [
    "images",
]

def main():
    print("=" * 50)
    print("🚀 Netlify 배포용 폴더 생성 중...")
    print("=" * 50)
    print()
    
    # 기존 deploy 폴더 삭제
    if os.path.exists(DEPLOY_DIR):
        print("기존 deploy 폴더 삭제 중...")
        shutil.rmtree(DEPLOY_DIR)
    
    # 새 deploy 폴더 생성
    os.makedirs(DEPLOY_DIR)
    print(f"✅ deploy 폴더 생성: {DEPLOY_DIR}")
    print()
    
    # 파일 복사
    print("📄 파일 복사 중...")
    for file_name in FILES_TO_COPY:
        src = os.path.join(BASE_DIR, file_name)
        dst = os.path.join(DEPLOY_DIR, file_name)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  ✓ {file_name}")
        else:
            print(f"  ⚠ {file_name} (파일 없음)")
    print()
    
    # 폴더 복사
    print("📁 폴더 복사 중...")
    for folder_name in FOLDERS_TO_COPY:
        src = os.path.join(BASE_DIR, folder_name)
        dst = os.path.join(DEPLOY_DIR, folder_name)
        if os.path.exists(src):
            shutil.copytree(src, dst)
            print(f"  ✓ {folder_name}/")
        else:
            print(f"  ⚠ {folder_name}/ (폴더 없음)")
    print()
    
    print("=" * 50)
    print("✅ 배포 폴더 생성 완료!")
    print()
    print("📌 다음 단계:")
    print(f"   1. 탐색기에서 deploy 폴더 열기:")
    print(f"      {DEPLOY_DIR}")
    print()
    print("   2. Netlify (https://app.netlify.com) 접속")
    print()
    print("   3. Sites > 'drag and drop your site' 영역에")
    print("      deploy 폴더 내용물 드래그 앤 드롭")
    print("=" * 50)
    
    # 탐색기로 폴더 열기
    os.startfile(DEPLOY_DIR)

if __name__ == "__main__":
    main()
