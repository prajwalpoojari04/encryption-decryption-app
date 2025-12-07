@echo off
echo ========================================
echo   Push to GitHub Script
echo ========================================
echo.
echo This script will help you push to GitHub.
echo.
echo FIRST: Make sure you've created a repository on GitHub!
echo.
pause

echo.
echo Enter your GitHub username:
set /p GITHUB_USER=

echo.
echo Enter your repository name (e.g., encryption-decryption-app):
set /p REPO_NAME=

echo.
echo Connecting to GitHub...
git remote remove origin 2>nul
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git

echo.
echo Renaming branch to main...
git branch -M main

echo.
echo Pushing to GitHub...
echo (You'll be asked for username and password/token)
git push -u origin main

echo.
echo ========================================
if %errorlevel% equ 0 (
    echo SUCCESS! Your code is on GitHub!
    echo.
    echo Repository URL:
    echo https://github.com/%GITHUB_USER%/%REPO_NAME%
) else (
    echo ERROR: Push failed. Check your credentials.
    echo.
    echo Make sure:
    echo 1. Repository exists on GitHub
    echo 2. You're using Personal Access Token (not password)
    echo 3. Token has 'repo' permissions
)
echo ========================================
pause

